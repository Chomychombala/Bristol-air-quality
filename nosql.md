Nosql database do not use the relational data modelling technique. It literally do not require any structure neither does 
it have any need for schema and this makes designing simple and easy. 

MongoDB is one example of nosql database. It stores data in flexible, JSON-like documents, meaning fields can vary from document to document and data structure can be changed over time. It is designed to be horizontally scalable meaning that it can handle large amount of data and traffic by simply distributing its workload across different users. This database can create copies of data across multiple servers and also provides high availablity. 

MongoDB was downloaded and installed from www.mongodb.com. Then i used PIP3 to install PyMongo, and afterwards launched mongoDB compass and established a connection to the server on localhost: 27017.
Using Python environment, i imported pymongo, and proceeded to make a connection to the localhost ip address. I created mongoobject Client which i called mydmfclient,  database called pollutionDB1 and collection called readings.

import pymongo
import pandas as pd

try:
    ## To create a MongoClient object and connect to a MongoDB database
    mydmfclient = pymongo.MongoClient("mongodb://localhost:27017/")
    database_name = "pollution1DB"
    db_names = mydmfclient.list_database_names()

    if database_name in db_names:
        mydmfclient.drop_database(database_name)
    
    database = mydmfclient[database_name]
    collection = database['readings']

    station_data = {
        "station_id" : 501,
        "location": "Colston Avenue",
        "geo_point_2d": "51.455269382758324, -2.596648828557916"
    }

    readings = []
    df = pd.read_csv('Data/clean.csv', low_memory=False, sep=",")

    count =0
    for index, row in df.iterrows():
        if count == 1000:
            break
    
        site_id =  row['SiteID']
        if site_id == 501:
            reading_data = {
                "Data Time": "2019-07-02T05:00:00+00:00",
                "Nox" : 36.3258,
                "NO2": 19.9612,
                "NO" : 10.6792,
                "PM10": 11.325,
                "NVPM10": "null",
                "VPM10": "null",    
                "NVPM2.5": "null",
                "PM2.5": "null",
                "VPM2.5": "null",
                "CO": "null",
                "O3": "null",
                "SO2": "null",
                "Temperature": 15.6,
                "RH": "null",   
                "Air Pressure": "null",
                "DateStart": "2018-11-30T00:00:00+00:00",
                "DateEnd": "null",
                "current": "TRUE",
                "Instrument Type": "Continuous (Reference)"
            }

            readings.append(reading_data)
            count +=1
        

    final_object = {
        "staion": station_data,
        "readings": readings
    }

    collection.insert_one(final_object)

except Exception as ex:
    print(f"Error occured: {ex}")


i extracted data for station (colston avenue)
On the mongodb i exported it to a JSON format which  displayed below

[{
  "_id": {
    "$oid": "645b91075d3fbe5cefd8bd27"
  },
  "staion": {
    "station_id": 501,
    "location": "Colston Avenue",
    "geo_point_2d": "51.455269382758324, -2.596648828557916"
  },
  "readings": [
    {
      "Data Time": "2019-07-02T05:00:00+00:00",
      "Nox": 36.3258,
      "NO2": 19.9612,
      "NO": 10.6792,
      "PM10": 11.325,
      "NVPM10": "null",
      "VPM10": "null",
      "NVPM2.5": "null",
      "PM2.5": "null",
      "VPM2.5": "null",
      "CO": "null",
      "O3": "null",
      "SO2": "null",
      "Temperature": 15.6,
      "RH": "null",
      "Air Pressure": "null",
      "DateStart": "2018-11-30T00:00:00+00:00",
      "DateEnd": "null",
      "current": "TRUE",
      "Instrument Type": "Continuous (Reference)"
    },
    {
      "Data Time": "2019-07-02T05:00:00+00:00",
      "Nox": 36.3258,
      "NO2": 19.9612,
      "NO": 10.6792,
      "PM10": 11.325,
      "NVPM10": "null",
      "VPM10": "null",
      "NVPM2.5": "null",
      "PM2.5": "null",
      "VPM2.5": "null",
      "CO": "null",
      "O3": "null",
      "SO2": "null",
      "Temperature": 15.6,
      "RH": "null",
      "Air Pressure": "null",
      "DateStart": "2018-11-30T00:00:00+00:00",
      "DateEnd": "null",
      "current": "TRUE",
      "Instrument Type": "Continuous (Reference)"
    },
    {
      "Data Time": "2019-07-02T05:00:00+00:00",
      "Nox": 36.3258,
      "NO2": 19.9612,
      "NO": 10.6792,
      "PM10": 11.325,
      "NVPM10": "null",
      "VPM10": "null",
      "NVPM2.5": "null",
      "PM2.5": "null",
      "VPM2.5": "null",
      "CO": "null",
      "O3": "null",
      "SO2": "null",
      "Temperature": 15.6,
      "RH": "null",
      "Air Pressure": "null",
      "DateStart": "2018-11-30T00:00:00+00:00",
      "DateEnd": "null",
      "current": "TRUE",
      "Instrument Type": "Continuous (Reference)"
}]

![mongo picture](nosql.png)
![mongo picture](nosql1.png)


