# Package ID: knb-lter-jrn.210425001.76 Cataloging System:https://pasta.edirepository.org.
# Data set title: Gap-filled daily precipitation at the 15 long-term NPP sites at Jornada Basin LTER, 1980-ongoing.
# Data set creator:  Jin Yao - USDA-ARS Jornada Experimental Range 
# Data set creator:  Heather Savoy - USDA-ARS Jornada Experimental Range 
# Data set creator:  John Anderson - Jornada Basin LTER/New Mexico State University 
# Data set creator:  Debra C Peters - USDA-ARS Jornada Experimental Range 
# Metadata Provider:    - Jornada Basin LTER 
# Contact:    - Information Manager Jornada Basin LTER  - jornada.data@nmsu.edu
# Stylesheet v1.0 for metadata conversion into program: John H. Porter, Univ. Virginia, jporter@virginia.edu      
# 
# This program creates numbered PANDA dataframes named dt1,dt2,dt3...,
# one for each data table in the dataset. It also provides some basic
# summaries of their contents. NumPy and Pandas modules need to be installed
# for the program to run. 

import numpy as np
import pandas as pd 

infile1  ="https://pasta.lternet.edu/package/data/eml/knb-lter-jrn/210425001/76/ef5203ba715401af1fca6e60707d27bb".strip() 
infile1  = infile1.replace("https://","http://")
                 
dt1 =pd.read_csv(infile1 
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "date",     
                    "zone",     
                    "site",     
                    "est_precp",     
                    "flag"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'date':'str' ,  
#             'zone':'str' ,  
#             'site':'str' , 
#             'est_precp':'float' ,  
#             'flag':'str'  
#        }
          ,parse_dates=[
                        'date',
                ] 
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt1=dt1.assign(date_datetime=pd.to_datetime(dt1.date,errors='coerce'))  
dt1.zone=dt1.zone.astype('category')  
dt1.site=dt1.site.astype('category') 
dt1.est_precp=pd.to_numeric(dt1.est_precp,errors='coerce')  
dt1.flag=dt1.flag.astype('category') 
      
print("Here is a description of the data frame dt1 and number of lines\n")
print(dt1.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt1\n")
print(dt1.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt1.date.describe())               
print("--------------------\n\n")
                    
print(dt1.zone.describe())               
print("--------------------\n\n")
                    
print(dt1.site.describe())               
print("--------------------\n\n")
                    
print(dt1.est_precp.describe())               
print("--------------------\n\n")
                    
print(dt1.flag.describe())               
print("--------------------\n\n")
                    
                    
                 

infile2  ="https://pasta.lternet.edu/package/data/eml/knb-lter-jrn/210425001/76/b28710a12a7735a91f74a974b2ccc11f".strip() 
infile2  = infile2.replace("https://","http://")
                 
dt2 =pd.read_csv(infile2 
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "site",     
                    "priority",     
                    "gauge",     
                    "distance",     
                    "affiliation",     
                    "type",     
                    "start",     
                    "end"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={  
#             'site':'str' , 
#             'priority':'int' ,  
#             'gauge':'str' , 
#             'distance':'float' ,  
#             'affiliation':'str' ,  
#             'type':'str' , 
#             'start':'str' , 
#             'end':'str'  
#        }
          ,parse_dates=[
                        'start',
                        'end',
                ] 
    )
# Coerce the data into the types specified in the metadata  
dt2.site=dt2.site.astype('category') 
dt2.priority=pd.to_numeric(dt2.priority,errors='coerce',downcast='integer')  
dt2.gauge=dt2.gauge.astype('category') 
dt2.distance=pd.to_numeric(dt2.distance,errors='coerce')  
dt2.affiliation=dt2.affiliation.astype('category')  
dt2.type=dt2.type.astype('category') 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt2=dt2.assign(start_datetime=pd.to_datetime(dt2.start,errors='coerce')) 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt2=dt2.assign(end_datetime=pd.to_datetime(dt2.end,errors='coerce')) 
      
print("Here is a description of the data frame dt2 and number of lines\n")
print(dt2.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt2\n")
print(dt2.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt2.site.describe())               
print("--------------------\n\n")
                    
print(dt2.priority.describe())               
print("--------------------\n\n")
                    
print(dt2.gauge.describe())               
print("--------------------\n\n")
                    
print(dt2.distance.describe())               
print("--------------------\n\n")
                    
print(dt2.affiliation.describe())               
print("--------------------\n\n")
                    
print(dt2.type.describe())               
print("--------------------\n\n")
                    
print(dt2.start.describe())               
print("--------------------\n\n")
                    
print(dt2.end.describe())               
print("--------------------\n\n")
                    
                    
                 

infile3  ="https://pasta.lternet.edu/package/data/eml/knb-lter-jrn/210425001/76/8ec05070d572061e0214fa8e1835c233".strip() 
infile3  = infile3.replace("https://","http://")
                 
dt3 =pd.read_csv(infile3 
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "JRN_ID",     
                    "site",     
                    "JRN_Num",     
                    "Zone",     
                    "pkg",     
                    "version"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={  
#             'JRN_ID':'str' ,  
#             'site':'str' , 
#             'JRN_Num':'int' ,  
#             'Zone':'str' , 
#             'pkg':'int' , 
#             'version':'int'  
#        }
    )
# Coerce the data into the types specified in the metadata  
dt3.JRN_ID=dt3.JRN_ID.astype('category')  
dt3.site=dt3.site.astype('category') 
dt3.JRN_Num=pd.to_numeric(dt3.JRN_Num,errors='coerce',downcast='integer')  
dt3.Zone=dt3.Zone.astype('category') 
dt3.pkg=pd.to_numeric(dt3.pkg,errors='coerce',downcast='integer') 
dt3.version=pd.to_numeric(dt3.version,errors='coerce',downcast='integer') 
      
print("Here is a description of the data frame dt3 and number of lines\n")
print(dt3.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt3\n")
print(dt3.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt3.JRN_ID.describe())               
print("--------------------\n\n")
                    
print(dt3.site.describe())               
print("--------------------\n\n")
                    
print(dt3.JRN_Num.describe())               
print("--------------------\n\n")
                    
print(dt3.Zone.describe())               
print("--------------------\n\n")
                    
print(dt3.pkg.describe())               
print("--------------------\n\n")
                    
print(dt3.version.describe())               
print("--------------------\n\n")
                    
                    
                




