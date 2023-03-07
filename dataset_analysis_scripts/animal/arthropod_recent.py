# Package ID: knb-lter-jrn.210008001.60 Cataloging System:https://pasta.edirepository.org.
# Data set title: Arthropod pitfall trap data from 12 NPP study locations at the Jornada Basin LTER site, 1996-2001.
# Data set creator:  David Lightfoot - Jornada Basin LTER (now at Univ. of NM) 
# Data set creator:  Walter Whitford - New Mexico State University 
# Contact:  John Anderson -  New Mexico State University  - 0000-0001-5060-9955
# Contact:  David Lightfoot -  Jornada Basin LTER (now at Univ. of NM)  - dlightfo@unm.edu
# Contact:   Data Manager -  Jornada Basin LTER  - datamanager.jrn.lter@gmail.com
# Stylesheet v1.0 for metadata conversion into program: John H. Porter, Univ. Virginia, jporter@virginia.edu      
# 
# This program creates numbered PANDA dataframes named dt1,dt2,dt3...,
# one for each data table in the dataset. It also provides some basic
# summaries of their contents. NumPy and Pandas modules need to be installed
# for the program to run. 

import numpy as np
import pandas as pd 

infile1  ="https://pasta.lternet.edu/package/data/eml/knb-lter-jrn/210008001/60/7e5c67ae8b4ff447a22aa2f331a4fa16".strip() 
infile1  = infile1.replace("https://","http://")
                 
dt1 =pd.read_csv(infile1 
          ,skiprows=1
            ,sep=","  
           , names=[
                    "period",     
                    "date",     
                    "zone",     
                    "site",     
                    "plot",     
                    "trap",     
                    "order",     
                    "family",     
                    "genus",     
                    "species",     
                    "count"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={  
#             'period':'str' , 
#             'date':'str' ,  
#             'zone':'str' ,  
#             'site':'str' ,  
#             'plot':'str' , 
#             'trap':'int' ,  
#             'order':'str' ,  
#             'family':'str' ,  
#             'genus':'str' ,  
#             'species':'str' , 
#             'count':'int'  
#        }
          ,parse_dates=[
                        'date',
                ] 
            ,na_values={
                  'order':[
                          'NA',],
                  'family':[
                          'NA',],
                  'genus':[
                          'NA',],
                  'species':[
                          'NA',],
                  'count':[
                          'NA',],} 
            
    )
# Coerce the data into the types specified in the metadata  
dt1.period=dt1.period.astype('category') 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt1=dt1.assign(date_datetime=pd.to_datetime(dt1.date,errors='coerce'))  
dt1.zone=dt1.zone.astype('category')  
dt1.site=dt1.site.astype('category')  
dt1.plot=dt1.plot.astype('category') 
dt1.trap=pd.to_numeric(dt1.trap,errors='coerce',downcast='integer')  
dt1.order=dt1.order.astype('category')  
dt1.family=dt1.family.astype('category')  
dt1.genus=dt1.genus.astype('category')  
dt1.species=dt1.species.astype('category') 
dt1.count=pd.to_numeric(dt1.count,errors='coerce',downcast='integer') 
      
print("Here is a description of the data frame dt1 and number of lines\n")
print(dt1.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt1\n")
print(dt1.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt1.period.describe())               
print("--------------------\n\n")
                    
print(dt1.date.describe())               
print("--------------------\n\n")
                    
print(dt1.zone.describe())               
print("--------------------\n\n")
                    
print(dt1.site.describe())               
print("--------------------\n\n")
                    
print(dt1.plot.describe())               
print("--------------------\n\n")
                    
print(dt1.trap.describe())               
print("--------------------\n\n")
                    
print(dt1.order.describe())               
print("--------------------\n\n")
                    
print(dt1.family.describe())               
print("--------------------\n\n")
                    
print(dt1.genus.describe())               
print("--------------------\n\n")
                    
print(dt1.species.describe())               
print("--------------------\n\n")
                    
print(dt1.count.describe())               
print("--------------------\n\n")
                    
                    
                




