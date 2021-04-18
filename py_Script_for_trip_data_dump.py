from os import listdir
from os.path import isfile, join
from datetime import time,datetime
import psycopg2
import csv
import random
from psycopg2 import sql
import uuid
import re


mypath = "/home/devender/Desktop/Scarpping/dump data script/Dec19-data-monitoring-sheet.csv"
provider_id = "7bc3e5c5-5439-44d8-b2a2-1e2a09a167fb"
# conn
# cur
def db_connection():
    conn = psycopg2.connect(host="15.206.238.207",dbname="adlp", user="adlpadmin", password="adlpadmin1-2")
    cur = conn.cursor()
    return conn,cur

def connection_close(conn,cur):
    if conn is not None:
        # conn.commit()
        cur.close()
        conn.close()
        print('Database connection closed.')


def vehicle_data(conn,cur,crbx_user_id,crbx_vehicle_id,created_date,data_sheet_file_name,last_modified_date,vin):
    # Staging server
    # cur = conn.cursor()


    rows_inserted = 0
    row_not_inserted = []
    try:
        # print(tuple(arr))

        cur.execute('''INSERT INTO adlp.vehicle (crbx_user_id,crbx_vehicle_id,created_date,data_sheet_file_name,last_modified_date,vin) VALUES ('{}','{}','{}','{}','{}','{}') RETURNING id;''' .format(crbx_user_id,crbx_vehicle_id,created_date,data_sheet_file_name,last_modified_date,vin))
        return_id = cur.fetchall()
        print(return_id)
        conn.commit()
        rows_inserted+=1

        return return_id

    except (Exception, psycopg2.DatabaseError) as error:
        row_not_inserted.append(1)
        print(error)
        connection_close(conn,cur)

        exit()
        # break
        # break
    print("rows_inserted",rows_inserted)
    print("row_not_inserted",row_not_inserted)

def csv_data(conn,cur,column_names,row_data):
    # Staging server
    cur = conn.cursor()


    rows_inserted = 0
    row_not_inserted = []
    try:
        # print(tuple(arr))

        cur.execute(sql.SQL('''INSERT INTO adlp.trip_data_main ({}) VALUES {}'''.format(column_names,row_data)))
        # return_id = cur.fetchall()
        # print(return_id)
        conn.commit()
        rows_inserted+=1

        # return return_id

    except (Exception, psycopg2.DatabaseError) as error:
        row_not_inserted.append(1)
        print(error)
        connection_close(conn,cur)

        exit()

        # break
    print("rows_inserted",rows_inserted)
    print("row_not_inserted",row_not_inserted)

    # connection_close(conn,cur)

    
    
def csv_read(csv_file):
    file_name = "1a704864_data_60"

    n = random.randint(000,999)
    # 2012,Ford,Ex
    crbx_vehicle_id = "FORDEX2012"+str(n)
    print("crbx_vehicle_id",crbx_vehicle_id)
    created_date = datetime.now().strftime("%Y-%m-%d")
    vin="MZ7AD1CDM2H000002"

    with open(mypath+'/'+csv_file, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

        print(data[2])
        for x in range(len(data[2])):
            if len(data[2][x]) == 2 and (data[2][x][0]== 'x' or data[2][x][0]== 'y' or data[2][x][0]== 'z'):
                data[2][x] = data[2][x][0]+str(int(data[2][x][1])+1)
            
            # if data[2][x] =='x10' or data[2][x] =='y10' or data[2][x] =='z10':
            
            elif len(data[2][x]) == 3 and (data[2][x][0]== 'x' or data[2][x][0]== 'y' or data[2][x][0]== 'z'):
                data[2][x] = data[2][x][0]+str(int(data[2][x][1]+data[2][x][2])+1)
                # print(d)
        data[2].append("vehicle_id")
        data[2].append("crbx_vehicle_id")
        data[2].append("crbx_trip_id")
        data[2].append("crbx_user_id")
        data[2].append("data_sheet_file_name")
        # for x in range(len(data[2])):
        #     data[2][x] = data[2][x][1:-1]
        column_string = ','.join(data[2])
        # print(data[2])
        print(column_string)

        connection,curs = db_connection()
        vehicle_id = vehicle_data(connection,curs,provider_id,crbx_vehicle_id,created_date,csv_file,created_date,vin)
        crbx_trip_id = uuid.uuid1()
        trip_data_array = []

        for x in range(3,len(data)):
            # print(re.match(r'\d{1,2}/\d{1,2}/\d{4} \d{2}:\d{2}', data[x][0]),data[x][0])
            if re.match(r'\d{1,2}/\d{1,2}/\d{4} \d{1,2}:\d{1,2}', data[x][0]) or re.match(r'\d{1,2}/\d{1,2}/\d{4} \d{1,2}:\d{1,2}:\d{1,2}', data[x][0]):
                print(csv_file,"     TRIP row no. ", x)
                data[x].append(vehicle_id[0][0])
                data[x].append(crbx_vehicle_id)
                data[x].append(crbx_trip_id)
                data[x].append(provider_id)
                data[x].append(csv_file)

                trip_data_array.append(tuple(data[x]))

            elif data[x][0] == "TRIP END":
                crbx_trip_id = uuid.uuid1()

            # else: 
                # daaaaa= ','.join(trip_data_array)
                # print(daaaaa)
            if x%1000 == 0 or x == (len(data)-1):

                var = ''
                for i in range(len(trip_data_array)):
                    if i < (len(trip_data_array)-1):
                        var+=str(trip_data_array[i])+","
                    elif i == (len(trip_data_array)-1):
                        var+=str(trip_data_array[i])

                print(" inserting data to db ")
                # print("var",var)
                csv_data(connection,curs,column_string,var)
                
                trip_data_array = []

                # print("else",trip_data_array)
                # break
        
        # connection.commit()
        connection_close(connection,curs)
        # print( vehicle_id)


        # for d in data:
        #     print(d)
        #     break


if __name__ == '__main__':
    # data()
    # mypath = "/home/amantya/AmantyaTech/AmantyaProjects/ADLP/Resources-Trip-Data/60-Day-100-Vehicle-Data-in-csv/60 Day"
    qinserted_sheet_list=[]
    all_csv_files_name_list = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for csv_file in all_csv_files_name_list:
        print("file name:::",csv_file)
        if csv_file != ".DS_Store":
            csv_read(csv_file)
            inserted_sheet_list.append(csv_file)

    # print(all_csv_files_name_list)
    