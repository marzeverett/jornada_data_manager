# Package ID: knb-lter-jrn.210351001.49 Cataloging System:https://pasta.edirepository.org.
# Data set title: Plant Cover at Permanent Quad Locations on the Jornada Experimental Range, 1915-ongoing.
# Data set creator:  William Chapline - U.S. Forest Service 
# Data set creator:  Kris Havstad - USDA-ARS Jornada Experimental Range 
# Data set creator:  Brandon Bestelmeyer - USDA-ARS Jornada Experimental Range 
# Contact:  Data Manager -  Jornada Basin LTER  - datamanager.jrn.lter@gmail.com
# Stylesheet v1.0 for metadata conversion into program: John H. Porter, Univ. Virginia, jporter@virginia.edu      
# 
# This program creates numbered PANDA dataframes named dt1,dt2,dt3...,
# one for each data table in the dataset. It also provides some basic
# summaries of their contents. NumPy and Pandas modules need to be installed
# for the program to run. 

import numpy as np
import pandas as pd 

infile1  ="https://pasta.lternet.edu/package/data/eml/knb-lter-jrn/210351001/49/c93e2a3a593d660fba6e4d7295544638".strip() 
infile1  = infile1.replace("https://","http://")
                 
dt1 =pd.read_csv(infile1 
          ,skiprows=1
            ,sep=","  
           , names=[
                    "quadrat",     
                    "year",     
                    "month",     
                    "day",     
                    "project_year",     
                    "USDA_code",     
                    "scientific_name",     
                    "duration",     
                    "form",     
                    "area",     
                    "perimeter",     
                    "cover_status",     
                    "chart_status"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={  
#             'quadrat':'str' , 
#             'year':'str' , 
#             'month':'str' , 
#             'day':'str' , 
#             'project_year':'str' ,  
#             'USDA_code':'str' ,  
#             'scientific_name':'str' ,  
#             'duration':'str' ,  
#             'form':'str' , 
#             'area':'float' , 
#             'perimeter':'float' ,  
#             'cover_status':'str' ,  
#             'chart_status':'str'  
#        }
          ,parse_dates=[
                        'year',
                        'month',
                        'day',
                        'project_year',
                ] 
            ,na_values={
                  'month':[
                          '.',],
                  'day':[
                          '.',],
                  'USDA_code':[
                          '.',],
                  'scientific_name':[
                          '.',],
                  'duration':[
                          '.',],
                  'form':[
                          '.',],
                  'area':[
                          '.',],
                  'perimeter':[
                          '.',],} 
            
    )
# Coerce the data into the types specified in the metadata  
dt1.quadrat=dt1.quadrat.astype('category') 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt1=dt1.assign(year_datetime=pd.to_datetime(dt1.year,errors='coerce')) 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt1=dt1.assign(month_datetime=pd.to_datetime(dt1.month,errors='coerce')) 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt1=dt1.assign(day_datetime=pd.to_datetime(dt1.day,errors='coerce')) 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt1=dt1.assign(project_year_datetime=pd.to_datetime(dt1.project_year,errors='coerce'))  
dt1.USDA_code=dt1.USDA_code.astype('category')  
dt1.scientific_name=dt1.scientific_name.astype('category')  
dt1.duration=dt1.duration.astype('category')  
dt1.form=dt1.form.astype('category') 
dt1.area=pd.to_numeric(dt1.area,errors='coerce') 
dt1.perimeter=pd.to_numeric(dt1.perimeter,errors='coerce')  
dt1.cover_status=dt1.cover_status.astype('category')  
dt1.chart_status=dt1.chart_status.astype('category') 
      
print("Here is a description of the data frame dt1 and number of lines\n")
print(dt1.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt1\n")
print(dt1.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt1.quadrat.describe())               
print("--------------------\n\n")
                    
print(dt1.year.describe())               
print("--------------------\n\n")
                    
print(dt1.month.describe())               
print("--------------------\n\n")
                    
print(dt1.day.describe())               
print("--------------------\n\n")
                    
print(dt1.project_year.describe())               
print("--------------------\n\n")
                    
print(dt1.USDA_code.describe())               
print("--------------------\n\n")
                    
print(dt1.scientific_name.describe())               
print("--------------------\n\n")
                    
print(dt1.duration.describe())               
print("--------------------\n\n")
                    
print(dt1.form.describe())               
print("--------------------\n\n")
                    
print(dt1.area.describe())               
print("--------------------\n\n")
                    
print(dt1.perimeter.describe())               
print("--------------------\n\n")
                    
print(dt1.cover_status.describe())               
print("--------------------\n\n")
                    
print(dt1.chart_status.describe())               
print("--------------------\n\n")
                    
                    
                




