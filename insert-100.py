# First intall the library i will use which is pandas
import pandas as pd

# The clean.csv file will be in a dataframe called My_csv_file and the output will be in the insert-100.sql
My_csv_file = 'clean.csv'
Sql_output = 'insert-100.sql'

# The csv_columns is the columns to read in from the clean.csv file and its data types
csv_columns = ['Date Time', 'NOx', 'NO2', 'NO', 'SiteID', 'PM10', 'NVPM10', 'VPM10', 'NVPM2.5', 'PM2.5', 'VPM2.5', 'CO', 'O3', 'SO2', 'Temperature', 'RH', 'Air Pressure', 'Location', 'geo_point_2d', 'DateStart', 'DateEnd', 'Current', 'Instrument Type']
data_types = {'Date Time': 'str', 'NOx': 'float', 'NO2': 'float', 'NO': 'float', 'SiteID': 'int', 'PM10': 'float', 'NVPM10': 'float', 'VPM10': 'float', 'NVPM2.5': 'float', 'PM2.5': 'float', 'VPM2.5': 'float', 'CO': 'float', 'O3': 'float', 'SO2': 'float', 'Temperature': 'float', 'RH': 'float', 'Air Pressure': 'float', 'Location': 'str', 'geo_point_2d': 'str', 'DateStart': 'str', 'DateEnd': 'str', 'Current': 'int', 'Instrument Type': 'str'}

# I set the number of values to read in to 100 into a dataframe i call insert_100
insert_100 = 100

# then i Read the CSV file into DMF_data dataframe with specifing the column, datatyoe and the number of rows
DMF_data = pd.read_csv(My_csv_file, usecols=csv_columns, dtype=data_types, nrows=insert_100)

#i Converted the  'Date Time' column to datetime data type
DMF_data['Date Time'] = pd.to_datetime(DMF_data['Date Time'])

# To generate SQL insert statements, i use for loop to iterate over the rows in the DMF_data DataFrame, convert it to a list of values. 
# then the first value which is Date time is converted to string, then iterrate over each row, check for missing
#values and convert them to null then concatenate all the values into a string using a comma as separator
#and append append it to sql variable which will contain the insert-100 for all the dataframe.
sql = ''
for index, row in DMF_data.iterrows():
    val = row.tolist()
    val[0] = val[0].strftime('%Y-%m-%d %H:%M:%S') 
    for i in range(len(val)):
        if pd.isna(val[i]):
            val[i] = "NULL"
        elif isinstance(val[i], str):
            val[i] = "'" + val[i].replace("'", "''") + "'"
    sql += "({0});\n".format(','.join(str(v) for v in val))

# Finally write SQL insert statements to file
with open(Sql_output, 'w') as f:
    f.write(sql)