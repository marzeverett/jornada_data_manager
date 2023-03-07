# Package ID: knb-lter-jrn.210437093.34 Cataloging System:https://pasta.edirepository.org.
# Data set title: Jornada Basin LTER: Wireless meteorological station at NPP C-SAND site: Daily average soil volumetric water content data:  2013 - ongoing.
# Data set creator:  Michael Duniway - JRN LTER 
# Contact:   Data Manager - JRN-LTER Information Manager   - datamanager.jrn.lter@gmail.com
# Stylesheet v1.0 for metadata conversion into program: John H. Porter, Univ. Virginia, jporter@virginia.edu      
# 
# This program creates numbered PANDA dataframes named dt1,dt2,dt3...,
# one for each data table in the dataset. It also provides some basic
# summaries of their contents. NumPy and Pandas modules need to be installed
# for the program to run. 

import numpy as np
import pandas as pd 

infile1  ="https://pasta.lternet.edu/package/data/eml/knb-lter-jrn/210437093/34/4e2a71a3abeae5be8aa43b8962fb93c1".strip() 
infile1  = infile1.replace("https://","http://")
                 
dt1 =pd.read_csv(infile1 
          ,skiprows=4
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "Date",     
                    "Year",     
                    "YearDay",     
                    "Hours",     
                    "RECORD",     
                    "Flag_RECORD",     
                    "Sitename",     
                    "VWC_Avg_201_10cm",     
                    "Flag_VWC_Avg_201_10cm",     
                    "EC_Avg_201_10cm",     
                    "Flag_EC_Avg_201_10cm",     
                    "Soil_Temp_Avg_201_10cm",     
                    "Flag_Soil_Temp_Avg_201_10cm",     
                    "P_Avg_201_10cm",     
                    "Flag_P_Avg_201_10cm",     
                    "Period_Avg_201_10cm",     
                    "Flag_Period_Avg_201_10cm",     
                    "Voltage_Ratio_Avg_201_10cm",     
                    "Flag_Voltage_Ratio_Avg_201_10cm",     
                    "VWC_Avg_201_20cm",     
                    "Flag_VWC_Avg_201_20cm",     
                    "EC_Avg_201_20cm",     
                    "Flag_EC_Avg_201_20cm",     
                    "Soil_Temp_Avg_201_20cm",     
                    "Flag_Soil_Temp_Avg_201_20cm",     
                    "P_Avg_201_20cm",     
                    "Flag_P_Avg_201_20cm",     
                    "Period_Avg_201_20cm",     
                    "Flag_Period_Avg_201_20cm",     
                    "Voltage_Ratio_Avg_201_20cm",     
                    "Flag_Voltage_Ratio_Avg_201_20cm",     
                    "VWC_Avg_201_30cm",     
                    "Flag_VWC_Avg_201_30cm",     
                    "EC_Avg_201_30cm",     
                    "Flag_EC_Avg_201_30cm",     
                    "Soil_Temp_Avg_201_30cm",     
                    "Flag_Soil_Temp_Avg_201_30cm",     
                    "P_Avg_201_30cm",     
                    "Flag_P_Avg_201_30cm",     
                    "Period_Avg_201_30cm",     
                    "Flag_Period_Avg_201_30cm",     
                    "Voltage_Ratio_Avg_201_30cm",     
                    "Flag_Voltage_Ratio_Avg_201_30cm",     
                    "VWC_Avg_202_10cm",     
                    "Flag_VWC_Avg_202_10cm",     
                    "EC_Avg_202_10cm",     
                    "Flag_EC_Avg_202_10cm",     
                    "Soil_Temp_Avg_202_10cm",     
                    "Flag_Soil_Temp_Avg_202_10cm",     
                    "P_Avg_202_10cm",     
                    "Flag_P_Avg_202_10cm",     
                    "Period_Avg_202_10cm",     
                    "Flag_Period_Avg_202_10cm",     
                    "Voltage_Ratio_Avg_202_10cm",     
                    "Flag_Voltage_Ratio_Avg_202_10cm",     
                    "VWC_Avg_202_20cm",     
                    "Flag_VWC_Avg_202_20cm",     
                    "EC_Avg_202_20cm",     
                    "Flag_EC_Avg_202_20cm",     
                    "Soil_Temp_Avg_202_20cm",     
                    "Flag_Soil_Temp_Avg_202_20cm",     
                    "P_Avg_202_20cm",     
                    "Flag_P_Avg_202_20cm",     
                    "Period_Avg_202_20cm",     
                    "Flag_Period_Avg_202_20cm",     
                    "Voltage_Ratio_Avg_202_20cm",     
                    "Flag_Voltage_Ratio_Avg_202_20cm",     
                    "VWC_Avg_202_30cm",     
                    "Flag_VWC_Avg_202_30cm",     
                    "EC_Avg_202_30cm",     
                    "Flag_EC_Avg_202_30cm",     
                    "Soil_Temp_Avg_202_30cm",     
                    "Flag_Soil_Temp_Avg_202_30cm",     
                    "P_Avg_202_30cm",     
                    "Flag_P_Avg_202_30cm",     
                    "Period_Avg_202_30cm",     
                    "Flag_Period_Avg_202_30cm",     
                    "Voltage_Ratio_Avg_202_30cm",     
                    "Flag_Voltage_Ratio_Avg_202_30cm",     
                    "VwcCorr_Avg_201_10cm",     
                    "Flag_VwcCorr_Avg_201_10cm",     
                    "VwcCorr_Avg_201_20cm",     
                    "Flag_VwcCorr_Avg_201_20cm",     
                    "VwcCorr_Avg_201_30cm",     
                    "Flag_VwcCorr_Avg_201_30cm",     
                    "VwcCorr_Avg_202_10cm",     
                    "Flag_VwcCorr_Avg_202_10cm",     
                    "VwcCorr_Avg_202_20cm",     
                    "Flag_VwcCorr_Avg_202_20cm",     
                    "VwcCorr_Avg_202_30cm",     
                    "Flag_VwcCorr_Avg_202_30cm"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'Date':'str' , 
#             'Year':'float' , 
#             'YearDay':'float' , 
#             'Hours':'float' , 
#             'RECORD':'float' ,  
#             'Flag_RECORD':'str' , 
#             'Sitename':'str', 
#             'VWC_Avg_201_10cm':'float' ,  
#             'Flag_VWC_Avg_201_10cm':'str' , 
#             'EC_Avg_201_10cm':'float' ,  
#             'Flag_EC_Avg_201_10cm':'str' , 
#             'Soil_Temp_Avg_201_10cm':'float' ,  
#             'Flag_Soil_Temp_Avg_201_10cm':'str' , 
#             'P_Avg_201_10cm':'float' ,  
#             'Flag_P_Avg_201_10cm':'str' , 
#             'Period_Avg_201_10cm':'float' ,  
#             'Flag_Period_Avg_201_10cm':'str' , 
#             'Voltage_Ratio_Avg_201_10cm':'float' ,  
#             'Flag_Voltage_Ratio_Avg_201_10cm':'str' , 
#             'VWC_Avg_201_20cm':'float' ,  
#             'Flag_VWC_Avg_201_20cm':'str' , 
#             'EC_Avg_201_20cm':'float' ,  
#             'Flag_EC_Avg_201_20cm':'str' , 
#             'Soil_Temp_Avg_201_20cm':'float' ,  
#             'Flag_Soil_Temp_Avg_201_20cm':'str' , 
#             'P_Avg_201_20cm':'float' ,  
#             'Flag_P_Avg_201_20cm':'str' , 
#             'Period_Avg_201_20cm':'float' ,  
#             'Flag_Period_Avg_201_20cm':'str' , 
#             'Voltage_Ratio_Avg_201_20cm':'float' ,  
#             'Flag_Voltage_Ratio_Avg_201_20cm':'str' , 
#             'VWC_Avg_201_30cm':'float' ,  
#             'Flag_VWC_Avg_201_30cm':'str' , 
#             'EC_Avg_201_30cm':'float' ,  
#             'Flag_EC_Avg_201_30cm':'str' , 
#             'Soil_Temp_Avg_201_30cm':'float' ,  
#             'Flag_Soil_Temp_Avg_201_30cm':'str' , 
#             'P_Avg_201_30cm':'float' ,  
#             'Flag_P_Avg_201_30cm':'str' , 
#             'Period_Avg_201_30cm':'float' ,  
#             'Flag_Period_Avg_201_30cm':'str' , 
#             'Voltage_Ratio_Avg_201_30cm':'float' ,  
#             'Flag_Voltage_Ratio_Avg_201_30cm':'str' , 
#             'VWC_Avg_202_10cm':'float' ,  
#             'Flag_VWC_Avg_202_10cm':'str' , 
#             'EC_Avg_202_10cm':'float' ,  
#             'Flag_EC_Avg_202_10cm':'str' , 
#             'Soil_Temp_Avg_202_10cm':'float' ,  
#             'Flag_Soil_Temp_Avg_202_10cm':'str' , 
#             'P_Avg_202_10cm':'float' ,  
#             'Flag_P_Avg_202_10cm':'str' , 
#             'Period_Avg_202_10cm':'float' ,  
#             'Flag_Period_Avg_202_10cm':'str' , 
#             'Voltage_Ratio_Avg_202_10cm':'float' ,  
#             'Flag_Voltage_Ratio_Avg_202_10cm':'str' , 
#             'VWC_Avg_202_20cm':'float' ,  
#             'Flag_VWC_Avg_202_20cm':'str' , 
#             'EC_Avg_202_20cm':'float' ,  
#             'Flag_EC_Avg_202_20cm':'str' , 
#             'Soil_Temp_Avg_202_20cm':'float' ,  
#             'Flag_Soil_Temp_Avg_202_20cm':'str' , 
#             'P_Avg_202_20cm':'float' ,  
#             'Flag_P_Avg_202_20cm':'str' , 
#             'Period_Avg_202_20cm':'float' ,  
#             'Flag_Period_Avg_202_20cm':'str' , 
#             'Voltage_Ratio_Avg_202_20cm':'float' ,  
#             'Flag_Voltage_Ratio_Avg_202_20cm':'str' , 
#             'VWC_Avg_202_30cm':'float' ,  
#             'Flag_VWC_Avg_202_30cm':'str' , 
#             'EC_Avg_202_30cm':'float' ,  
#             'Flag_EC_Avg_202_30cm':'str' , 
#             'Soil_Temp_Avg_202_30cm':'float' ,  
#             'Flag_Soil_Temp_Avg_202_30cm':'str' , 
#             'P_Avg_202_30cm':'float' ,  
#             'Flag_P_Avg_202_30cm':'str' , 
#             'Period_Avg_202_30cm':'float' ,  
#             'Flag_Period_Avg_202_30cm':'str' , 
#             'Voltage_Ratio_Avg_202_30cm':'float' ,  
#             'Flag_Voltage_Ratio_Avg_202_30cm':'str' , 
#             'VwcCorr_Avg_201_10cm':'float' ,  
#             'Flag_VwcCorr_Avg_201_10cm':'str' , 
#             'VwcCorr_Avg_201_20cm':'float' ,  
#             'Flag_VwcCorr_Avg_201_20cm':'str' , 
#             'VwcCorr_Avg_201_30cm':'float' ,  
#             'Flag_VwcCorr_Avg_201_30cm':'str' , 
#             'VwcCorr_Avg_202_10cm':'float' ,  
#             'Flag_VwcCorr_Avg_202_10cm':'str' , 
#             'VwcCorr_Avg_202_20cm':'float' ,  
#             'Flag_VwcCorr_Avg_202_20cm':'str' , 
#             'VwcCorr_Avg_202_30cm':'float' ,  
#             'Flag_VwcCorr_Avg_202_30cm':'str'  
#        }
          ,parse_dates=[
                        'Date',
                ] 
            ,na_values={
                  'Year':[
                          'NaN',],
                  'YearDay':[
                          'NaN',],
                  'Hours':[
                          'NaN',],
                  'RECORD':[
                          'NaN',],
                  'VWC_Avg_201_10cm':[
                          'NaN',],
                  'EC_Avg_201_10cm':[
                          'NaN',],
                  'Soil_Temp_Avg_201_10cm':[
                          'NaN',],
                  'P_Avg_201_10cm':[
                          'NaN',],
                  'Period_Avg_201_10cm':[
                          'NaN',],
                  'Voltage_Ratio_Avg_201_10cm':[
                          'NaN',],
                  'VWC_Avg_201_20cm':[
                          'NaN',],
                  'EC_Avg_201_20cm':[
                          'NaN',],
                  'Soil_Temp_Avg_201_20cm':[
                          'NaN',],
                  'P_Avg_201_20cm':[
                          'NaN',],
                  'Period_Avg_201_20cm':[
                          'NaN',],
                  'Voltage_Ratio_Avg_201_20cm':[
                          'NaN',],
                  'VWC_Avg_201_30cm':[
                          'NaN',],
                  'EC_Avg_201_30cm':[
                          'NaN',],
                  'Soil_Temp_Avg_201_30cm':[
                          'NaN',],
                  'P_Avg_201_30cm':[
                          'NaN',],
                  'Period_Avg_201_30cm':[
                          'NaN',],
                  'Voltage_Ratio_Avg_201_30cm':[
                          'NaN',],
                  'VWC_Avg_202_10cm':[
                          'NaN',],
                  'EC_Avg_202_10cm':[
                          'NaN',],
                  'Soil_Temp_Avg_202_10cm':[
                          'NaN',],
                  'P_Avg_202_10cm':[
                          'NaN',],
                  'Period_Avg_202_10cm':[
                          'NaN',],
                  'Voltage_Ratio_Avg_202_10cm':[
                          'NaN',],
                  'VWC_Avg_202_20cm':[
                          'NaN',],
                  'EC_Avg_202_20cm':[
                          'NaN',],
                  'Soil_Temp_Avg_202_20cm':[
                          'NaN',],
                  'P_Avg_202_20cm':[
                          'NaN',],
                  'Period_Avg_202_20cm':[
                          'NaN',],
                  'Voltage_Ratio_Avg_202_20cm':[
                          'NaN',],
                  'VWC_Avg_202_30cm':[
                          'NaN',],
                  'EC_Avg_202_30cm':[
                          'NaN',],
                  'Soil_Temp_Avg_202_30cm':[
                          'NaN',],
                  'P_Avg_202_30cm':[
                          'NaN',],
                  'Period_Avg_202_30cm':[
                          'NaN',],
                  'Voltage_Ratio_Avg_202_30cm':[
                          'NaN',],
                  'VwcCorr_Avg_201_10cm':[
                          'NaN',],
                  'VwcCorr_Avg_201_20cm':[
                          'NaN',],
                  'VwcCorr_Avg_201_30cm':[
                          'NaN',],
                  'VwcCorr_Avg_202_10cm':[
                          'NaN',],
                  'VwcCorr_Avg_202_20cm':[
                          'NaN',],
                  'VwcCorr_Avg_202_30cm':[
                          'NaN',],} 
            
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt1=dt1.assign(Date_datetime=pd.to_datetime(dt1.Date,errors='coerce')) 
dt1.Year=pd.to_numeric(dt1.Year,errors='coerce') 
dt1.YearDay=pd.to_numeric(dt1.YearDay,errors='coerce') 
dt1.Hours=pd.to_numeric(dt1.Hours,errors='coerce') 
dt1.RECORD=pd.to_numeric(dt1.RECORD,errors='coerce')  
dt1.Flag_RECORD=dt1.Flag_RECORD.astype('category') 
dt1.Sitename=str(dt1.Sitename) 
dt1.VWC_Avg_201_10cm=pd.to_numeric(dt1.VWC_Avg_201_10cm,errors='coerce')  
dt1.Flag_VWC_Avg_201_10cm=dt1.Flag_VWC_Avg_201_10cm.astype('category') 
dt1.EC_Avg_201_10cm=pd.to_numeric(dt1.EC_Avg_201_10cm,errors='coerce')  
dt1.Flag_EC_Avg_201_10cm=dt1.Flag_EC_Avg_201_10cm.astype('category') 
dt1.Soil_Temp_Avg_201_10cm=pd.to_numeric(dt1.Soil_Temp_Avg_201_10cm,errors='coerce')  
dt1.Flag_Soil_Temp_Avg_201_10cm=dt1.Flag_Soil_Temp_Avg_201_10cm.astype('category') 
dt1.P_Avg_201_10cm=pd.to_numeric(dt1.P_Avg_201_10cm,errors='coerce')  
dt1.Flag_P_Avg_201_10cm=dt1.Flag_P_Avg_201_10cm.astype('category') 
dt1.Period_Avg_201_10cm=pd.to_numeric(dt1.Period_Avg_201_10cm,errors='coerce')  
dt1.Flag_Period_Avg_201_10cm=dt1.Flag_Period_Avg_201_10cm.astype('category') 
dt1.Voltage_Ratio_Avg_201_10cm=pd.to_numeric(dt1.Voltage_Ratio_Avg_201_10cm,errors='coerce')  
dt1.Flag_Voltage_Ratio_Avg_201_10cm=dt1.Flag_Voltage_Ratio_Avg_201_10cm.astype('category') 
dt1.VWC_Avg_201_20cm=pd.to_numeric(dt1.VWC_Avg_201_20cm,errors='coerce')  
dt1.Flag_VWC_Avg_201_20cm=dt1.Flag_VWC_Avg_201_20cm.astype('category') 
dt1.EC_Avg_201_20cm=pd.to_numeric(dt1.EC_Avg_201_20cm,errors='coerce')  
dt1.Flag_EC_Avg_201_20cm=dt1.Flag_EC_Avg_201_20cm.astype('category') 
dt1.Soil_Temp_Avg_201_20cm=pd.to_numeric(dt1.Soil_Temp_Avg_201_20cm,errors='coerce')  
dt1.Flag_Soil_Temp_Avg_201_20cm=dt1.Flag_Soil_Temp_Avg_201_20cm.astype('category') 
dt1.P_Avg_201_20cm=pd.to_numeric(dt1.P_Avg_201_20cm,errors='coerce')  
dt1.Flag_P_Avg_201_20cm=dt1.Flag_P_Avg_201_20cm.astype('category') 
dt1.Period_Avg_201_20cm=pd.to_numeric(dt1.Period_Avg_201_20cm,errors='coerce')  
dt1.Flag_Period_Avg_201_20cm=dt1.Flag_Period_Avg_201_20cm.astype('category') 
dt1.Voltage_Ratio_Avg_201_20cm=pd.to_numeric(dt1.Voltage_Ratio_Avg_201_20cm,errors='coerce')  
dt1.Flag_Voltage_Ratio_Avg_201_20cm=dt1.Flag_Voltage_Ratio_Avg_201_20cm.astype('category') 
dt1.VWC_Avg_201_30cm=pd.to_numeric(dt1.VWC_Avg_201_30cm,errors='coerce')  
dt1.Flag_VWC_Avg_201_30cm=dt1.Flag_VWC_Avg_201_30cm.astype('category') 
dt1.EC_Avg_201_30cm=pd.to_numeric(dt1.EC_Avg_201_30cm,errors='coerce')  
dt1.Flag_EC_Avg_201_30cm=dt1.Flag_EC_Avg_201_30cm.astype('category') 
dt1.Soil_Temp_Avg_201_30cm=pd.to_numeric(dt1.Soil_Temp_Avg_201_30cm,errors='coerce')  
dt1.Flag_Soil_Temp_Avg_201_30cm=dt1.Flag_Soil_Temp_Avg_201_30cm.astype('category') 
dt1.P_Avg_201_30cm=pd.to_numeric(dt1.P_Avg_201_30cm,errors='coerce')  
dt1.Flag_P_Avg_201_30cm=dt1.Flag_P_Avg_201_30cm.astype('category') 
dt1.Period_Avg_201_30cm=pd.to_numeric(dt1.Period_Avg_201_30cm,errors='coerce')  
dt1.Flag_Period_Avg_201_30cm=dt1.Flag_Period_Avg_201_30cm.astype('category') 
dt1.Voltage_Ratio_Avg_201_30cm=pd.to_numeric(dt1.Voltage_Ratio_Avg_201_30cm,errors='coerce')  
dt1.Flag_Voltage_Ratio_Avg_201_30cm=dt1.Flag_Voltage_Ratio_Avg_201_30cm.astype('category') 
dt1.VWC_Avg_202_10cm=pd.to_numeric(dt1.VWC_Avg_202_10cm,errors='coerce')  
dt1.Flag_VWC_Avg_202_10cm=dt1.Flag_VWC_Avg_202_10cm.astype('category') 
dt1.EC_Avg_202_10cm=pd.to_numeric(dt1.EC_Avg_202_10cm,errors='coerce')  
dt1.Flag_EC_Avg_202_10cm=dt1.Flag_EC_Avg_202_10cm.astype('category') 
dt1.Soil_Temp_Avg_202_10cm=pd.to_numeric(dt1.Soil_Temp_Avg_202_10cm,errors='coerce')  
dt1.Flag_Soil_Temp_Avg_202_10cm=dt1.Flag_Soil_Temp_Avg_202_10cm.astype('category') 
dt1.P_Avg_202_10cm=pd.to_numeric(dt1.P_Avg_202_10cm,errors='coerce')  
dt1.Flag_P_Avg_202_10cm=dt1.Flag_P_Avg_202_10cm.astype('category') 
dt1.Period_Avg_202_10cm=pd.to_numeric(dt1.Period_Avg_202_10cm,errors='coerce')  
dt1.Flag_Period_Avg_202_10cm=dt1.Flag_Period_Avg_202_10cm.astype('category') 
dt1.Voltage_Ratio_Avg_202_10cm=pd.to_numeric(dt1.Voltage_Ratio_Avg_202_10cm,errors='coerce')  
dt1.Flag_Voltage_Ratio_Avg_202_10cm=dt1.Flag_Voltage_Ratio_Avg_202_10cm.astype('category') 
dt1.VWC_Avg_202_20cm=pd.to_numeric(dt1.VWC_Avg_202_20cm,errors='coerce')  
dt1.Flag_VWC_Avg_202_20cm=dt1.Flag_VWC_Avg_202_20cm.astype('category') 
dt1.EC_Avg_202_20cm=pd.to_numeric(dt1.EC_Avg_202_20cm,errors='coerce')  
dt1.Flag_EC_Avg_202_20cm=dt1.Flag_EC_Avg_202_20cm.astype('category') 
dt1.Soil_Temp_Avg_202_20cm=pd.to_numeric(dt1.Soil_Temp_Avg_202_20cm,errors='coerce')  
dt1.Flag_Soil_Temp_Avg_202_20cm=dt1.Flag_Soil_Temp_Avg_202_20cm.astype('category') 
dt1.P_Avg_202_20cm=pd.to_numeric(dt1.P_Avg_202_20cm,errors='coerce')  
dt1.Flag_P_Avg_202_20cm=dt1.Flag_P_Avg_202_20cm.astype('category') 
dt1.Period_Avg_202_20cm=pd.to_numeric(dt1.Period_Avg_202_20cm,errors='coerce')  
dt1.Flag_Period_Avg_202_20cm=dt1.Flag_Period_Avg_202_20cm.astype('category') 
dt1.Voltage_Ratio_Avg_202_20cm=pd.to_numeric(dt1.Voltage_Ratio_Avg_202_20cm,errors='coerce')  
dt1.Flag_Voltage_Ratio_Avg_202_20cm=dt1.Flag_Voltage_Ratio_Avg_202_20cm.astype('category') 
dt1.VWC_Avg_202_30cm=pd.to_numeric(dt1.VWC_Avg_202_30cm,errors='coerce')  
dt1.Flag_VWC_Avg_202_30cm=dt1.Flag_VWC_Avg_202_30cm.astype('category') 
dt1.EC_Avg_202_30cm=pd.to_numeric(dt1.EC_Avg_202_30cm,errors='coerce')  
dt1.Flag_EC_Avg_202_30cm=dt1.Flag_EC_Avg_202_30cm.astype('category') 
dt1.Soil_Temp_Avg_202_30cm=pd.to_numeric(dt1.Soil_Temp_Avg_202_30cm,errors='coerce')  
dt1.Flag_Soil_Temp_Avg_202_30cm=dt1.Flag_Soil_Temp_Avg_202_30cm.astype('category') 
dt1.P_Avg_202_30cm=pd.to_numeric(dt1.P_Avg_202_30cm,errors='coerce')  
dt1.Flag_P_Avg_202_30cm=dt1.Flag_P_Avg_202_30cm.astype('category') 
dt1.Period_Avg_202_30cm=pd.to_numeric(dt1.Period_Avg_202_30cm,errors='coerce')  
dt1.Flag_Period_Avg_202_30cm=dt1.Flag_Period_Avg_202_30cm.astype('category') 
dt1.Voltage_Ratio_Avg_202_30cm=pd.to_numeric(dt1.Voltage_Ratio_Avg_202_30cm,errors='coerce')  
dt1.Flag_Voltage_Ratio_Avg_202_30cm=dt1.Flag_Voltage_Ratio_Avg_202_30cm.astype('category') 
dt1.VwcCorr_Avg_201_10cm=pd.to_numeric(dt1.VwcCorr_Avg_201_10cm,errors='coerce')  
dt1.Flag_VwcCorr_Avg_201_10cm=dt1.Flag_VwcCorr_Avg_201_10cm.astype('category') 
dt1.VwcCorr_Avg_201_20cm=pd.to_numeric(dt1.VwcCorr_Avg_201_20cm,errors='coerce')  
dt1.Flag_VwcCorr_Avg_201_20cm=dt1.Flag_VwcCorr_Avg_201_20cm.astype('category') 
dt1.VwcCorr_Avg_201_30cm=pd.to_numeric(dt1.VwcCorr_Avg_201_30cm,errors='coerce')  
dt1.Flag_VwcCorr_Avg_201_30cm=dt1.Flag_VwcCorr_Avg_201_30cm.astype('category') 
dt1.VwcCorr_Avg_202_10cm=pd.to_numeric(dt1.VwcCorr_Avg_202_10cm,errors='coerce')  
dt1.Flag_VwcCorr_Avg_202_10cm=dt1.Flag_VwcCorr_Avg_202_10cm.astype('category') 
dt1.VwcCorr_Avg_202_20cm=pd.to_numeric(dt1.VwcCorr_Avg_202_20cm,errors='coerce')  
dt1.Flag_VwcCorr_Avg_202_20cm=dt1.Flag_VwcCorr_Avg_202_20cm.astype('category') 
dt1.VwcCorr_Avg_202_30cm=pd.to_numeric(dt1.VwcCorr_Avg_202_30cm,errors='coerce')  
dt1.Flag_VwcCorr_Avg_202_30cm=dt1.Flag_VwcCorr_Avg_202_30cm.astype('category') 
      
print("Here is a description of the data frame dt1 and number of lines\n")
print(dt1.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt1\n")
print(dt1.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt1.Date.describe())               
print("--------------------\n\n")
                    
print(dt1.Year.describe())               
print("--------------------\n\n")
                    
print(dt1.YearDay.describe())               
print("--------------------\n\n")
                    
print(dt1.Hours.describe())               
print("--------------------\n\n")
                    
print(dt1.RECORD.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_RECORD.describe())               
print("--------------------\n\n")
                    
print(dt1.Sitename.describe())               
print("--------------------\n\n")
                    
print(dt1.VWC_Avg_201_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_VWC_Avg_201_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.EC_Avg_201_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_EC_Avg_201_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Soil_Temp_Avg_201_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Soil_Temp_Avg_201_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.P_Avg_201_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_P_Avg_201_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_Avg_201_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_Avg_201_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Voltage_Ratio_Avg_201_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Voltage_Ratio_Avg_201_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.VWC_Avg_201_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_VWC_Avg_201_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.EC_Avg_201_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_EC_Avg_201_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Soil_Temp_Avg_201_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Soil_Temp_Avg_201_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.P_Avg_201_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_P_Avg_201_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_Avg_201_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_Avg_201_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Voltage_Ratio_Avg_201_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Voltage_Ratio_Avg_201_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.VWC_Avg_201_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_VWC_Avg_201_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.EC_Avg_201_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_EC_Avg_201_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Soil_Temp_Avg_201_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Soil_Temp_Avg_201_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.P_Avg_201_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_P_Avg_201_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_Avg_201_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_Avg_201_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Voltage_Ratio_Avg_201_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Voltage_Ratio_Avg_201_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.VWC_Avg_202_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_VWC_Avg_202_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.EC_Avg_202_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_EC_Avg_202_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Soil_Temp_Avg_202_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Soil_Temp_Avg_202_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.P_Avg_202_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_P_Avg_202_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_Avg_202_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_Avg_202_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Voltage_Ratio_Avg_202_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Voltage_Ratio_Avg_202_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.VWC_Avg_202_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_VWC_Avg_202_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.EC_Avg_202_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_EC_Avg_202_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Soil_Temp_Avg_202_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Soil_Temp_Avg_202_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.P_Avg_202_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_P_Avg_202_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_Avg_202_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_Avg_202_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Voltage_Ratio_Avg_202_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Voltage_Ratio_Avg_202_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.VWC_Avg_202_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_VWC_Avg_202_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.EC_Avg_202_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_EC_Avg_202_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Soil_Temp_Avg_202_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Soil_Temp_Avg_202_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.P_Avg_202_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_P_Avg_202_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_Avg_202_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_Avg_202_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Voltage_Ratio_Avg_202_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Voltage_Ratio_Avg_202_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.VwcCorr_Avg_201_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_VwcCorr_Avg_201_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.VwcCorr_Avg_201_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_VwcCorr_Avg_201_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.VwcCorr_Avg_201_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_VwcCorr_Avg_201_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.VwcCorr_Avg_202_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_VwcCorr_Avg_202_10cm.describe())               
print("--------------------\n\n")
                    
print(dt1.VwcCorr_Avg_202_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_VwcCorr_Avg_202_20cm.describe())               
print("--------------------\n\n")
                    
print(dt1.VwcCorr_Avg_202_30cm.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_VwcCorr_Avg_202_30cm.describe())               
print("--------------------\n\n")
                    
                    
                




