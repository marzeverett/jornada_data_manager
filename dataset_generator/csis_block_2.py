# Package ID: knb-lter-jrn.210548047.29 Cataloging System:https://pasta.edirepository.org.
# Data set title: Jornada Basin LTER Cross-scale Interactions Study (CSIS) Block 2 meteorological station: Daily summary data: 2013 - ongoing.
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
        infile1  ="https://pasta.lternet.edu/package/data/eml/knb-lter-jrn/210548047/29/8c51406049ed08945dbe9a1983bfdab3".strip() 
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
                        "SiteID",     
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
                        "Flag_Ppt_mm_Tot",     
                        "Ws_Mean_300cm",     
                        "Flag_Ws_Mean_300cm",     
                        "Ws_mean_Resultant_300cm",     
                        "Flag_Ws_mean_Resultant_300cm",     
                        "WinDir_mean_Resultant",     
                        "Flag_WinDir_mean_Resultant",     
                        "WinDir_Std_Dev",     
                        "Flag_WinDir_Std_Dev",     
                        "WS_ms_37cm_Avg",     
                        "Flag_WS_ms_37cm_Avg",     
                        "WS_ms_75cm_Avg",     
                        "Flag_WS_ms_75cm_Avg",     
                        "WS_ms_150cm_Avg",     
                        "Flag_WS_ms_150cm_Avg",     
                        "WS_ms_300cm_Avg",     
                        "Flag_WS_ms_300cm_Avg",     
                        "WS_ms_37cm_Max",     
                        "Flag_WS_ms_37cm_Max",     
                        "WS_ms_75cm_Max",     
                        "Flag_WS_ms_75cm_Max",     
                        "WS_ms_150cm_Max",     
                        "Flag_WS_ms_150cm_Max",     
                        "WS_ms_300cm_Max",     
                        "Flag_WS_ms_300cm_Max"    ]
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
        #             'SiteID':'str', 
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
        #             'Flag_Ppt_mm_Tot':'str' , 
        #             'Ws_Mean_300cm':'float' ,  
        #             'Flag_Ws_Mean_300cm':'str' , 
        #             'Ws_mean_Resultant_300cm':'float' ,  
        #             'Flag_Ws_mean_Resultant_300cm':'str' , 
        #             'WinDir_mean_Resultant':'float' ,  
        #             'Flag_WinDir_mean_Resultant':'str' , 
        #             'WinDir_Std_Dev':'float' ,  
        #             'Flag_WinDir_Std_Dev':'str' , 
        #             'WS_ms_37cm_Avg':'float' ,  
        #             'Flag_WS_ms_37cm_Avg':'str' , 
        #             'WS_ms_75cm_Avg':'float' ,  
        #             'Flag_WS_ms_75cm_Avg':'str' , 
        #             'WS_ms_150cm_Avg':'float' ,  
        #             'Flag_WS_ms_150cm_Avg':'str' , 
        #             'WS_ms_300cm_Avg':'float' ,  
        #             'Flag_WS_ms_300cm_Avg':'str' , 
        #             'WS_ms_37cm_Max':'float' ,  
        #             'Flag_WS_ms_37cm_Max':'str' , 
        #             'WS_ms_75cm_Max':'float' ,  
        #             'Flag_WS_ms_75cm_Max':'str' , 
        #             'WS_ms_150cm_Max':'float' ,  
        #             'Flag_WS_ms_150cm_Max':'str' , 
        #             'WS_ms_300cm_Max':'float' ,  
        #             'Flag_WS_ms_300cm_Max':'str'  
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
                                'NaN',],
                        'Ws_Mean_300cm':[
                                'NaN',],
                        'Ws_mean_Resultant_300cm':[
                                'NaN',],
                        'WinDir_mean_Resultant':[
                                'NaN',],
                        'WinDir_Std_Dev':[
                                'NaN',],
                        'WS_ms_37cm_Avg':[
                                'NaN',],
                        'WS_ms_75cm_Avg':[
                                'NaN',],
                        'WS_ms_150cm_Avg':[
                                'NaN',],
                        'WS_ms_300cm_Avg':[
                                'NaN',],
                        'WS_ms_37cm_Max':[
                                'NaN',],
                        'WS_ms_75cm_Max':[
                                'NaN',],
                        'WS_ms_150cm_Max':[
                                'NaN',],
                        'WS_ms_300cm_Max':[
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
        dt1.SiteID=str(dt1.SiteID) 
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
        dt1.Ws_Mean_300cm=pd.to_numeric(dt1.Ws_Mean_300cm,errors='coerce')  
        dt1.Flag_Ws_Mean_300cm=dt1.Flag_Ws_Mean_300cm.astype('category') 
        dt1.Ws_mean_Resultant_300cm=pd.to_numeric(dt1.Ws_mean_Resultant_300cm,errors='coerce')  
        dt1.Flag_Ws_mean_Resultant_300cm=dt1.Flag_Ws_mean_Resultant_300cm.astype('category') 
        dt1.WinDir_mean_Resultant=pd.to_numeric(dt1.WinDir_mean_Resultant,errors='coerce')  
        dt1.Flag_WinDir_mean_Resultant=dt1.Flag_WinDir_mean_Resultant.astype('category') 
        dt1.WinDir_Std_Dev=pd.to_numeric(dt1.WinDir_Std_Dev,errors='coerce')  
        dt1.Flag_WinDir_Std_Dev=dt1.Flag_WinDir_Std_Dev.astype('category') 
        dt1.WS_ms_37cm_Avg=pd.to_numeric(dt1.WS_ms_37cm_Avg,errors='coerce')  
        dt1.Flag_WS_ms_37cm_Avg=dt1.Flag_WS_ms_37cm_Avg.astype('category') 
        dt1.WS_ms_75cm_Avg=pd.to_numeric(dt1.WS_ms_75cm_Avg,errors='coerce')  
        dt1.Flag_WS_ms_75cm_Avg=dt1.Flag_WS_ms_75cm_Avg.astype('category') 
        dt1.WS_ms_150cm_Avg=pd.to_numeric(dt1.WS_ms_150cm_Avg,errors='coerce')  
        dt1.Flag_WS_ms_150cm_Avg=dt1.Flag_WS_ms_150cm_Avg.astype('category') 
        dt1.WS_ms_300cm_Avg=pd.to_numeric(dt1.WS_ms_300cm_Avg,errors='coerce')  
        dt1.Flag_WS_ms_300cm_Avg=dt1.Flag_WS_ms_300cm_Avg.astype('category') 
        dt1.WS_ms_37cm_Max=pd.to_numeric(dt1.WS_ms_37cm_Max,errors='coerce')  
        dt1.Flag_WS_ms_37cm_Max=dt1.Flag_WS_ms_37cm_Max.astype('category') 
        dt1.WS_ms_75cm_Max=pd.to_numeric(dt1.WS_ms_75cm_Max,errors='coerce')  
        dt1.Flag_WS_ms_75cm_Max=dt1.Flag_WS_ms_75cm_Max.astype('category') 
        dt1.WS_ms_150cm_Max=pd.to_numeric(dt1.WS_ms_150cm_Max,errors='coerce')  
        dt1.Flag_WS_ms_150cm_Max=dt1.Flag_WS_ms_150cm_Max.astype('category') 
        dt1.WS_ms_300cm_Max=pd.to_numeric(dt1.WS_ms_300cm_Max,errors='coerce')  
        dt1.Flag_WS_ms_300cm_Max=dt1.Flag_WS_ms_300cm_Max.astype('category') 
        
        return dt1
                    
                    
                




