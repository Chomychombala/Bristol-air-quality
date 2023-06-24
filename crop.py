#import the libraries we will use like pandas, datetime and pytz

import pandas as pd
from datetime import datetime
import pytz
import time


# read the CSV file using pandas into a data frame i call DMF_data by specifying the delimiter used 
#and setting the low_memory to False thereby telling pandas not to try to automatically detect 
# the data type of each column as i wish to save memory
DMF_data = pd.read_csv("air-quality-data-2003-2022.csv", delimiter=';', low_memory=False)

# here i first filter out rows with non-date values
DMF_data = DMF_data[DMF_data['Date Time'].notna()]

# then i convert timestamp string to datetime object

DMF_data['Date Time'] = pd.to_datetime(DMF_data['Date Time'], utc=True)

# since i want to cutoff the dates before 00:00 1 Jan 2010, i set cutoff date
cutoff_date = datetime(2010, 1, 1,)
cutoff_date = pytz.utc.localize(cutoff_date)

# then i filter the dataframe based on the cutoff date by using the localize method 
# from the pytz module to add timezone information to the cutoff_date object. 
# Specifically, it sets the timezone of cutoff_date 
# to Coordinated Universal Time (UTC) by calling the utc method of the pytz module.
DMF_data = DMF_data[DMF_data['Date Time'] >= cutoff_date]

# i Print length then of the filtered dataframe just to be sure that the filtering worked before saving it on my crop.csv folder
print(len(DMF_data))

#Finally i use the to_csv function to save my cropped dataframe to a new folder called crop.csv.  
# I set the index parameter to "False" to exclude row indexes from the exported data.
DMF_data.to_csv("crop.csv", index = False)
