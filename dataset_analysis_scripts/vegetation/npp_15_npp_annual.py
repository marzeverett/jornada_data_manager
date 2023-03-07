# Package ID: knb-lter-jrn.210011003.105 Cataloging System:https://pasta.edirepository.org.
# Data set title: Annual mean estimates of aboveground net primary production (NPP) at 15 sites at Jornada Basin LTER, 1989-ongoing.
# Data set creator:  Debra C Peters - USDA-ARS Jornada Experimental Range 
# Data set creator:  Laura F Huenneke - New Mexico State University (Now at NAU) 
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

infile1  ="https://pasta.lternet.edu/package/data/eml/knb-lter-jrn/210011003/105/127124b0f04a1c71f34148e3d40a5c72".strip() 
infile1  = infile1.replace("https://","http://")
                 
dt1 =pd.read_csv(infile1 
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "year",     
                    "zone",     
                    "site",     
                    "npp_g_m2"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'year':'str' ,  
#             'zone':'str' ,  
#             'site':'str' , 
#             'npp_g_m2':'float'  
#        }
          ,parse_dates=[
                        'year',
                ] 
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt1=dt1.assign(year_datetime=pd.to_datetime(dt1.year,errors='coerce'))  
dt1.zone=dt1.zone.astype('category')  
dt1.site=dt1.site.astype('category') 
dt1.npp_g_m2=pd.to_numeric(dt1.npp_g_m2,errors='coerce') 
      
print("Here is a description of the data frame dt1 and number of lines\n")
print(dt1.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt1\n")
print(dt1.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt1.year.describe())               
print("--------------------\n\n")
                    
print(dt1.zone.describe())               
print("--------------------\n\n")
                    
print(dt1.site.describe())               
print("--------------------\n\n")
                    
print(dt1.npp_g_m2.describe())               
print("--------------------\n\n")
                    
                    
                




