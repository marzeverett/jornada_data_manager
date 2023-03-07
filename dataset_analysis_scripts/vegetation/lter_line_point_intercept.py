# Package ID: knb-lter-jrn.210119001.128 Cataloging System:https://pasta.edirepository.org.
# Data set title: Percent cover of vegetation measured by the line-intercept method at multiple locations on long-term ecosystem transects (including nitrogen fertilization treatments) at Jornada Basin LTER, 1982-2014.
# Data set creator:  Gary Cunningham - New Mexico State University, Biology 
# Contact:  Data Manager -  Jornada Basin LTER  - datamanager.jrn.lter@gmail.com
# Contact:  John Anderson -  Jornada Basin LTER  - janderso@jornada.nmsu.edu
# Stylesheet v1.0 for metadata conversion into program: John H. Porter, Univ. Virginia, jporter@virginia.edu      
# 
# This program creates numbered PANDA dataframes named dt1,dt2,dt3...,
# one for each data table in the dataset. It also provides some basic
# summaries of their contents. NumPy and Pandas modules need to be installed
# for the program to run. 

import numpy as np
import pandas as pd 

infile1  ="https://pasta.lternet.edu/package/data/eml/knb-lter-jrn/210119001/128/b6fa09dde8d65a280d7bf1631a252ac2".strip() 
infile1  = infile1.replace("https://","http://")
                 
dt1 =pd.read_csv(infile1 
          ,skiprows=1
            ,sep=","  
           , names=[
                    "date",     
                    "week",     
                    "transect",     
                    "station",     
                    "species_code",     
                    "USDA_code",     
                    "Species_binomial",     
                    "habit",     
                    "form",     
                    "cpath",     
                    "cover_percent"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'date':'str' , 
#             'week':'int' ,  
#             'transect':'str' ,  
#             'station':'str' ,  
#             'species_code':'str' ,  
#             'USDA_code':'str' ,  
#             'Species_binomial':'str' ,  
#             'habit':'str' ,  
#             'form':'str' ,  
#             'cpath':'str' , 
#             'cover_percent':'float'  
#        }
          ,parse_dates=[
                        'date',
                ] 
            ,na_values={
                  'habit':[
                          'NA',],
                  'form':[
                          'NA',],
                  'cpath':[
                          'NA',],
                  'cover_percent':[
                          'NA',],} 
            
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt1=dt1.assign(date_datetime=pd.to_datetime(dt1.date,errors='coerce')) 
dt1.week=pd.to_numeric(dt1.week,errors='coerce',downcast='integer')  
dt1.transect=dt1.transect.astype('category')  
dt1.station=dt1.station.astype('category')  
dt1.species_code=dt1.species_code.astype('category')  
dt1.USDA_code=dt1.USDA_code.astype('category')  
dt1.Species_binomial=dt1.Species_binomial.astype('category')  
dt1.habit=dt1.habit.astype('category')  
dt1.form=dt1.form.astype('category')  
dt1.cpath=dt1.cpath.astype('category') 
dt1.cover_percent=pd.to_numeric(dt1.cover_percent,errors='coerce') 
      
print("Here is a description of the data frame dt1 and number of lines\n")
print(dt1.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt1\n")
print(dt1.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt1.date.describe())               
print("--------------------\n\n")
                    
print(dt1.week.describe())               
print("--------------------\n\n")
                    
print(dt1.transect.describe())               
print("--------------------\n\n")
                    
print(dt1.station.describe())               
print("--------------------\n\n")
                    
print(dt1.species_code.describe())               
print("--------------------\n\n")
                    
print(dt1.USDA_code.describe())               
print("--------------------\n\n")
                    
print(dt1.Species_binomial.describe())               
print("--------------------\n\n")
                    
print(dt1.habit.describe())               
print("--------------------\n\n")
                    
print(dt1.form.describe())               
print("--------------------\n\n")
                    
print(dt1.cpath.describe())               
print("--------------------\n\n")
                    
print(dt1.cover_percent.describe())               
print("--------------------\n\n")
                    
                    