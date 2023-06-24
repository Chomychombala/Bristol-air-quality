import pandas as pd
from sqlalchemy import create_engine
import numpy as np


#first create a connection to a MySQL database using Python and the SQLAlchemy library which will use the create_engine function from SQLAlchemy
#to create an engine object that will allow Python to interact with the MySQL database
engine = create_engine("mysql+pymysql://{user}:{passwd}@localhost"
                       .format(user="root",
                               passwd=""))

#then i create a new database called "pollution-db2" using the execute method of the engine object
engine.execute("CREATE DATABASE `pollution-db2`;")

#then i create a SQLAlchemy engine object will connect to the MySQL database "pollution-db2" 
#using the create_engine function.
engine = create_engine("mysql+pymysql://{user}:{passwd}@localhost/{db}"
                       .format(user="root",
                               passwd="",
                               db="pollution-db2"))

#then i proceed to creating the station's table
create_station_table = """
                CREATE TABLE stations (
                `SiteID` VARCHAR(255) PRIMARY KEY,
                `geo_point_2d` VARCHAR(255),
                `Location` VARCHAR(255)
                );
                """
                
#and the readings's table
create_reading_table = """
                CREATE TABLE readings (
                `Date Time` DATETIME,
                `SiteID` VARCHAR(255),
                `NOx` FLOAT,
                `NO2` FLOAT,
                `NO` FLOAT,
                `PM10` FLOAT,
                `NVPM10` FLOAT,
                `VPM10` FLOAT,
                `NVPM2.5` FLOAT,
                `PM2.5` FLOAT,
                `VPM2.5` FLOAT,
                `CO` FLOAT,
                `O3` FLOAT,
                `SO2` FLOAT,
                `Temperature` FLOAT,
                `RH` FLOAT,
                `Air Pressure` FLOAT,
                `Instrument Type` VARCHAR(255),
                `DateStart` DATETIME, 
                `DateEnd` DATETIME,
                `Current` VARCHAR(255),

                FOREIGN KEY (`SiteID`) REFERENCES `station`(`SiteID`)
                );
                """

#then i create a connection to the MySQL database using the engine object and the connect() method.
# to execute a SQL query called
# create_station_table on that database using the execute() method of the connection object.
with engine.connect() as conn:
    conn.execute(create_station_table)

#the same method above is done here but this time for readings
with engine.connect() as conn:
    conn.execute(create_reading_table)

#then i read in the clean.csv file setting the low_memory to False into a variable used mydata
mydata = pd.read_csv('clean.csv', low_memory=False)

#then i specified the columns i need in the readings column
readings_column = ['Date Time', 'NOx', 'NO2', 'NO', 'SiteID', 'PM10', 'NVPM10', 'VPM10',
           'NVPM2.5', 'PM2.5', 'VPM2.5', 'CO', 'O3', 'SO2', 'Temperature', 'RH',
           'Air Pressure','DateStart', 'DateEnd', 'Current', 'Instrument Type']

#same with stations table
stations_column = ['SiteID', 'Location', 'geo_point_2d']

#then i print the number of missing (NaN) values in each column of  mydata
print(mydata.isna().sum())

mydata = mydata.replace({np.nan: None})

#the i create a new variables readings 
readings = mydata[readings_column]

#selects all columns in the readings Series object that have numeric data types using the select_dtypes() method
numeric_columns = readings.select_dtypes(include=['number']).columns
readings[numeric_columns] = readings[numeric_columns].fillna(None)

stations= mydata[stations_column]

#the will remove duplicates from the station table
stations.drop_duplicates(subset='SiteID',inplace=True)

#populate values to  stations table using to_sql method 
stations.to_sql('stations',index=False, con = engine, if_exists = 'append', chunksize = 1000)
print("station's data populated")

#populate values to  readings table using to_sql method
readings.to_sql('readings',index=False, con = engine, if_exists = 'append', chunksize = 10000)
print("reading's data populated")
