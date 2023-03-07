# Package ID: knb-lter-jrn.210086006.84 Cataloging System:https://pasta.edirepository.org.
# Data set title: Rabbit survey data on creosotebush and grassland routes from the long-term Small Mammal Exclusion Study at Jornada Basin LTER, 1996-ongoing.
# Data set creator:  Robert Schooley - University of Illinois 
# Data set creator:  Brandon T Bestelmeyer - USDA-ARS Jornada Experimental Range 
# Data set creator:  David C Lightfoot - Jornada Basin LTER (now at Univ. of NM) 
# Metadata Provider:    - Jornada Basin LTER 
# Contact:    - Jornada Basin LTER Information Manager Jornada Basin LTER  - jornada.data@nmsu.edu
# Stylesheet v1.0 for metadata conversion into program: John H. Porter, Univ. Virginia, jporter@virginia.edu      
# 
# This program creates numbered PANDA dataframes named dt1,dt2,dt3...,
# one for each data table in the dataset. It also provides some basic
# summaries of their contents. NumPy and Pandas modules need to be installed
# for the program to run. 

import numpy as np
import pandas as pd 

infile1  ="https://pasta.lternet.edu/package/data/eml/knb-lter-jrn/210086006/84/b41b21340e3513f268f6642b534184b1".strip() 
infile1  = infile1.replace("https://","http://")
                 
dt1 =pd.read_csv(infile1 
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "survey_date",     
                    "date_time_obs",     
                    "route",     
                    "type",     
                    "mileage",     
                    "distance",     
                    "direction",     
                    "qflag1",     
                    "qflag2",     
                    "comment"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'survey_date':'str' , 
#             'date_time_obs':'str' ,  
#             'route':'str' ,  
#             'type':'str' , 
#             'mileage':'float' , 
#             'distance':'float' ,  
#             'direction':'str' ,  
#             'qflag1':'str' ,  
#             'qflag2':'str' ,  
#             'comment':'str'  
#        }
          ,parse_dates=[
                        'survey_date',
                        'date_time_obs',
                ] 
            ,na_values={
                  'survey_date':[
                          'NA',],
                  'date_time_obs':[
                          'NA',],
                  'type':[
                          'NA',],
                  'mileage':[
                          'NA',],
                  'distance':[
                          'NA',],
                  'direction':[
                          'NA',],
                  'qflag2':[
                          'NA',],
                  'comment':[
                          'NA',],} 
            
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt1=dt1.assign(survey_date_datetime=pd.to_datetime(dt1.survey_date,errors='coerce')) 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt1=dt1.assign(date_time_obs_datetime=pd.to_datetime(dt1.date_time_obs,errors='coerce'))  
dt1.route=dt1.route.astype('category')  
dt1.type=dt1.type.astype('category') 
dt1.mileage=pd.to_numeric(dt1.mileage,errors='coerce') 
dt1.distance=pd.to_numeric(dt1.distance,errors='coerce')  
dt1.direction=dt1.direction.astype('category')  
dt1.qflag1=dt1.qflag1.astype('category')  
dt1.qflag2=dt1.qflag2.astype('category')  
dt1.comment=dt1.comment.astype('category') 
      
print("Here is a description of the data frame dt1 and number of lines\n")
print(dt1.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt1\n")
print(dt1.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt1.survey_date.describe())               
print("--------------------\n\n")
                    
print(dt1.date_time_obs.describe())               
print("--------------------\n\n")
                    
print(dt1.route.describe())               
print("--------------------\n\n")
                    
print(dt1.type.describe())               
print("--------------------\n\n")
                    
print(dt1.mileage.describe())               
print("--------------------\n\n")
                    
print(dt1.distance.describe())               
print("--------------------\n\n")
                    
print(dt1.direction.describe())               
print("--------------------\n\n")
                    
print(dt1.qflag1.describe())               
print("--------------------\n\n")
                    
print(dt1.qflag2.describe())               
print("--------------------\n\n")
                    
print(dt1.comment.describe())               
print("--------------------\n\n")
                    
                    
                




