                                   Air Quality Data Analysis and Database Integration
Project Overview
This project involved preparing, cleaning, validating and storing air-quality monitoring data using Python, Pandas, MySQL and MongoDB.
The project started with a raw air-quality dataset covering monitoring stations and environmental measurements from 2003 to 2022. I prepared the data for analysis by filtering the required period, checking data quality, validating monitoring station information and removing inconsistent records.
I then transformed the cleaned dataset for database storage and implemented it in both a relational MySQL database and a NoSQL MongoDB database.
The project demonstrates a practical data analyst workflow from raw data through to structured, analysis-ready data.

Project Objective
The main objective was to prepare a reliable dataset that could support air-quality analysis and reporting.
The project focused on:
Understanding the structure of the raw dataset.
Preparing the data for analysis.
Filtering the dataset to the required time period.
Identifying and handling data-quality issues.
Validating monitoring station information.
Removing inconsistent records.
Preparing data for SQL database storage.
Loading the processed data into MySQL.
Exploring NoSQL storage using MongoDB.
Creating a structured dataset suitable for further analysis.

Dataset
The dataset contains air-quality measurements collected from monitoring stations.
The main variables include:
Date and time of measurement
Monitoring station ID
Monitoring station location
Geographic coordinates
Nitrogen oxides (NOx)
Nitrogen dioxide (NO₂)
Nitric oxide (NO)
PM10
PM2.5
Carbon monoxide (CO)
Ozone (O₃)
Sulphur dioxide (SO₂)
Temperature
Relative humidity
Air pressure
Monitoring period
Current station status
Instrument type
The original dataset covered 2003–2022. For this project, the data was filtered to records from 1 January 2010 onwards.

Data Analyst Workflow
The project followed these stages:
1. Data Understanding
Understand the dataset structure, variables and time period.
2. Data Cleaning
Remove records that could not be used reliably for analysis.
3. Data Validation
Check the consistency of monitoring station IDs and locations.
4. Data Transformation
Prepare fields and data types for database storage.
5. Database Integration
Store the processed data in MySQL and MongoDB.
6. Analysis Readiness
Produce structured data that can be used for further exploratory analysis and reporting.

Data Understanding
The raw CSV dataset was imported into Python using Pandas.
The dataset was reviewed to understand the available fields and identify the information required for further processing.
The Date Time field was converted into a datetime format so that the records could be filtered accurately by date.
Records without a valid timestamp were removed because a valid timestamp is required for time-based air-quality analysis.

Data Cleaning
The project focused on preparing the raw data for reliable use.
Date filtering
The dataset contained records from 2003 onwards. The analysis dataset was restricted to records from 1 January 2010 onwards.
This created a filtered dataset called:
crop.csv
Missing values
Missing values were reviewed across the dataset.
Rather than automatically removing every record containing a missing measurement, missing values were retained where the record could still be useful for analysis.
This distinction is important because removing too many records can reduce the amount of usable data.

Data Quality Validation
A key quality check focused on the relationship between SiteID and Location.
Each monitoring station ID was compared against its expected location.
For example:
SiteID 501 → Colston Avenue
SiteID 500 → Temple Way
SiteID 481 → CREATE Centre Roof
SiteID 463 → Fishponds Road
Records where the station ID did not correspond to the expected location were identified as inconsistent.
These inconsistent records were removed from the working dataset.
The resulting dataset was saved as:
clean.csv

Data Transformation
The cleaned dataset was prepared for database integration.
The transformation process included:
Selecting the required columns.
Defining suitable data types.
Converting date fields into appropriate datetime formats.
Reviewing missing values.
Removing duplicate station records.
Preparing missing values for database storage.
Converting a sample of records into SQL-compatible statements.
A sample of 100 records was also converted into SQL INSERT statements and saved as:
insert-100.sql

MySQL Database Implementation
The cleaned data was stored in a MySQL relational database.
The database was structured into two tables:
Stations
The station table contains information about monitoring locations:
Site ID
Location
Geographic coordinates
Readings
The readings table contains the air-quality measurements associated with each monitoring station.
The relationship between the tables is based on SiteID.
This structure separates monitoring station information from the repeated measurement records and provides a suitable foundation for querying the data.

Python and MySQL Integration
Python was used to connect to MySQL through SQLAlchemy.
The cleaned dataset was loaded into Pandas, separated into station and reading datasets, and then inserted into the corresponding MySQL tables.
Duplicate station IDs were removed before loading the station data.
The reading data was inserted in batches to support the loading of a larger dataset.
This demonstrated the use of Python as part of a data pipeline between a CSV dataset and a relational database.

MongoDB Implementation
MongoDB was used to demonstrate an alternative approach to storing the air-quality information.
Instead of using relational tables, the data was represented using JSON-like documents.
Python was connected to MongoDB using PyMongo.
A MongoDB database called pollution1DB and a collection called readings were created.
For this implementation, data for SiteID 501 — Colston Avenue was selected.
The document contained:
Station information
Location
Geographic coordinates
Associated air-quality readings
The resulting MongoDB data was exported into JSON for review.

Relational vs NoSQL Approach
The project provided an opportunity to work with two different database models.
MySQL	MongoDB
Relational database	NoSQL database
Data stored in tables	Data stored in documents
Stations and readings stored separately	Station information and readings stored together
Uses relationships between tables	Supports embedded document structures
SQL used for database operations	JSON-like document structure
Using both approaches helped demonstrate how the same source data can be structured differently depending on the database requirements.

Data Quality Issues Addressed
The project addressed several data-quality considerations:
Missing timestamps
Records without valid timestamps were removed.
Date range
Records before 1 January 2010 were excluded from the working dataset.
Site and location inconsistencies
Monitoring station IDs were checked against their expected locations.
Duplicate stations
Duplicate station IDs were removed before populating the station table.
Missing measurements
Missing values were identified and considered during the preparation process rather than treating every missing value as an invalid record.
Data type consistency
Fields were assigned appropriate data types before database loading.

 Project Outcomes
The project produced several outputs:
crop.csv — filtered dataset from 2010 onwards.
clean.csv — validated and cleaned dataset.
insert-100.sql — SQL insert statements generated from a sample of the cleaned data.
MySQL database — structured station and reading tables.
MongoDB collection — document-based representation of selected station data.
JSON output — exported MongoDB document.


Conclusion
This project demonstrates a complete data preparation and database integration workflow using Python, Pandas, MySQL and MongoDB.
I started with raw air-quality data and applied date filtering, data-quality checks and station validation before producing a cleaned dataset.
The processed data was then prepared for relational database storage in MySQL and represented as document-based data in MongoDB.
The project demonstrates practical Data Analyst skills in data cleaning, validation, transformation, database integration and preparing data for further analysis.
The resulting dataset can support future analysis of pollution trends, monitoring station performance, pollutant levels and environmental factors.
