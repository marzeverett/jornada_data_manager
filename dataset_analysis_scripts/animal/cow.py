# Package ID: knb-lter-jrn.200022001.3 Cataloging System:https://pasta.edirepository.org.
# Data set title: Criollo and Crossbred Steer Comparison: Weight Gain, Grazing, Carcass Quality, 2015-2017.
# Data set creator:  Matt M McIntosh - New Mexico State University 
# Data set creator:  Andres F Cibils - New Mexico State University 
# Data set creator:  Rick E Estell - USDA-ARS Jornada Experimental Range 
# Data set creator:  Shelemia Nyamuryekung'e - New Mexico State University 
# Data set creator:  Sheri Spiegal - USDA-ARS Jornada Experimental Range 
# Data set creator:  Alfredo L Gonzalez - USDA-ARS Jornada Experimental Range 
# Data set creator:  Amanda D Blair - South Dakota State University 
# Metadata Provider:    - Jornada Experimental Range LTAR (USDA-ARS) 
# Contact:    - Jornada Information Manager USDA-ARS Jornada Experimental Range  - jornada.data@nmsu.edu
# Stylesheet v1.0 for metadata conversion into program: John H. Porter, Univ. Virginia, jporter@virginia.edu      
# 
# This program creates numbered PANDA dataframes named dt1,dt2,dt3...,
# one for each data table in the dataset. It also provides some basic
# summaries of their contents. NumPy and Pandas modules need to be installed
# for the program to run. 

import numpy as np
import pandas as pd 

infile1  ="https://pasta.lternet.edu/package/data/eml/knb-lter-jrn/200022001/3/07bee70ba845ff53782af5a5753d491a".strip() 
infile1  = infile1.replace("https://","http://")
                 
dt1 =pd.read_csv(infile1 
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "cohort",     
                    "season",     
                    "cow_id",     
                    "date",     
                    "time",     
                    "northing",     
                    "easting"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={  
#             'cohort':'str' ,  
#             'season':'str' ,  
#             'cow_id':'str' , 
#             'date':'str' , 
#             'time':'str' , 
#             'northing':'float' , 
#             'easting':'float'  
#        }
          ,parse_dates=[
                        'date',
                        'time',
                ] 
    )
# Coerce the data into the types specified in the metadata  
dt1.cohort=dt1.cohort.astype('category')  
dt1.season=dt1.season.astype('category')  
dt1.cow_id=dt1.cow_id.astype('category') 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt1=dt1.assign(date_datetime=pd.to_datetime(dt1.date,errors='coerce')) 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt1=dt1.assign(time_datetime=pd.to_datetime(dt1.time,errors='coerce')) 
dt1.northing=pd.to_numeric(dt1.northing,errors='coerce') 
dt1.easting=pd.to_numeric(dt1.easting,errors='coerce') 
      
print("Here is a description of the data frame dt1 and number of lines\n")
print(dt1.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt1\n")
print(dt1.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt1.cohort.describe())               
print("--------------------\n\n")
                    
print(dt1.season.describe())               
print("--------------------\n\n")
                    
print(dt1.cow_id.describe())               
print("--------------------\n\n")
                    
print(dt1.date.describe())               
print("--------------------\n\n")
                    
print(dt1.time.describe())               
print("--------------------\n\n")
                    
print(dt1.northing.describe())               
print("--------------------\n\n")
                    
print(dt1.easting.describe())               
print("--------------------\n\n")
                    
                    
                 

infile2  ="https://pasta.lternet.edu/package/data/eml/knb-lter-jrn/200022001/3/a5014e32227c60d5197c03344be1c06a".strip() 
infile2  = infile2.replace("https://","http://")
                 
dt2 =pd.read_csv(infile2 
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "date",     
                    "breed",     
                    "cohort",     
                    "cow_id",     
                    "weight"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'date':'str' ,  
#             'breed':'str' ,  
#             'cohort':'str' ,  
#             'cow_id':'str' , 
#             'weight':'float'  
#        }
          ,parse_dates=[
                        'date',
                ] 
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt2=dt2.assign(date_datetime=pd.to_datetime(dt2.date,errors='coerce'))  
dt2.breed=dt2.breed.astype('category')  
dt2.cohort=dt2.cohort.astype('category')  
dt2.cow_id=dt2.cow_id.astype('category') 
dt2.weight=pd.to_numeric(dt2.weight,errors='coerce') 
      
print("Here is a description of the data frame dt2 and number of lines\n")
print(dt2.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt2\n")
print(dt2.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt2.date.describe())               
print("--------------------\n\n")
                    
print(dt2.breed.describe())               
print("--------------------\n\n")
                    
print(dt2.cohort.describe())               
print("--------------------\n\n")
                    
print(dt2.cow_id.describe())               
print("--------------------\n\n")
                    
print(dt2.weight.describe())               
print("--------------------\n\n")
                    
                    
                




