#import the necessary libraries (pandas, numpy, os, re) and display the current working directory using the os.getcwd() command.

import pandas as pd
import numpy as np
import os 
import re

os.getcwd()
#I read the CSV file into a pandas DataFrame called "DMF_data", using the pd.read_csv() function. 
#The parameter low_memory=False is used to ensure that the data types of each column are correctly inferred.
DMF_data = pd.read_csv('crop.csv', low_memory = False)

# I created a new DataFrame called DMF_data1 by selecting only the 'SiteID' and 'Location' columns from the 
# original DataFrame DMF_data.
DMF_data1 = DMF_data.loc[:, ['SiteID', 'Location']]

#A dictionary called "siteID_location" is defined, which maps site IDs to their corresponding locations
siteID_location = {188:'AURN Bristol Centre', 203:'Brislington Depot', 206:'Rupert Street', 209:'IKEA M32', 213:'Old Market', 215:'Parson Street School', 228:'Temple Meads Station', 270:'Wells Road', 271:'Trailer Portway P&R', 375:'Newfoundland Road Police Station', 395:"Shiner's Garage", 452:'AURN St Pauls', 447:'Bath Road', 459:'Cheltenham Road \ Station Road', 463:'Fishponds Road', 481:'CREATE Centre Roof', 500:'Temple Way', 501:'Colston Avenue', 672:'Marlborough Street'}

#The for loop iterates over each row in the DMF_data DataFrame, and checks if the site ID and location in that row match the values in the siteID_location dictionary. 
# If they don't match, a message is printed indicating a mismatch.
for index, row in DMF_data1.iterrows():
    siteID = row['SiteID']
    location = row['Location']
    if siteID in siteID_location and siteID_location[siteID] != location:
        print(f"Mismatch found for SiteID {siteID}. Correct location {siteID_location[siteID]}, got instead {location}. Row: {row}")

#A copy of the DMF_data DataFrame is created using DMF_data_copy = DMF_data.copy()
#Another for loop iterates over each row in the DMF_data_copy DataFrame. For each row, if the site ID and 
# location do not match the values in the siteID_location dictionary, 
# the location value in the DMF_data1 and DMF_data DataFrames are set to 0.
DMF_data_copy = DMF_data.copy()
for index, row in DMF_data_copy.iterrows():
    siteID = row['SiteID']
    location = row['Location']
    if siteID in siteID_location and siteID_location[siteID] != location:
        DMF_data1.at[index, 'Location'] = 0
        DMF_data.loc[index, 'Location'] = 0
#Rows in the DMF_data DataFrame with a location value of 0 are filtered out using 
DMF_data = DMF_data[DMF_data['Location'] != 0]

DMF_data.shape
#Finally, the cleaned DataFrame is saved to a new CSV file called "clean.csv" 
# using the DMF_data.to_csv() command, with the parameter index=False to avoid including 
# the index column in the output file.
DMF_data.to_csv('clean.csv', index=False)
