# Package ID: knb-lter-jrn.210461001.17 Cataloging System:https://pasta.edirepository.org.
# Data set title: Perennial grass recovery following livestock overgazing and shrub removal: an experiment at the Jornada Experimental Range (Jornada Basin LTER), 1996-2016.
# Data set creator:  Kris Havstad - USDA ARS Jornada Experimental Range (JER) 
# Data set creator:  Brandon Bestelmeyer - USDA ARS Jornada Experimental Range (JER) 
# Contact:  Data Manager -  Jornada Basin LTER  - datamanager.jrn.lter@gmail.comÂ 
# Stylesheet v1.0 for metadata conversion into program: John H. Porter, Univ. Virginia, jporter@virginia.edu      
# 
# This program creates numbered PANDA dataframes named dt1,dt2,dt3...,
# one for each data table in the dataset. It also provides some basic
# summaries of their contents. NumPy and Pandas modules need to be installed
# for the program to run. 

import numpy as np
import pandas as pd 

infile1  ="https://pasta.lternet.edu/package/data/eml/knb-lter-jrn/210461001/17/12137791f6cade12e21e48dfcb8c55d9".strip() 
infile1  = infile1.replace("https://","http://")
                 
dt1 =pd.read_csv(infile1 
          ,skiprows=1
            ,sep=","  
           , names=[
                    "year",     
                    "date",     
                    "exclosure",     
                    "block",     
                    "shrub_treatment",     
                    "grazing_treatment",     
                    "line",     
                    "point",     
                    "layer",     
                    "USDA_code",     
                    "live_dead",     
                    "scientific_name",     
                    "common_name",     
                    "habit",     
                    "form"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'year':'str' , 
#             'date':'str' ,  
#             'exclosure':'str' ,  
#             'block':'str' ,  
#             'shrub_treatment':'str' ,  
#             'grazing_treatment':'str' , 
#             'line':'int' , 
#             'point':'int' ,  
#             'layer':'str' ,  
#             'USDA_code':'str' ,  
#             'live_dead':'str' ,  
#             'scientific_name':'str' ,  
#             'common_name':'str' ,  
#             'habit':'str' ,  
#             'form':'str'  
#        }
          ,parse_dates=[
                        'year',
                        'date',
                ] 
            ,na_values={
                  'date':[
                          '.',],
                  'live_dead':[
                          '.',],
                  'scientific_name':[
                          '.',],
                  'habit':[
                          '.',],
                  'form':[
                          '.',],} 
            
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt1=dt1.assign(year_datetime=pd.to_datetime(dt1.year,errors='coerce')) 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt1=dt1.assign(date_datetime=pd.to_datetime(dt1.date,errors='coerce'))  
dt1.exclosure=dt1.exclosure.astype('category')  
dt1.block=dt1.block.astype('category')  
dt1.shrub_treatment=dt1.shrub_treatment.astype('category')  
dt1.grazing_treatment=dt1.grazing_treatment.astype('category') 
dt1.line=pd.to_numeric(dt1.line,errors='coerce',downcast='integer') 
dt1.point=pd.to_numeric(dt1.point,errors='coerce',downcast='integer')  
dt1.layer=dt1.layer.astype('category')  
dt1.USDA_code=dt1.USDA_code.astype('category')  
dt1.live_dead=dt1.live_dead.astype('category')  
dt1.scientific_name=dt1.scientific_name.astype('category')  
dt1.common_name=dt1.common_name.astype('category')  
dt1.habit=dt1.habit.astype('category')  
dt1.form=dt1.form.astype('category') 
      
print("Here is a description of the data frame dt1 and number of lines\n")
print(dt1.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt1\n")
print(dt1.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt1.year.describe())               
print("--------------------\n\n")
                    
print(dt1.date.describe())               
print("--------------------\n\n")
                    
print(dt1.exclosure.describe())               
print("--------------------\n\n")
                    
print(dt1.block.describe())               
print("--------------------\n\n")
                    
print(dt1.shrub_treatment.describe())               
print("--------------------\n\n")
                    
print(dt1.grazing_treatment.describe())               
print("--------------------\n\n")
                    
print(dt1.line.describe())               
print("--------------------\n\n")
                    
print(dt1.point.describe())               
print("--------------------\n\n")
                    
print(dt1.layer.describe())               
print("--------------------\n\n")
                    
print(dt1.USDA_code.describe())               
print("--------------------\n\n")
                    
print(dt1.live_dead.describe())               
print("--------------------\n\n")
                    
print(dt1.scientific_name.describe())               
print("--------------------\n\n")
                    
print(dt1.common_name.describe())               
print("--------------------\n\n")
                    
print(dt1.habit.describe())               
print("--------------------\n\n")
                    
print(dt1.form.describe())               
print("--------------------\n\n")
                    
                    
                




