l = [2,3,4,5,5,3,5,667,5,3,3,5,6,7,6,43,23,3]

def assending(l):
    for i in range(len(l)):
        for j in range(len(l)):
            if(l[j]>l[i]):
                temp = l[j]
                l[j]=l[i]
                l[i]=temp

def dessending(l):
    for i in range(len(l)):
        for j in range(len(l)):
            if(l[j]<l[i]):
                temp = l[j]
                l[j]=l[i]
                l[i]=temp
ys = 'y'
while(ys == "y" or ys == "Y"):
    print('_________________________________****____________________________')
    print("1 for assending.....")
    print("2 for dessending....")
    n = int(input("Enter a number for assending or dessending :- "))
    print('_________________________________****____________________________')
    print("\n")
    print('___________OUTPUT__________')
    if(n == 1):
        assending(l)
        print(l)
    elif(n==2):
        dessending(l)
        print(l)
    elif(n==3):
        print("You have been exited from program")
        exit()
    else:
        print('You have entered a wrong value. Please enter a right value 1 or 2')
        ag = input('Enter Y/N for checking values again :- ')
    ys = input('Enter Y/N for continue :- ')
# print(l)
# for i in l:
#     print(l)