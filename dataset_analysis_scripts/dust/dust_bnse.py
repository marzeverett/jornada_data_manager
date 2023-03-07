# Package ID: knb-lter-jrn.210288001.103 Cataloging System:https://pasta.edirepository.org.
# Data set title: Aeolian dust weights sampled by BSNE collectors in 18 locations at the Jornada Basin LTER site, 1998-ongoing.
# Data set creator:  Gregory S Okin - University of California Los Angeles 
# Data set creator:  Dale Gillette - National Oceanic and Atmospheric Administration 
# Metadata Provider:    - Jornada Basin LTER/New Mexico State University 
# Contact:    - Jornada Basin LTER Information Manager Jornada Basin LTER/New Mexico State University  - jornada.data@nmsu.edu
# Stylesheet v1.0 for metadata conversion into program: John H. Porter, Univ. Virginia, jporter@virginia.edu      
# 
# This program creates numbered PANDA dataframes named dt1,dt2,dt3...,
# one for each data table in the dataset. It also provides some basic
# summaries of their contents. NumPy and Pandas modules need to be installed
# for the program to run. 

import numpy as np
import pandas as pd 

infile1  ="https://pasta.lternet.edu/package/data/eml/knb-lter-jrn/210288001/103/6f125d7db533a1e624fe10a005b47553".strip() 
infile1  = infile1.replace("https://","http://")
                 
dt1 =pd.read_csv(infile1 
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "date",     
                    "site",     
                    "zone",     
                    "stand_id",     
                    "height_cm",     
                    "dust_weight",     
                    "qwt",     
                    "comments"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'date':'str' ,  
#             'site':'str' ,  
#             'zone':'str' ,  
#             'stand_id':'str' , 
#             'height_cm':'float' , 
#             'dust_weight':'float' ,  
#             'qwt':'str' ,  
#             'comments':'str'  
#        }
          ,parse_dates=[
                        'date',
                ] 
            ,na_values={
                  'zone':[
                          'NA',],
                  'dust_weight':[
                          'NA',],
                  'qwt':[
                          'NA',],
                  'comments':[
                          'NA',],} 
            
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt1=dt1.assign(date_datetime=pd.to_datetime(dt1.date,errors='coerce'))  
dt1.site=dt1.site.astype('category')  
dt1.zone=dt1.zone.astype('category')  
dt1.stand_id=dt1.stand_id.astype('category') 
dt1.height_cm=pd.to_numeric(dt1.height_cm,errors='coerce') 
dt1.dust_weight=pd.to_numeric(dt1.dust_weight,errors='coerce')  
dt1.qwt=dt1.qwt.astype('category')  
dt1.comments=dt1.comments.astype('category') 
      
print("Here is a description of the data frame dt1 and number of lines\n")
print(dt1.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt1\n")
print(dt1.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt1.date.describe())               
print("--------------------\n\n")
                    
print(dt1.site.describe())               
print("--------------------\n\n")
                    
print(dt1.zone.describe())               
print("--------------------\n\n")
                    
print(dt1.stand_id.describe())               
print("--------------------\n\n")
                    
print(dt1.height_cm.describe())               
print("--------------------\n\n")
                    
print(dt1.dust_weight.describe())               
print("--------------------\n\n")
                    
print(dt1.qwt.describe())               
print("--------------------\n\n")
                    
print(dt1.comments.describe())               
print("--------------------\n\n")
                    
                    
                






