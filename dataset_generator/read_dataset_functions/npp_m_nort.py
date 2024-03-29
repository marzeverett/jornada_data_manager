# Package ID: knb-lter-jrn.210437052.33 Cataloging System:https://pasta.edirepository.org.
# Data set title: Jornada Basin LTER: Wireless meteorological station at NPP M-NORT site: Daily summary data:  2013 - ongoing.
# Data set creator:  John Anderson - JRN LTER 
# Contact:   Data Manager - JRN-LTER Information Manager   - datamanager.jrn.lter@gmail.com
# Stylesheet v1.0 for metadata conversion into program: John H. Porter, Univ. Virginia, jporter@virginia.edu      
# 
# This program creates numbered PANDA dataframes named dt1,dt2,dt3...,
# one for each data table in the dataset. It also provides some basic
# summaries of their contents. NumPy and Pandas modules need to be installed
# for the program to run. 

import numpy as np
import pandas as pd 

def return_data():
        infile1  ="https://pasta.lternet.edu/package/data/eml/knb-lter-jrn/210437052/33/39e869fee79cfc16e75faa195b590f87".strip() 
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
                        "Batt_V_Min",     
                        "Flag_Batt_V_Min",     
                        "Batt_V_TMn",     
                        "Ptemp_C_Avg",     
                        "Flag_Ptemp_C_Avg",     
                        "Air_TempC_Avg",     
                        "Flag_Air_TempC_Avg",     
                        "Air_TempC_Max",     
                        "Flag_Air_TempC_Max",     
                        "Air_TempC_Min",     
                        "Flag_Air_TempC_Min",     
                        "Relative_Humidity_Avg",     
                        "Flag_Relative_Humidity_Avg",     
                        "Relative_Humidity_Max",     
                        "Flag_Relative_Humidity_Max",     
                        "Relative_Humidity_Min",     
                        "Flag_Relative_Humidity_Min",     
                        "Ppt_mm_Tot",     
                        "Flag_Ppt_mm_Tot"    ]
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
        #             'Batt_V_Min':'float' ,  
        #             'Flag_Batt_V_Min':'str' , 
        #             'Batt_V_TMn':'str' , 
        #             'Ptemp_C_Avg':'float' ,  
        #             'Flag_Ptemp_C_Avg':'str' , 
        #             'Air_TempC_Avg':'float' ,  
        #             'Flag_Air_TempC_Avg':'str' , 
        #             'Air_TempC_Max':'float' ,  
        #             'Flag_Air_TempC_Max':'str' , 
        #             'Air_TempC_Min':'float' ,  
        #             'Flag_Air_TempC_Min':'str' , 
        #             'Relative_Humidity_Avg':'float' ,  
        #             'Flag_Relative_Humidity_Avg':'str' , 
        #             'Relative_Humidity_Max':'float' ,  
        #             'Flag_Relative_Humidity_Max':'str' , 
        #             'Relative_Humidity_Min':'float' ,  
        #             'Flag_Relative_Humidity_Min':'str' , 
        #             'Ppt_mm_Tot':'float' ,  
        #             'Flag_Ppt_mm_Tot':'str'  
        #        }
                ,parse_dates=[
                                'Date',
                                'Batt_V_TMn',
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
                        'Batt_V_Min':[
                                'NaN',],
                        'Ptemp_C_Avg':[
                                'NaN',],
                        'Air_TempC_Avg':[
                                'NaN',],
                        'Air_TempC_Max':[
                                'NaN',],
                        'Air_TempC_Min':[
                                'NaN',],
                        'Relative_Humidity_Avg':[
                                'NaN',],
                        'Relative_Humidity_Max':[
                                'NaN',],
                        'Relative_Humidity_Min':[
                                'NaN',],
                        'Ppt_mm_Tot':[
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
        dt1.Batt_V_Min=pd.to_numeric(dt1.Batt_V_Min,errors='coerce')  
        dt1.Flag_Batt_V_Min=dt1.Flag_Batt_V_Min.astype('category') 
        # Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
        # This new column is added to the dataframe but does not show up in automated summaries below. 
        dt1=dt1.assign(Batt_V_TMn_datetime=pd.to_datetime(dt1.Batt_V_TMn,errors='coerce')) 
        dt1.Ptemp_C_Avg=pd.to_numeric(dt1.Ptemp_C_Avg,errors='coerce')  
        dt1.Flag_Ptemp_C_Avg=dt1.Flag_Ptemp_C_Avg.astype('category') 
        dt1.Air_TempC_Avg=pd.to_numeric(dt1.Air_TempC_Avg,errors='coerce')  
        dt1.Flag_Air_TempC_Avg=dt1.Flag_Air_TempC_Avg.astype('category') 
        dt1.Air_TempC_Max=pd.to_numeric(dt1.Air_TempC_Max,errors='coerce')  
        dt1.Flag_Air_TempC_Max=dt1.Flag_Air_TempC_Max.astype('category') 
        dt1.Air_TempC_Min=pd.to_numeric(dt1.Air_TempC_Min,errors='coerce')  
        dt1.Flag_Air_TempC_Min=dt1.Flag_Air_TempC_Min.astype('category') 
        dt1.Relative_Humidity_Avg=pd.to_numeric(dt1.Relative_Humidity_Avg,errors='coerce')  
        dt1.Flag_Relative_Humidity_Avg=dt1.Flag_Relative_Humidity_Avg.astype('category') 
        dt1.Relative_Humidity_Max=pd.to_numeric(dt1.Relative_Humidity_Max,errors='coerce')  
        dt1.Flag_Relative_Humidity_Max=dt1.Flag_Relative_Humidity_Max.astype('category') 
        dt1.Relative_Humidity_Min=pd.to_numeric(dt1.Relative_Humidity_Min,errors='coerce')  
        dt1.Flag_Relative_Humidity_Min=dt1.Flag_Relative_Humidity_Min.astype('category') 
        dt1.Ppt_mm_Tot=pd.to_numeric(dt1.Ppt_mm_Tot,errors='coerce')  
        dt1.Flag_Ppt_mm_Tot=dt1.Flag_Ppt_mm_Tot.astype('category') 

        return dt1
