import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from  pyspark.sql.functions import regexp_replace,col,concat,lit
import pyspark.sql.functions as F
import re
from awsglue.dynamicframe import DynamicFrame
import boto3

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
## @type: DataSource
## @args: [database = "amantya-bronze-db", table_name = "autondtv_usedcar", transformation_ctx = "datasource0"]
## @return: datasource0
## @inputs: []
datasource0 = glueContext.create_dynamic_frame.from_catalog(database = "amantya-bronze-db", table_name = "autondtv_usedcar", transformation_ctx = "datasource0")
## @type: ApplyMapping
## @args: [mapping = [("adjustable_power_steering", "string", "adjustable_power_steering", "string"), ("boot_space", "string", "boot_space", "string"), ("brand_name", "string", "brand_name", "string"), ("brand_price", "string", "brand_price", "string"), ("clutch_type", "string", "clutch_type", "string"), ("damage", "string", "damage", "string"), ("displacement_cc", "string", "displacement_cc", "string"), ("drive_train", "string", "drive_train", "string"), ("emission", "string", "emission", "string"), ("emission_standard", "string", "emission_standard", "string"), ("emission_type", "string", "emission_type", "string"), ("engine_cc", "string", "engine_cc", "string"), ("engine_type", "string", "engine_type", "string"), ("front_brake_type", "string", "front_brake_type", "string"), ("front_suspension", "string", "front_suspension", "string"), ("front_track", "string", "front_track", "string"), ("front_tyre_size", "string", "front_tyre_size", "string"), ("fuel", "string", "fuel", "string"), ("fuel_tank_capacity", "double", "fuel_tank_capacity", "double"), ("gearbox", "string", "gearbox", "string"), ("gross_weight", "string", "gross_weight", "string"), ("ground_clearance", "string", "ground_clearance", "string"), ("height", "string", "height", "string"), ("kms_run", "string", "kms_run", "string"), ("kerb_weight", "string", "kerb_weight", "string"), ("length", "string", "length", "string"), ("mfg_date", "string", "mfg_date", "string"), ("max_speed", "long", "max_speed", "long"), ("mileage", "string", "mileage", "string"), ("mileage_city", "string", "mileage_city", "string"), ("mileage_highway", "string", "mileage_highway", "string"), ("minimum_turning_radius", "string", "minimum_turning_radius", "string"), ("no_of_cylinder", "long", "no_of_cylinder", "long"), ("no_of_doors", "long", "no_of_doors", "long"), ("no_of_gears", "string", "no_of_gears", "string"), ("owner_count", "string", "owner_count", "string"), ("performance_0_to_100_kmph", "string", "performance_0_to_100_kmph", "string"), ("place", "string", "place", "string"), ("power", "string", "power", "string"), ("power_steering", "string", "power_steering", "string"), ("rear_brake_type", "string", "rear_brake_type", "string"), ("rear_suspension", "string", "rear_suspension", "string"), ("rear_track", "string", "rear_track", "string"), ("rear_tyre_size", "string", "rear_tyre_size", "string"), ("seating_capacity", "long", "seating_capacity", "long"), ("steering_type", "string", "steering_type", "string"), ("torque", "string", "torque", "string"), ("tyre_type", "string", "tyre_type", "string"), ("wheel_type", "string", "wheel_type", "string"), ("wheelbase", "string", "wheelbase", "string"), ("width", "string", "width", "string")], transformation_ctx = "applymapping1"]
## @return: applymapping1
## @inputs: [frame = datasource0]
applymapping1 = ApplyMapping.apply(frame = datasource0, mappings = [
    ("adjustable_power_steering", "string", "adjustable_power_steering", "string"), 
    ("boot_space", "string", "boot_space", "string"), 
    ("brand_name", "string", "brand_name", "string"), 
    ("brand_price", "string", "brand_price", "string"), 
    ("clutch_type", "string", "clutch_type", "string"), 
    ("damage", "string", "damage", "string"), 
    ("displacement_cc", "string", "displacement_cc", "string"), 
    ("drive_train", "string", "drive_train", "string"), 
    ("emission", "string", "emission", "string"), 
    ("emission_standard", "string", "emission_standard", "string"), 
    ("emission_type", "string", "emission_type", "string"), 
    ("engine_cc", "string", "engine_cc", "string"), 
    ("engine_type", "string", "engine_type", "string"), 
    ("front_brake_type", "string", "front_brake_type", "string"), 
    ("front_suspension", "string", "front_suspension", "string"), 
    ("front_track", "string", "front_track", "string"), 
    ("front_tyre_size", "string", "front_tyre_size", "string"), 
    ("fuel", "string", "fuel", "string"), 
    ("fuel_tank_capacity", "double", "fuel_tank_capacity", "double"), 
    ("gearbox", "string", "gearbox", "string"), 
    ("gross_weight", "string", "gross_weight", "string"), 
    ("ground_clearance", "string", "ground_clearance", "string"), 
    ("height", "string", "height", "string"), 
    ("kms_run", "string", "kms_run", "string"), 
    ("kerb_weight", "string", "kerb_weight", "string"), 
    ("length", "string", "length", "string"), 
    ("mfg_date", "string", "mfg_date", "string"), 
    ("max_speed", "long", "max_speed", "long"), 
    ("mileage", "string", "mileage", "string"), 
    ("mileage_city", "string", "mileage_city", "string"), 
    ("mileage_highway", "string", "mileage_highway", "string"), 
    ("minimum_turning_radius", "string", "minimum_turning_radius", "string"), 
    ("no_of_cylinder", "long", "no_of_cylinder", "long"), 
    ("no_of_doors", "long", "no_of_doors", "long"), 
    ("no_of_gears", "string", "no_of_gears", "string"), 
    ("owner_count", "string", "owner_count", "string"), 
    ("performance_0_to_100_kmph", "string", "performance_0_to_100_kmph", "string"), 
    ("place", "string", "place", "string"), 
    ("power", "string", "power", "string"), 
    ("power_steering", "string", "power_steering", "string"), 
    ("rear_brake_type", "string", "rear_brake_type", "string"), 
    ("rear_suspension", "string", "rear_suspension", "string"), 
    ("rear_track", "string", "rear_track", "string"), 
    ("rear_tyre_size", "string", "rear_tyre_size", "string"), 
    ("seating_capacity", "long", "seating_capacity", "long"), 
    ("steering_type", "string", "steering_type", "string"), 
    ("torque", "string", "torque", "string"), 
    ("tyre_type", "string", "tyre_type", "string"), 
    ("wheel_type", "string", "wheel_type", "string"), 
    ("wheelbase", "string", "wheelbase", "string"), 
    ("width", "string", "width", "string")
    ], transformation_ctx = "applymapping1")
## @type: SelectFields
## @args: [paths = ["adjustable_power_steering", "boot_space", "brand_name", "brand_price", "clutch_type", "damage", "displacement_cc", "drive_train", "emission", "emission_standard", "emission_type", "engine_cc", "engine_type", "front_brake_type", "front_suspension", "front_track", "front_tyre_size", "fuel", "fuel_tank_capacity", "gearbox", "gross_weight", "ground_clearance", "height", "kms_run", "kerb_weight", "length", "mfg_date", "max_speed", "mileage", "mileage_city", "mileage_highway", "minimum_turning_radius", "no_of_cylinder", "no_of_doors", "no_of_gears", "owner_count", "performance_0_to_100_kmph", "place", "power", "power_steering", "rear_brake_type", "rear_suspension", "rear_track", "rear_tyre_size", "seating_capacity", "steering_type", "torque", "tyre_type", "wheel_type", "wheelbase", "width"], transformation_ctx = "selectfields2"]
## @return: selectfields2
## @inputs: [frame = applymapping1]

df=applymapping1.toDF()
df1=(df.withColumn('boot_space_in_l',regexp_replace('boot_space',"[^0-9|.]",''))
            .drop('boot_space')
            .withColumn('brand_name', regexp_replace('brand_name',"VI",'6'))
            .withColumn('brand_name', regexp_replace('brand_name',"IV",'4'))
            .withColumn("brand_price_in",F.when(col("brand_price").contains('Lakh'),regexp_replace('brand_price',"[^0-9|.]",'')*100000))
            .withColumn('brand_price_in',regexp_replace('brand_price_in',"[^0-9|.]",''))
            .withColumn('brand_price_in',regexp_replace('brand_price_in',"NA",''))
            .withColumn("currency", F.lit("INR"))
            .drop("brand_price")
            .withColumn('displacement_cc', regexp_replace('displacement_cc',"[^0-9|.]",''))
            .withColumn('emission_std', F.concat(F.col('emission'), F.col('emission_standard'), F.col('emission_type')))
            .drop('emission')
            .drop('emission_standard')
            .drop('emission_type')
            .withColumn('emission_std', regexp_replace('emission_std',"VI",'6'))
            .withColumn('emission_std', regexp_replace('emission_std',"IV",'4'))
            .withColumn('emission_std', regexp_replace('emission_std',"II",'2'))
            .withColumn('emission_std', regexp_replace('emission_std',"I",'1'))
            .withColumn('engine_cc', regexp_replace('engine_cc',"CC",''))
            .withColumn('front_brake_type', regexp_replace('front_brake_type',"\\?",''))
            .withColumn('front_track_in_mm', regexp_replace('front_track', '[^0-9|.]', ''))
            .drop('front_track')
            .withColumn('front_suspension', regexp_replace('front_suspension',"\\?",''))
            .withColumn('front_tyre_size', regexp_replace('front_tyre_size',"\\`",''))
            .withColumn('front_tyre_size', F.split(F.col("front_tyre_size"),"/").getItem(0))
            .withColumn('front_tire_width_size',regexp_replace('front_tyre_size',"145128",''))
            .withColumn('front_tire_width_size',regexp_replace('front_tyre_size',"15513",''))
            .withColumn('front_tire_width_size', F.split(F.col("front_tire_width_size"),"R").getItem(0))
            .withColumn('front_tire_width_size',regexp_replace('front_tire_width_size',"[^0-9|.]",''))
            .drop('front_tyre_size')
            .withColumn('fuel_tank_capacity',regexp_replace('fuel_tank_capacity',"[^0-9|.]",''))
            .withColumn('gears', F.concat(F.col('no_of_gears'), F.col('gearbox')))
            .drop('no_of_gears')
            .drop('gearbox')
            .withColumn('gross_weight_in_kg',regexp_replace('gross_weight',"[^0-9|.]",''))
            .drop('gross_weight')
            .withColumn('ground_clearance_in_mm',regexp_replace('ground_clearance',"[^0-9|.]",''))
            .drop('ground_clearance')
            .withColumn('height_in_mm',regexp_replace('height',"[^0-9|.]",''))
            .drop('height')
            .withColumn('kms_run',regexp_replace('kms_run',"[^0-9|.]",''))
            .withColumn('kerb_weight_in_kg',regexp_replace('kerb_weight',"[^0-9|.]",''))
            .drop('kerb_weight')
            .withColumn('length_in_mm',regexp_replace('length',"[^0-9|.]",''))
            .drop('length')
            .withColumn('mfg_year', F.split(F.col("mfg_date"),"/").getItem(1))
            .withColumn('mfg_year',regexp_replace('mfg_year',"[^0-9|.]",''))
            .drop('mfg_date')
            .withColumn('max_speed',regexp_replace('max_speed',"[^0-9|.]",''))
            .withColumn('mileage_kmpl',regexp_replace('mileage',"[^0-9|.]",''))
            .drop('mileage')
            .drop('mileage_city')
            .drop('mileage_highway')
            .withColumn('minimum_turning_radius_in_m',regexp_replace('minimum_turning_radius',"[^0-9|.]",''))
            .withColumn('no_of_cylinder',regexp_replace('no_of_cylinder',"[^0-9|.]",''))
            .withColumn('no_of_doors',regexp_replace('no_of_doors',"[^0-9|.]",''))
            .drop('minimum_turning_radius')
            .drop('performance_0_to_100_kmph')
            .withColumn("power_in_bhp",F.split(col("power"),"@").getItem(0))
            .withColumn('power_in_bhp', regexp_replace('power_in_bhp',"[^0-9|.]",''))
            .withColumn("power_at_rpm",F.split(col("power"),"@").getItem(1))
            .withColumn('power_at_rpm', regexp_replace('power_at_rpm',"[^0-9|.]",''))
            .drop('power')
            .withColumn('rear_track_in_mm',regexp_replace('rear_track',"[^0-9|.]",''))
            .drop('rear_track')
            .withColumn('seating_capacity', regexp_replace('seating_capacity',"[^0-9|.]",''))
            .withColumn('rear_tyre_size', F.split(F.col("rear_tyre_size"),"/").getItem(0))
            .withColumn('tyresize_width_in_mm', regexp_replace('rear_tyre_size',"[^0-9]",''))
            .drop('rear_tyre_size')
            
            .withColumn("torque_in_nm",F.split(col("torque"),"@").getItem(0))
            .withColumn('torque_in_nm', regexp_replace('torque_in_nm',"[^0-9|.]",''))
            .withColumn("torque_at_rpm",F.split(col("torque"),"@").getItem(1))
            .withColumn("torque_at_rpm",F.split(col("torque_at_rpm"),"-").getItem(0))
            .withColumn('torque_at_rpm', regexp_replace('torque_at_rpm',"[^0-9|.]",''))
            .drop("torque")
            
            .withColumn('wheelbase_in_mm',regexp_replace('wheelbase',"[^0-9]",''))
            .drop('wheelbase')
            .withColumn('width_in_mm',regexp_replace('width',"[^0-9]",''))
            .withColumn('width_in_mm',regexp_replace('width_in_mm',"N/A",''))
            .drop('width')
            
    )
df2 = df1.where(F.col("brand_price_in").isNotNull())    
df2 = df2.filter(df1.brand_name != "2016 Mahindra NuvoSport N8 AMT")
df2 = df2.filter(df1.front_tire_width_size != "7.001538.110")
df2.coalesce(1).write.save("s3://amantya-adlp-silver/autondtv_usedcar11/", format='csv', header=True)

##selectfields2 = SelectFields.apply(frame = applymapping1, paths = ["adjustable_power_steering", "boot_space", "brand_name", "brand_price", "clutch_type", "damage", "displacement_cc", "drive_train", "emission", "emission_standard", "emission_type", "engine_cc", "engine_type", "front_brake_type", "front_suspension", "front_track", "front_tyre_size", "fuel", "fuel_tank_capacity", "gearbox", "gross_weight", "ground_clearance", "height", "kms_run", "kerb_weight", "length", "mfg_date", "max_speed", "mileage", "mileage_city", "mileage_highway", "minimum_turning_radius", "no_of_cylinder", "no_of_doors", "no_of_gears", "owner_count", "performance_0_to_100_kmph", "place", "power", "power_steering", "rear_brake_type", "rear_suspension", "rear_track", "rear_tyre_size", "seating_capacity", "steering_type", "torque", "tyre_type", "wheel_type", "wheelbase", "width"], transformation_ctx = "selectfields2")
## @type: ResolveChoice
## @args: [choice = "MATCH_CATALOG", database = "amantya-bronze-db", table_name = "autondtv_usedcar", transformation_ctx = "resolvechoice3"]
## @return: resolvechoice3
## @inputs: [frame = selectfields2]
##resolvechoice3 = ResolveChoice.apply(frame = selectfields2, choice = "MATCH_CATALOG", database = "amantya-bronze-db", table_name = "autondtv_usedcar", transformation_ctx = "resolvechoice3")
## @type: DataSink
## @args: [database = "amantya-bronze-db", table_name = "autondtv_usedcar", transformation_ctx = "datasink4"]
##@return: datasink4
## @inputs: [frame = resolvechoice3]
##datasink4 = glueContext.write_dynamic_frame.from_catalog(frame = resolvechoice3, database = "amantya-bronze-db", table_name = "autondtv_usedcar", transformation_ctx = "datasink4")
job.commit()