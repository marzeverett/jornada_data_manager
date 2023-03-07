# Package ID: knb-lter-jrn.210011001.2 Cataloging System:https://pasta.edirepository.org.
# Data set title: Seasonal aboveground plant biomass estimates at 15 net primary production (NPP) study sites at Jornada Basin LTER from 1989-ongoing.
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

infile1  ="https://pasta.lternet.edu/package/data/eml/knb-lter-jrn/210011001/2/387af8a5032b3a69b9e9ff660b70dcb3".strip() 
infile1  = infile1.replace("https://","http://")
                 
dt1 =pd.read_csv(infile1 
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "file_id",     
                    "year",     
                    "season",     
                    "date",     
                    "zone",     
                    "site",     
                    "quad",     
                    "spp",     
                    "volume",     
                    "cum_cover",     
                    "biomass",     
                    "USDA_code",     
                    "habit",     
                    "form",     
                    "cpath"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={  
#             'file_id':'str' , 
#             'year':'str' ,  
#             'season':'str' , 
#             'date':'str' ,  
#             'zone':'str' ,  
#             'site':'str' , 
#             'quad':'int' ,  
#             'spp':'str' , 
#             'volume':'float' , 
#             'cum_cover':'float' , 
#             'biomass':'float' ,  
#             'USDA_code':'str' ,  
#             'habit':'str' ,  
#             'form':'str' ,  
#             'cpath':'str'  
#        }
          ,parse_dates=[
                        'year',
                        'date',
                ] 
            ,na_values={
                  'spp':[
                          'NA',],
                  'volume':[
                          'NA',],
                  'cum_cover':[
                          'NA',],
                  'biomass':[
                          'NA',],
                  'USDA_code':[
                          'NA',],
                  'habit':[
                          'NA',],
                  'form':[
                          'NA',],
                  'cpath':[
                          'NA',],} 
            
    )
# Coerce the data into the types specified in the metadata  
dt1.file_id=dt1.file_id.astype('category') 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt1=dt1.assign(year_datetime=pd.to_datetime(dt1.year,errors='coerce'))  
dt1.season=dt1.season.astype('category') 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt1=dt1.assign(date_datetime=pd.to_datetime(dt1.date,errors='coerce'))  
dt1.zone=dt1.zone.astype('category')  
dt1.site=dt1.site.astype('category') 
dt1.quad=pd.to_numeric(dt1.quad,errors='coerce',downcast='integer')  
dt1.spp=dt1.spp.astype('category') 
dt1.volume=pd.to_numeric(dt1.volume,errors='coerce') 
dt1.cum_cover=pd.to_numeric(dt1.cum_cover,errors='coerce') 
dt1.biomass=pd.to_numeric(dt1.biomass,errors='coerce')  
dt1.USDA_code=dt1.USDA_code.astype('category')  
dt1.habit=dt1.habit.astype('category')  
dt1.form=dt1.form.astype('category')  
dt1.cpath=dt1.cpath.astype('category') 
      
print("Here is a description of the data frame dt1 and number of lines\n")
print(dt1.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt1\n")
print(dt1.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt1.file_id.describe())               
print("--------------------\n\n")
                    
print(dt1.year.describe())               
print("--------------------\n\n")
                    
print(dt1.season.describe())               
print("--------------------\n\n")
                    
print(dt1.date.describe())               
print("--------------------\n\n")
                    
print(dt1.zone.describe())               
print("--------------------\n\n")
                    
print(dt1.site.describe())               
print("--------------------\n\n")
                    
print(dt1.quad.describe())               
print("--------------------\n\n")
                    
print(dt1.spp.describe())               
print("--------------------\n\n")
                    
print(dt1.volume.describe())               
print("--------------------\n\n")
                    
print(dt1.cum_cover.describe())               
print("--------------------\n\n")
                    
print(dt1.biomass.describe())               
print("--------------------\n\n")
                    
print(dt1.USDA_code.describe())               
print("--------------------\n\n")
                    
print(dt1.habit.describe())               
print("--------------------\n\n")
                    
print(dt1.form.describe())               
print("--------------------\n\n")
                    
print(dt1.cpath.describe())               
print("--------------------\n\n")
                    
                    
                




