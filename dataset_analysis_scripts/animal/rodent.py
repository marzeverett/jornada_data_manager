# Package ID: knb-lter-jrn.210262010.89 Cataloging System:https://pasta.edirepository.org.
# Data set title: Rodent abundance and biomass data across grassland-shrubland ecotones at 3 sites in the Jornada Basin, 2004-ongoing.
# Data set creator:  Brandon T Bestelmeyer - USDA-ARS Jornada Experimental Range 
# Data set creator:  Robert Schooley - University of Illinois 
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

infile1  ="https://pasta.lternet.edu/package/data/eml/knb-lter-jrn/210262010/89/f65572e18ceb0403b0d9a0d188a42411".strip() 
infile1  = infile1.replace("https://","http://")
                 
dt1 =pd.read_csv(infile1 
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "Year",     
                    "Site",     
                    "Habitat",     
                    "No_Individuals",     
                    "Abundance_no_ha",     
                    "Biomass_ha"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'Year':'str' ,  
#             'Site':'str' ,  
#             'Habitat':'str' , 
#             'No_Individuals':'float' , 
#             'Abundance_no_ha':'float' , 
#             'Biomass_ha':'float'  
#        }
          ,parse_dates=[
                        'Year',
                ] 
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt1=dt1.assign(Year_datetime=pd.to_datetime(dt1.Year,errors='coerce'))  
dt1.Site=dt1.Site.astype('category')  
dt1.Habitat=dt1.Habitat.astype('category') 
dt1.No_Individuals=pd.to_numeric(dt1.No_Individuals,errors='coerce') 
dt1.Abundance_no_ha=pd.to_numeric(dt1.Abundance_no_ha,errors='coerce') 
dt1.Biomass_ha=pd.to_numeric(dt1.Biomass_ha,errors='coerce') 
      
print("Here is a description of the data frame dt1 and number of lines\n")
print(dt1.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt1\n")
print(dt1.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt1.Year.describe())               
print("--------------------\n\n")
                    
print(dt1.Site.describe())               
print("--------------------\n\n")
                    
print(dt1.Habitat.describe())               
print("--------------------\n\n")
                    
print(dt1.No_Individuals.describe())               
print("--------------------\n\n")
                    
print(dt1.Abundance_no_ha.describe())               
print("--------------------\n\n")
                    
print(dt1.Biomass_ha.describe())               
print("--------------------\n\n")
                    
                    
                




