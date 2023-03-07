# Package ID: knb-lter-jrn.210548090.29 Cataloging System:https://pasta.edirepository.org.
# Data set title: Jornada Basin LTER Cross-scale Interactions Study (CSIS) Block 15 meteorological station: Daily average soil volumetric water content data: 2013 - ongoing.
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

infile1  ="https://pasta.lternet.edu/package/data/eml/knb-lter-jrn/210548090/29/06cfd925d25e2245940ae99600eaed8e".strip() 
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
                    "Vwc_15A_Bare_10cm_Avg",     
                    "Flag_Vwc_15A_Bare_10cm_Avg",     
                    "Vwc_15A_Grass_10cm_Avg",     
                    "Flag_Vwc_15A_Grass_10cm_Avg",     
                    "Vwc_15A_Shrub_10cm_Avg",     
                    "Flag_Vwc_15A_Shrub_10cm_Avg",     
                    "Vwc_15B_Bare_10cm_Avg",     
                    "Flag_Vwc_15B_Bare_10cm_Avg",     
                    "Vwc_15B_Grass_10cm_Avg",     
                    "Flag_Vwc_15B_Grass_10cm_Avg",     
                    "Vwc_15B_Shrub_10cm_Avg",     
                    "Flag_Vwc_15B_Shrub_10cm_Avg",     
                    "Vwc_15C_Bare_10cm_Avg",     
                    "Flag_Vwc_15C_Bare_10cm_Avg",     
                    "Vwc_15C_Grass_10cm_Avg",     
                    "Flag_Vwc_15C_Grass_10cm_Avg",     
                    "Vwc_15C_Shrub_10cm_Avg",     
                    "Flag_Vwc_15C_Shrub_10cm_Avg",     
                    "Vwc_15D_Bare_10cm_Avg",     
                    "Flag_Vwc_15D_Bare_10cm_Avg",     
                    "Vwc_15D_Grass_10cm_Avg",     
                    "Flag_Vwc_15D_Grass_10cm_Avg",     
                    "Vwc_15D_Shrub_10cm_Avg",     
                    "Flag_Vwc_15D_Shrub_10cm_Avg",     
                    "Ec_15A_Bare_10cm_Avg",     
                    "Flag_Ec_15A_Bare_10cm_Avg",     
                    "Ec_15A_Grass_10cm_Avg",     
                    "Flag_Ec_15A_Grass_10cm_Avg",     
                    "Ec_15A_Shrub_10cm_Avg",     
                    "Flag_Ec_15A_Shrub_10cm_Avg",     
                    "Ec_15B_Bare_10cm_Avg",     
                    "Flag_Ec_15B_Bare_10cm_Avg",     
                    "Ec_15B_Grass_10cm_Avg",     
                    "Flag_Ec_15B_Grass_10cm_Avg",     
                    "Ec_15B_Shrub_10cm_Avg",     
                    "Flag_Ec_15B_Shrub_10cm_Avg",     
                    "Ec_15C_Bare_10cm_Avg",     
                    "Flag_Ec_15C_Bare_10cm_Avg",     
                    "Ec_15C_Grass_10cm_Avg",     
                    "Flag_Ec_15C_Grass_10cm_Avg",     
                    "Ec_15C_Shrub_10cm_Avg",     
                    "Flag_Ec_15C_Shrub_10cm_Avg",     
                    "Ec_15D_Bare_10cm_Avg",     
                    "Flag_Ec_15D_Bare_10cm_Avg",     
                    "Ec_15D_Grass_10cm_Avg",     
                    "Flag_Ec_15D_Grass_10cm_Avg",     
                    "Ec_15D_Shrub_10cm_Avg",     
                    "Flag_Ec_15D_Shrub_10cm_Avg",     
                    "Tsoil_15A_Bare_10cm_Avg",     
                    "Flag_Tsoil_15A_Bare_10cm_Avg",     
                    "Tsoil_15A_Grass_10cm_Avg",     
                    "Flag_Tsoil_15A_Grass_10cm_Avg",     
                    "Tsoil_15A_Shrub_10cm_Avg",     
                    "Flag_Tsoil_15A_Shrub_10cm_Avg",     
                    "Tsoil_15B_Bare_10cm_Avg",     
                    "Flag_Tsoil_15B_Bare_10cm_Avg",     
                    "Tsoil_15B_Grass_10cm_Avg",     
                    "Flag_Tsoil_15B_Grass_10cm_Avg",     
                    "Tsoil_15B_Shrub_10cm_Avg",     
                    "Flag_Tsoil_15B_Shrub_10cm_Avg",     
                    "Tsoil_15C_Bare_10cm_Avg",     
                    "Flag_Tsoil_15C_Bare_10cm_Avg",     
                    "Tsoil_15C_Grass_10cm_Avg",     
                    "Flag_Tsoil_15C_Grass_10cm_Avg",     
                    "Tsoil_15C_Shrub_10cm_Avg",     
                    "Flag_Tsoil_15C_Shrub_10cm_Avg",     
                    "Tsoil_15D_Bare_10cm_Avg",     
                    "Flag_Tsoil_15D_Bare_10cm_Avg",     
                    "Tsoil_15D_Grass_10cm_Avg",     
                    "Flag_Tsoil_15D_Grass_10cm_Avg",     
                    "Tsoil_15D_Shrub_10cm_Avg",     
                    "Flag_Tsoil_15D_Shrub_10cm_Avg",     
                    "Perm_15A_Bare_10cm_Avg",     
                    "Flag_Perm_15A_Bare_10cm_Avg",     
                    "Perm_15A_Grass_10cm_Avg",     
                    "Flag_Perm_15A_Grass_10cm_Avg",     
                    "Perm_15A_Shrub_10cm_Avg",     
                    "Flag_Perm_15A_Shrub_10cm_Avg",     
                    "Perm_15B_Bare_10cm_Avg",     
                    "Flag_Perm_15B_Bare_10cm_Avg",     
                    "Perm_15B_Grass_10cm_Avg",     
                    "Flag_Perm_15B_Grass_10cm_Avg",     
                    "Perm_15B_Shrub_10cm_Avg",     
                    "Flag_Perm_15B_Shrub_10cm_Avg",     
                    "Perm_15C_Bare_10cm_Avg",     
                    "Flag_Perm_15C_Bare_10cm_Avg",     
                    "Perm_15C_Grass_10cm_Avg",     
                    "Flag_Perm_15C_Grass_10cm_Avg",     
                    "Perm_15C_Shrub_10cm_Avg",     
                    "Flag_Perm_15C_Shrub_10cm_Avg",     
                    "Perm_15D_Bare_10cm_Avg",     
                    "Flag_Perm_15D_Bare_10cm_Avg",     
                    "Perm_15D_Grass_10cm_Avg",     
                    "Flag_Perm_15D_Grass_10cm_Avg",     
                    "Perm_15D_Shrub_10cm_Avg",     
                    "Flag_Perm_15D_Shrub_10cm_Avg",     
                    "Period_15A_Bare_10cm_Avg",     
                    "Flag_Period_15A_Bare_10cm_Avg",     
                    "Period_15A_Grass_10cm_Avg",     
                    "Flag_Period_15A_Grass_10cm_Avg",     
                    "Period_15A_Shrub_10cm_Avg",     
                    "Flag_Period_15A_Shrub_10cm_Avg",     
                    "Period_15B_Bare_10cm_Avg",     
                    "Flag_Period_15B_Bare_10cm_Avg",     
                    "Period_15B_Grass_10cm_Avg",     
                    "Flag_Period_15B_Grass_10cm_Avg",     
                    "Period_15B_Shrub_10cm_Avg",     
                    "Flag_Period_15B_Shrub_10cm_Avg",     
                    "Period_15C_Bare_10cm_Avg",     
                    "Flag_Period_15C_Bare_10cm_Avg",     
                    "Period_15C_Grass_10cm_Avg",     
                    "Flag_Period_15C_Grass_10cm_Avg",     
                    "Period_15C_Shrub_10cm_Avg",     
                    "Flag_Period_15C_Shrub_10cm_Avg",     
                    "Period_15D_Bare_10cm_Avg",     
                    "Flag_Period_15D_Bare_10cm_Avg",     
                    "Period_15D_Grass_10cm_Avg",     
                    "Flag_Period_15D_Grass_10cm_Avg",     
                    "Period_15D_Shrub_10cm_Avg",     
                    "Flag_Period_15D_Shrub_10cm_Avg",     
                    "Vratio_15A_Bare_10cm_Avg",     
                    "Flag_Vratio_15A_Bare_10cm_Avg",     
                    "Vratio_15A_Grass_10cm_Avg",     
                    "Flag_Vratio_15A_Grass_10cm_Avg",     
                    "Vratio_15A_Shrub_10cm_Avg",     
                    "Flag_Vratio_15A_Shrub_10cm_Avg",     
                    "Vratio_15B_Bare_10cm_Avg",     
                    "Flag_Vratio_15B_Bare_10cm_Avg",     
                    "Vratio_15B_Grass_10cm_Avg",     
                    "Flag_Vratio_15B_Grass_10cm_Avg",     
                    "Vratio_15B_Shrub_10cm_Avg",     
                    "Flag_Vratio_15B_Shrub_10cm_Avg",     
                    "Vratio_15C_Bare_10cm_Avg",     
                    "Flag_Vratio_15C_Bare_10cm_Avg",     
                    "Vratio_15C_Grass_10cm_Avg",     
                    "Flag_Vratio_15C_Grass_10cm_Avg",     
                    "Vratio_15C_Shrub_10cm_Avg",     
                    "Flag_Vratio_15C_Shrub_10cm_Avg",     
                    "Vratio_15D_Bare_10cm_Avg",     
                    "Flag_Vratio_15D_Bare_10cm_Avg",     
                    "Vratio_15D_Grass_10cm_Avg",     
                    "Flag_Vratio_15D_Grass_10cm_Avg",     
                    "Vratio_15D_Shrub_10cm_Avg",     
                    "Flag_Vratio_15D_Shrub_10cm_Avg"    ]
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
#             'Vwc_15A_Bare_10cm_Avg':'float' ,  
#             'Flag_Vwc_15A_Bare_10cm_Avg':'str' , 
#             'Vwc_15A_Grass_10cm_Avg':'float' ,  
#             'Flag_Vwc_15A_Grass_10cm_Avg':'str' , 
#             'Vwc_15A_Shrub_10cm_Avg':'float' ,  
#             'Flag_Vwc_15A_Shrub_10cm_Avg':'str' , 
#             'Vwc_15B_Bare_10cm_Avg':'float' ,  
#             'Flag_Vwc_15B_Bare_10cm_Avg':'str' , 
#             'Vwc_15B_Grass_10cm_Avg':'float' ,  
#             'Flag_Vwc_15B_Grass_10cm_Avg':'str' , 
#             'Vwc_15B_Shrub_10cm_Avg':'float' ,  
#             'Flag_Vwc_15B_Shrub_10cm_Avg':'str' , 
#             'Vwc_15C_Bare_10cm_Avg':'float' ,  
#             'Flag_Vwc_15C_Bare_10cm_Avg':'str' , 
#             'Vwc_15C_Grass_10cm_Avg':'float' ,  
#             'Flag_Vwc_15C_Grass_10cm_Avg':'str' , 
#             'Vwc_15C_Shrub_10cm_Avg':'float' ,  
#             'Flag_Vwc_15C_Shrub_10cm_Avg':'str' , 
#             'Vwc_15D_Bare_10cm_Avg':'float' ,  
#             'Flag_Vwc_15D_Bare_10cm_Avg':'str' , 
#             'Vwc_15D_Grass_10cm_Avg':'float' ,  
#             'Flag_Vwc_15D_Grass_10cm_Avg':'str' , 
#             'Vwc_15D_Shrub_10cm_Avg':'float' ,  
#             'Flag_Vwc_15D_Shrub_10cm_Avg':'str' , 
#             'Ec_15A_Bare_10cm_Avg':'float' ,  
#             'Flag_Ec_15A_Bare_10cm_Avg':'str' , 
#             'Ec_15A_Grass_10cm_Avg':'float' ,  
#             'Flag_Ec_15A_Grass_10cm_Avg':'str' , 
#             'Ec_15A_Shrub_10cm_Avg':'float' ,  
#             'Flag_Ec_15A_Shrub_10cm_Avg':'str' , 
#             'Ec_15B_Bare_10cm_Avg':'float' ,  
#             'Flag_Ec_15B_Bare_10cm_Avg':'str' , 
#             'Ec_15B_Grass_10cm_Avg':'float' ,  
#             'Flag_Ec_15B_Grass_10cm_Avg':'str' , 
#             'Ec_15B_Shrub_10cm_Avg':'float' ,  
#             'Flag_Ec_15B_Shrub_10cm_Avg':'str' , 
#             'Ec_15C_Bare_10cm_Avg':'float' ,  
#             'Flag_Ec_15C_Bare_10cm_Avg':'str' , 
#             'Ec_15C_Grass_10cm_Avg':'float' ,  
#             'Flag_Ec_15C_Grass_10cm_Avg':'str' , 
#             'Ec_15C_Shrub_10cm_Avg':'float' ,  
#             'Flag_Ec_15C_Shrub_10cm_Avg':'str' , 
#             'Ec_15D_Bare_10cm_Avg':'float' ,  
#             'Flag_Ec_15D_Bare_10cm_Avg':'str' , 
#             'Ec_15D_Grass_10cm_Avg':'float' ,  
#             'Flag_Ec_15D_Grass_10cm_Avg':'str' , 
#             'Ec_15D_Shrub_10cm_Avg':'float' ,  
#             'Flag_Ec_15D_Shrub_10cm_Avg':'str' , 
#             'Tsoil_15A_Bare_10cm_Avg':'float' ,  
#             'Flag_Tsoil_15A_Bare_10cm_Avg':'str' , 
#             'Tsoil_15A_Grass_10cm_Avg':'float' ,  
#             'Flag_Tsoil_15A_Grass_10cm_Avg':'str' , 
#             'Tsoil_15A_Shrub_10cm_Avg':'float' ,  
#             'Flag_Tsoil_15A_Shrub_10cm_Avg':'str' , 
#             'Tsoil_15B_Bare_10cm_Avg':'float' ,  
#             'Flag_Tsoil_15B_Bare_10cm_Avg':'str' , 
#             'Tsoil_15B_Grass_10cm_Avg':'float' ,  
#             'Flag_Tsoil_15B_Grass_10cm_Avg':'str' , 
#             'Tsoil_15B_Shrub_10cm_Avg':'float' ,  
#             'Flag_Tsoil_15B_Shrub_10cm_Avg':'str' , 
#             'Tsoil_15C_Bare_10cm_Avg':'float' ,  
#             'Flag_Tsoil_15C_Bare_10cm_Avg':'str' , 
#             'Tsoil_15C_Grass_10cm_Avg':'float' ,  
#             'Flag_Tsoil_15C_Grass_10cm_Avg':'str' , 
#             'Tsoil_15C_Shrub_10cm_Avg':'float' ,  
#             'Flag_Tsoil_15C_Shrub_10cm_Avg':'str' , 
#             'Tsoil_15D_Bare_10cm_Avg':'float' ,  
#             'Flag_Tsoil_15D_Bare_10cm_Avg':'str' , 
#             'Tsoil_15D_Grass_10cm_Avg':'float' ,  
#             'Flag_Tsoil_15D_Grass_10cm_Avg':'str' , 
#             'Tsoil_15D_Shrub_10cm_Avg':'float' ,  
#             'Flag_Tsoil_15D_Shrub_10cm_Avg':'str' , 
#             'Perm_15A_Bare_10cm_Avg':'float' ,  
#             'Flag_Perm_15A_Bare_10cm_Avg':'str' , 
#             'Perm_15A_Grass_10cm_Avg':'float' ,  
#             'Flag_Perm_15A_Grass_10cm_Avg':'str' , 
#             'Perm_15A_Shrub_10cm_Avg':'float' ,  
#             'Flag_Perm_15A_Shrub_10cm_Avg':'str' , 
#             'Perm_15B_Bare_10cm_Avg':'float' ,  
#             'Flag_Perm_15B_Bare_10cm_Avg':'str' , 
#             'Perm_15B_Grass_10cm_Avg':'float' ,  
#             'Flag_Perm_15B_Grass_10cm_Avg':'str' , 
#             'Perm_15B_Shrub_10cm_Avg':'float' ,  
#             'Flag_Perm_15B_Shrub_10cm_Avg':'str' , 
#             'Perm_15C_Bare_10cm_Avg':'float' ,  
#             'Flag_Perm_15C_Bare_10cm_Avg':'str' , 
#             'Perm_15C_Grass_10cm_Avg':'float' ,  
#             'Flag_Perm_15C_Grass_10cm_Avg':'str' , 
#             'Perm_15C_Shrub_10cm_Avg':'float' ,  
#             'Flag_Perm_15C_Shrub_10cm_Avg':'str' , 
#             'Perm_15D_Bare_10cm_Avg':'float' ,  
#             'Flag_Perm_15D_Bare_10cm_Avg':'str' , 
#             'Perm_15D_Grass_10cm_Avg':'float' ,  
#             'Flag_Perm_15D_Grass_10cm_Avg':'str' , 
#             'Perm_15D_Shrub_10cm_Avg':'float' ,  
#             'Flag_Perm_15D_Shrub_10cm_Avg':'str' , 
#             'Period_15A_Bare_10cm_Avg':'float' ,  
#             'Flag_Period_15A_Bare_10cm_Avg':'str' , 
#             'Period_15A_Grass_10cm_Avg':'float' ,  
#             'Flag_Period_15A_Grass_10cm_Avg':'str' , 
#             'Period_15A_Shrub_10cm_Avg':'float' ,  
#             'Flag_Period_15A_Shrub_10cm_Avg':'str' , 
#             'Period_15B_Bare_10cm_Avg':'float' ,  
#             'Flag_Period_15B_Bare_10cm_Avg':'str' , 
#             'Period_15B_Grass_10cm_Avg':'float' ,  
#             'Flag_Period_15B_Grass_10cm_Avg':'str' , 
#             'Period_15B_Shrub_10cm_Avg':'float' ,  
#             'Flag_Period_15B_Shrub_10cm_Avg':'str' , 
#             'Period_15C_Bare_10cm_Avg':'float' ,  
#             'Flag_Period_15C_Bare_10cm_Avg':'str' , 
#             'Period_15C_Grass_10cm_Avg':'float' ,  
#             'Flag_Period_15C_Grass_10cm_Avg':'str' , 
#             'Period_15C_Shrub_10cm_Avg':'float' ,  
#             'Flag_Period_15C_Shrub_10cm_Avg':'str' , 
#             'Period_15D_Bare_10cm_Avg':'float' ,  
#             'Flag_Period_15D_Bare_10cm_Avg':'str' , 
#             'Period_15D_Grass_10cm_Avg':'float' ,  
#             'Flag_Period_15D_Grass_10cm_Avg':'str' , 
#             'Period_15D_Shrub_10cm_Avg':'float' ,  
#             'Flag_Period_15D_Shrub_10cm_Avg':'str' , 
#             'Vratio_15A_Bare_10cm_Avg':'float' ,  
#             'Flag_Vratio_15A_Bare_10cm_Avg':'str' , 
#             'Vratio_15A_Grass_10cm_Avg':'float' ,  
#             'Flag_Vratio_15A_Grass_10cm_Avg':'str' , 
#             'Vratio_15A_Shrub_10cm_Avg':'float' ,  
#             'Flag_Vratio_15A_Shrub_10cm_Avg':'str' , 
#             'Vratio_15B_Bare_10cm_Avg':'float' ,  
#             'Flag_Vratio_15B_Bare_10cm_Avg':'str' , 
#             'Vratio_15B_Grass_10cm_Avg':'float' ,  
#             'Flag_Vratio_15B_Grass_10cm_Avg':'str' , 
#             'Vratio_15B_Shrub_10cm_Avg':'float' ,  
#             'Flag_Vratio_15B_Shrub_10cm_Avg':'str' , 
#             'Vratio_15C_Bare_10cm_Avg':'float' ,  
#             'Flag_Vratio_15C_Bare_10cm_Avg':'str' , 
#             'Vratio_15C_Grass_10cm_Avg':'float' ,  
#             'Flag_Vratio_15C_Grass_10cm_Avg':'str' , 
#             'Vratio_15C_Shrub_10cm_Avg':'float' ,  
#             'Flag_Vratio_15C_Shrub_10cm_Avg':'str' , 
#             'Vratio_15D_Bare_10cm_Avg':'float' ,  
#             'Flag_Vratio_15D_Bare_10cm_Avg':'str' , 
#             'Vratio_15D_Grass_10cm_Avg':'float' ,  
#             'Flag_Vratio_15D_Grass_10cm_Avg':'str' , 
#             'Vratio_15D_Shrub_10cm_Avg':'float' ,  
#             'Flag_Vratio_15D_Shrub_10cm_Avg':'str'  
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
                  'Vwc_15A_Bare_10cm_Avg':[
                          'NaN',],
                  'Vwc_15A_Grass_10cm_Avg':[
                          'NaN',],
                  'Vwc_15A_Shrub_10cm_Avg':[
                          'NaN',],
                  'Vwc_15B_Bare_10cm_Avg':[
                          'NaN',],
                  'Vwc_15B_Grass_10cm_Avg':[
                          'NaN',],
                  'Vwc_15B_Shrub_10cm_Avg':[
                          'NaN',],
                  'Vwc_15C_Bare_10cm_Avg':[
                          'NaN',],
                  'Vwc_15C_Grass_10cm_Avg':[
                          'NaN',],
                  'Vwc_15C_Shrub_10cm_Avg':[
                          'NaN',],
                  'Vwc_15D_Bare_10cm_Avg':[
                          'NaN',],
                  'Vwc_15D_Grass_10cm_Avg':[
                          'NaN',],
                  'Vwc_15D_Shrub_10cm_Avg':[
                          'NaN',],
                  'Ec_15A_Bare_10cm_Avg':[
                          'NaN',],
                  'Ec_15A_Grass_10cm_Avg':[
                          'NaN',],
                  'Ec_15A_Shrub_10cm_Avg':[
                          'NaN',],
                  'Ec_15B_Bare_10cm_Avg':[
                          'NaN',],
                  'Ec_15B_Grass_10cm_Avg':[
                          'NaN',],
                  'Ec_15B_Shrub_10cm_Avg':[
                          'NaN',],
                  'Ec_15C_Bare_10cm_Avg':[
                          'NaN',],
                  'Ec_15C_Grass_10cm_Avg':[
                          'NaN',],
                  'Ec_15C_Shrub_10cm_Avg':[
                          'NaN',],
                  'Ec_15D_Bare_10cm_Avg':[
                          'NaN',],
                  'Ec_15D_Grass_10cm_Avg':[
                          'NaN',],
                  'Ec_15D_Shrub_10cm_Avg':[
                          'NaN',],
                  'Tsoil_15A_Bare_10cm_Avg':[
                          'NaN',],
                  'Tsoil_15A_Grass_10cm_Avg':[
                          'NaN',],
                  'Tsoil_15A_Shrub_10cm_Avg':[
                          'NaN',],
                  'Tsoil_15B_Bare_10cm_Avg':[
                          'NaN',],
                  'Tsoil_15B_Grass_10cm_Avg':[
                          'NaN',],
                  'Tsoil_15B_Shrub_10cm_Avg':[
                          'NaN',],
                  'Tsoil_15C_Bare_10cm_Avg':[
                          'NaN',],
                  'Tsoil_15C_Grass_10cm_Avg':[
                          'NaN',],
                  'Tsoil_15C_Shrub_10cm_Avg':[
                          'NaN',],
                  'Tsoil_15D_Bare_10cm_Avg':[
                          'NaN',],
                  'Tsoil_15D_Grass_10cm_Avg':[
                          'NaN',],
                  'Tsoil_15D_Shrub_10cm_Avg':[
                          'NaN',],
                  'Perm_15A_Bare_10cm_Avg':[
                          'NaN',],
                  'Perm_15A_Grass_10cm_Avg':[
                          'NaN',],
                  'Perm_15A_Shrub_10cm_Avg':[
                          'NaN',],
                  'Perm_15B_Bare_10cm_Avg':[
                          'NaN',],
                  'Perm_15B_Grass_10cm_Avg':[
                          'NaN',],
                  'Perm_15B_Shrub_10cm_Avg':[
                          'NaN',],
                  'Perm_15C_Bare_10cm_Avg':[
                          'NaN',],
                  'Perm_15C_Grass_10cm_Avg':[
                          'NaN',],
                  'Perm_15C_Shrub_10cm_Avg':[
                          'NaN',],
                  'Perm_15D_Bare_10cm_Avg':[
                          'NaN',],
                  'Perm_15D_Grass_10cm_Avg':[
                          'NaN',],
                  'Perm_15D_Shrub_10cm_Avg':[
                          'NaN',],
                  'Period_15A_Bare_10cm_Avg':[
                          'NaN',],
                  'Period_15A_Grass_10cm_Avg':[
                          'NaN',],
                  'Period_15A_Shrub_10cm_Avg':[
                          'NaN',],
                  'Period_15B_Bare_10cm_Avg':[
                          'NaN',],
                  'Period_15B_Grass_10cm_Avg':[
                          'NaN',],
                  'Period_15B_Shrub_10cm_Avg':[
                          'NaN',],
                  'Period_15C_Bare_10cm_Avg':[
                          'NaN',],
                  'Period_15C_Grass_10cm_Avg':[
                          'NaN',],
                  'Period_15C_Shrub_10cm_Avg':[
                          'NaN',],
                  'Period_15D_Bare_10cm_Avg':[
                          'NaN',],
                  'Period_15D_Grass_10cm_Avg':[
                          'NaN',],
                  'Period_15D_Shrub_10cm_Avg':[
                          'NaN',],
                  'Vratio_15A_Bare_10cm_Avg':[
                          'NaN',],
                  'Vratio_15A_Grass_10cm_Avg':[
                          'NaN',],
                  'Vratio_15A_Shrub_10cm_Avg':[
                          'NaN',],
                  'Vratio_15B_Bare_10cm_Avg':[
                          'NaN',],
                  'Vratio_15B_Grass_10cm_Avg':[
                          'NaN',],
                  'Vratio_15B_Shrub_10cm_Avg':[
                          'NaN',],
                  'Vratio_15C_Bare_10cm_Avg':[
                          'NaN',],
                  'Vratio_15C_Grass_10cm_Avg':[
                          'NaN',],
                  'Vratio_15C_Shrub_10cm_Avg':[
                          'NaN',],
                  'Vratio_15D_Bare_10cm_Avg':[
                          'NaN',],
                  'Vratio_15D_Grass_10cm_Avg':[
                          'NaN',],
                  'Vratio_15D_Shrub_10cm_Avg':[
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
dt1.Vwc_15A_Bare_10cm_Avg=pd.to_numeric(dt1.Vwc_15A_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_15A_Bare_10cm_Avg=dt1.Flag_Vwc_15A_Bare_10cm_Avg.astype('category') 
dt1.Vwc_15A_Grass_10cm_Avg=pd.to_numeric(dt1.Vwc_15A_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_15A_Grass_10cm_Avg=dt1.Flag_Vwc_15A_Grass_10cm_Avg.astype('category') 
dt1.Vwc_15A_Shrub_10cm_Avg=pd.to_numeric(dt1.Vwc_15A_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_15A_Shrub_10cm_Avg=dt1.Flag_Vwc_15A_Shrub_10cm_Avg.astype('category') 
dt1.Vwc_15B_Bare_10cm_Avg=pd.to_numeric(dt1.Vwc_15B_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_15B_Bare_10cm_Avg=dt1.Flag_Vwc_15B_Bare_10cm_Avg.astype('category') 
dt1.Vwc_15B_Grass_10cm_Avg=pd.to_numeric(dt1.Vwc_15B_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_15B_Grass_10cm_Avg=dt1.Flag_Vwc_15B_Grass_10cm_Avg.astype('category') 
dt1.Vwc_15B_Shrub_10cm_Avg=pd.to_numeric(dt1.Vwc_15B_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_15B_Shrub_10cm_Avg=dt1.Flag_Vwc_15B_Shrub_10cm_Avg.astype('category') 
dt1.Vwc_15C_Bare_10cm_Avg=pd.to_numeric(dt1.Vwc_15C_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_15C_Bare_10cm_Avg=dt1.Flag_Vwc_15C_Bare_10cm_Avg.astype('category') 
dt1.Vwc_15C_Grass_10cm_Avg=pd.to_numeric(dt1.Vwc_15C_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_15C_Grass_10cm_Avg=dt1.Flag_Vwc_15C_Grass_10cm_Avg.astype('category') 
dt1.Vwc_15C_Shrub_10cm_Avg=pd.to_numeric(dt1.Vwc_15C_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_15C_Shrub_10cm_Avg=dt1.Flag_Vwc_15C_Shrub_10cm_Avg.astype('category') 
dt1.Vwc_15D_Bare_10cm_Avg=pd.to_numeric(dt1.Vwc_15D_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_15D_Bare_10cm_Avg=dt1.Flag_Vwc_15D_Bare_10cm_Avg.astype('category') 
dt1.Vwc_15D_Grass_10cm_Avg=pd.to_numeric(dt1.Vwc_15D_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_15D_Grass_10cm_Avg=dt1.Flag_Vwc_15D_Grass_10cm_Avg.astype('category') 
dt1.Vwc_15D_Shrub_10cm_Avg=pd.to_numeric(dt1.Vwc_15D_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_15D_Shrub_10cm_Avg=dt1.Flag_Vwc_15D_Shrub_10cm_Avg.astype('category') 
dt1.Ec_15A_Bare_10cm_Avg=pd.to_numeric(dt1.Ec_15A_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_15A_Bare_10cm_Avg=dt1.Flag_Ec_15A_Bare_10cm_Avg.astype('category') 
dt1.Ec_15A_Grass_10cm_Avg=pd.to_numeric(dt1.Ec_15A_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_15A_Grass_10cm_Avg=dt1.Flag_Ec_15A_Grass_10cm_Avg.astype('category') 
dt1.Ec_15A_Shrub_10cm_Avg=pd.to_numeric(dt1.Ec_15A_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_15A_Shrub_10cm_Avg=dt1.Flag_Ec_15A_Shrub_10cm_Avg.astype('category') 
dt1.Ec_15B_Bare_10cm_Avg=pd.to_numeric(dt1.Ec_15B_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_15B_Bare_10cm_Avg=dt1.Flag_Ec_15B_Bare_10cm_Avg.astype('category') 
dt1.Ec_15B_Grass_10cm_Avg=pd.to_numeric(dt1.Ec_15B_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_15B_Grass_10cm_Avg=dt1.Flag_Ec_15B_Grass_10cm_Avg.astype('category') 
dt1.Ec_15B_Shrub_10cm_Avg=pd.to_numeric(dt1.Ec_15B_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_15B_Shrub_10cm_Avg=dt1.Flag_Ec_15B_Shrub_10cm_Avg.astype('category') 
dt1.Ec_15C_Bare_10cm_Avg=pd.to_numeric(dt1.Ec_15C_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_15C_Bare_10cm_Avg=dt1.Flag_Ec_15C_Bare_10cm_Avg.astype('category') 
dt1.Ec_15C_Grass_10cm_Avg=pd.to_numeric(dt1.Ec_15C_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_15C_Grass_10cm_Avg=dt1.Flag_Ec_15C_Grass_10cm_Avg.astype('category') 
dt1.Ec_15C_Shrub_10cm_Avg=pd.to_numeric(dt1.Ec_15C_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_15C_Shrub_10cm_Avg=dt1.Flag_Ec_15C_Shrub_10cm_Avg.astype('category') 
dt1.Ec_15D_Bare_10cm_Avg=pd.to_numeric(dt1.Ec_15D_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_15D_Bare_10cm_Avg=dt1.Flag_Ec_15D_Bare_10cm_Avg.astype('category') 
dt1.Ec_15D_Grass_10cm_Avg=pd.to_numeric(dt1.Ec_15D_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_15D_Grass_10cm_Avg=dt1.Flag_Ec_15D_Grass_10cm_Avg.astype('category') 
dt1.Ec_15D_Shrub_10cm_Avg=pd.to_numeric(dt1.Ec_15D_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_15D_Shrub_10cm_Avg=dt1.Flag_Ec_15D_Shrub_10cm_Avg.astype('category') 
dt1.Tsoil_15A_Bare_10cm_Avg=pd.to_numeric(dt1.Tsoil_15A_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_15A_Bare_10cm_Avg=dt1.Flag_Tsoil_15A_Bare_10cm_Avg.astype('category') 
dt1.Tsoil_15A_Grass_10cm_Avg=pd.to_numeric(dt1.Tsoil_15A_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_15A_Grass_10cm_Avg=dt1.Flag_Tsoil_15A_Grass_10cm_Avg.astype('category') 
dt1.Tsoil_15A_Shrub_10cm_Avg=pd.to_numeric(dt1.Tsoil_15A_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_15A_Shrub_10cm_Avg=dt1.Flag_Tsoil_15A_Shrub_10cm_Avg.astype('category') 
dt1.Tsoil_15B_Bare_10cm_Avg=pd.to_numeric(dt1.Tsoil_15B_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_15B_Bare_10cm_Avg=dt1.Flag_Tsoil_15B_Bare_10cm_Avg.astype('category') 
dt1.Tsoil_15B_Grass_10cm_Avg=pd.to_numeric(dt1.Tsoil_15B_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_15B_Grass_10cm_Avg=dt1.Flag_Tsoil_15B_Grass_10cm_Avg.astype('category') 
dt1.Tsoil_15B_Shrub_10cm_Avg=pd.to_numeric(dt1.Tsoil_15B_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_15B_Shrub_10cm_Avg=dt1.Flag_Tsoil_15B_Shrub_10cm_Avg.astype('category') 
dt1.Tsoil_15C_Bare_10cm_Avg=pd.to_numeric(dt1.Tsoil_15C_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_15C_Bare_10cm_Avg=dt1.Flag_Tsoil_15C_Bare_10cm_Avg.astype('category') 
dt1.Tsoil_15C_Grass_10cm_Avg=pd.to_numeric(dt1.Tsoil_15C_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_15C_Grass_10cm_Avg=dt1.Flag_Tsoil_15C_Grass_10cm_Avg.astype('category') 
dt1.Tsoil_15C_Shrub_10cm_Avg=pd.to_numeric(dt1.Tsoil_15C_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_15C_Shrub_10cm_Avg=dt1.Flag_Tsoil_15C_Shrub_10cm_Avg.astype('category') 
dt1.Tsoil_15D_Bare_10cm_Avg=pd.to_numeric(dt1.Tsoil_15D_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_15D_Bare_10cm_Avg=dt1.Flag_Tsoil_15D_Bare_10cm_Avg.astype('category') 
dt1.Tsoil_15D_Grass_10cm_Avg=pd.to_numeric(dt1.Tsoil_15D_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_15D_Grass_10cm_Avg=dt1.Flag_Tsoil_15D_Grass_10cm_Avg.astype('category') 
dt1.Tsoil_15D_Shrub_10cm_Avg=pd.to_numeric(dt1.Tsoil_15D_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_15D_Shrub_10cm_Avg=dt1.Flag_Tsoil_15D_Shrub_10cm_Avg.astype('category') 
dt1.Perm_15A_Bare_10cm_Avg=pd.to_numeric(dt1.Perm_15A_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_15A_Bare_10cm_Avg=dt1.Flag_Perm_15A_Bare_10cm_Avg.astype('category') 
dt1.Perm_15A_Grass_10cm_Avg=pd.to_numeric(dt1.Perm_15A_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_15A_Grass_10cm_Avg=dt1.Flag_Perm_15A_Grass_10cm_Avg.astype('category') 
dt1.Perm_15A_Shrub_10cm_Avg=pd.to_numeric(dt1.Perm_15A_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_15A_Shrub_10cm_Avg=dt1.Flag_Perm_15A_Shrub_10cm_Avg.astype('category') 
dt1.Perm_15B_Bare_10cm_Avg=pd.to_numeric(dt1.Perm_15B_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_15B_Bare_10cm_Avg=dt1.Flag_Perm_15B_Bare_10cm_Avg.astype('category') 
dt1.Perm_15B_Grass_10cm_Avg=pd.to_numeric(dt1.Perm_15B_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_15B_Grass_10cm_Avg=dt1.Flag_Perm_15B_Grass_10cm_Avg.astype('category') 
dt1.Perm_15B_Shrub_10cm_Avg=pd.to_numeric(dt1.Perm_15B_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_15B_Shrub_10cm_Avg=dt1.Flag_Perm_15B_Shrub_10cm_Avg.astype('category') 
dt1.Perm_15C_Bare_10cm_Avg=pd.to_numeric(dt1.Perm_15C_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_15C_Bare_10cm_Avg=dt1.Flag_Perm_15C_Bare_10cm_Avg.astype('category') 
dt1.Perm_15C_Grass_10cm_Avg=pd.to_numeric(dt1.Perm_15C_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_15C_Grass_10cm_Avg=dt1.Flag_Perm_15C_Grass_10cm_Avg.astype('category') 
dt1.Perm_15C_Shrub_10cm_Avg=pd.to_numeric(dt1.Perm_15C_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_15C_Shrub_10cm_Avg=dt1.Flag_Perm_15C_Shrub_10cm_Avg.astype('category') 
dt1.Perm_15D_Bare_10cm_Avg=pd.to_numeric(dt1.Perm_15D_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_15D_Bare_10cm_Avg=dt1.Flag_Perm_15D_Bare_10cm_Avg.astype('category') 
dt1.Perm_15D_Grass_10cm_Avg=pd.to_numeric(dt1.Perm_15D_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_15D_Grass_10cm_Avg=dt1.Flag_Perm_15D_Grass_10cm_Avg.astype('category') 
dt1.Perm_15D_Shrub_10cm_Avg=pd.to_numeric(dt1.Perm_15D_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_15D_Shrub_10cm_Avg=dt1.Flag_Perm_15D_Shrub_10cm_Avg.astype('category') 
dt1.Period_15A_Bare_10cm_Avg=pd.to_numeric(dt1.Period_15A_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Period_15A_Bare_10cm_Avg=dt1.Flag_Period_15A_Bare_10cm_Avg.astype('category') 
dt1.Period_15A_Grass_10cm_Avg=pd.to_numeric(dt1.Period_15A_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Period_15A_Grass_10cm_Avg=dt1.Flag_Period_15A_Grass_10cm_Avg.astype('category') 
dt1.Period_15A_Shrub_10cm_Avg=pd.to_numeric(dt1.Period_15A_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Period_15A_Shrub_10cm_Avg=dt1.Flag_Period_15A_Shrub_10cm_Avg.astype('category') 
dt1.Period_15B_Bare_10cm_Avg=pd.to_numeric(dt1.Period_15B_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Period_15B_Bare_10cm_Avg=dt1.Flag_Period_15B_Bare_10cm_Avg.astype('category') 
dt1.Period_15B_Grass_10cm_Avg=pd.to_numeric(dt1.Period_15B_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Period_15B_Grass_10cm_Avg=dt1.Flag_Period_15B_Grass_10cm_Avg.astype('category') 
dt1.Period_15B_Shrub_10cm_Avg=pd.to_numeric(dt1.Period_15B_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Period_15B_Shrub_10cm_Avg=dt1.Flag_Period_15B_Shrub_10cm_Avg.astype('category') 
dt1.Period_15C_Bare_10cm_Avg=pd.to_numeric(dt1.Period_15C_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Period_15C_Bare_10cm_Avg=dt1.Flag_Period_15C_Bare_10cm_Avg.astype('category') 
dt1.Period_15C_Grass_10cm_Avg=pd.to_numeric(dt1.Period_15C_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Period_15C_Grass_10cm_Avg=dt1.Flag_Period_15C_Grass_10cm_Avg.astype('category') 
dt1.Period_15C_Shrub_10cm_Avg=pd.to_numeric(dt1.Period_15C_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Period_15C_Shrub_10cm_Avg=dt1.Flag_Period_15C_Shrub_10cm_Avg.astype('category') 
dt1.Period_15D_Bare_10cm_Avg=pd.to_numeric(dt1.Period_15D_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Period_15D_Bare_10cm_Avg=dt1.Flag_Period_15D_Bare_10cm_Avg.astype('category') 
dt1.Period_15D_Grass_10cm_Avg=pd.to_numeric(dt1.Period_15D_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Period_15D_Grass_10cm_Avg=dt1.Flag_Period_15D_Grass_10cm_Avg.astype('category') 
dt1.Period_15D_Shrub_10cm_Avg=pd.to_numeric(dt1.Period_15D_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Period_15D_Shrub_10cm_Avg=dt1.Flag_Period_15D_Shrub_10cm_Avg.astype('category') 
dt1.Vratio_15A_Bare_10cm_Avg=pd.to_numeric(dt1.Vratio_15A_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_15A_Bare_10cm_Avg=dt1.Flag_Vratio_15A_Bare_10cm_Avg.astype('category') 
dt1.Vratio_15A_Grass_10cm_Avg=pd.to_numeric(dt1.Vratio_15A_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_15A_Grass_10cm_Avg=dt1.Flag_Vratio_15A_Grass_10cm_Avg.astype('category') 
dt1.Vratio_15A_Shrub_10cm_Avg=pd.to_numeric(dt1.Vratio_15A_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_15A_Shrub_10cm_Avg=dt1.Flag_Vratio_15A_Shrub_10cm_Avg.astype('category') 
dt1.Vratio_15B_Bare_10cm_Avg=pd.to_numeric(dt1.Vratio_15B_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_15B_Bare_10cm_Avg=dt1.Flag_Vratio_15B_Bare_10cm_Avg.astype('category') 
dt1.Vratio_15B_Grass_10cm_Avg=pd.to_numeric(dt1.Vratio_15B_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_15B_Grass_10cm_Avg=dt1.Flag_Vratio_15B_Grass_10cm_Avg.astype('category') 
dt1.Vratio_15B_Shrub_10cm_Avg=pd.to_numeric(dt1.Vratio_15B_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_15B_Shrub_10cm_Avg=dt1.Flag_Vratio_15B_Shrub_10cm_Avg.astype('category') 
dt1.Vratio_15C_Bare_10cm_Avg=pd.to_numeric(dt1.Vratio_15C_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_15C_Bare_10cm_Avg=dt1.Flag_Vratio_15C_Bare_10cm_Avg.astype('category') 
dt1.Vratio_15C_Grass_10cm_Avg=pd.to_numeric(dt1.Vratio_15C_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_15C_Grass_10cm_Avg=dt1.Flag_Vratio_15C_Grass_10cm_Avg.astype('category') 
dt1.Vratio_15C_Shrub_10cm_Avg=pd.to_numeric(dt1.Vratio_15C_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_15C_Shrub_10cm_Avg=dt1.Flag_Vratio_15C_Shrub_10cm_Avg.astype('category') 
dt1.Vratio_15D_Bare_10cm_Avg=pd.to_numeric(dt1.Vratio_15D_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_15D_Bare_10cm_Avg=dt1.Flag_Vratio_15D_Bare_10cm_Avg.astype('category') 
dt1.Vratio_15D_Grass_10cm_Avg=pd.to_numeric(dt1.Vratio_15D_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_15D_Grass_10cm_Avg=dt1.Flag_Vratio_15D_Grass_10cm_Avg.astype('category') 
dt1.Vratio_15D_Shrub_10cm_Avg=pd.to_numeric(dt1.Vratio_15D_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_15D_Shrub_10cm_Avg=dt1.Flag_Vratio_15D_Shrub_10cm_Avg.astype('category') 
      
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
                    
print(dt1.SiteID.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_15A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_15A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_15A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_15A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_15A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_15A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_15B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_15B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_15B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_15B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_15B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_15B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_15C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_15C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_15C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_15C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_15C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_15C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_15D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_15D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_15D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_15D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_15D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_15D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_15A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_15A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_15A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_15A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_15A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_15A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_15B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_15B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_15B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_15B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_15B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_15B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_15C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_15C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_15C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_15C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_15C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_15C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_15D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_15D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_15D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_15D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_15D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_15D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_15A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_15A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_15A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_15A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_15A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_15A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_15B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_15B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_15B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_15B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_15B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_15B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_15C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_15C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_15C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_15C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_15C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_15C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_15D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_15D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_15D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_15D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_15D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_15D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_15A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_15A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_15A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_15A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_15A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_15A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_15B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_15B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_15B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_15B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_15B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_15B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_15C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_15C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_15C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_15C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_15C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_15C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_15D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_15D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_15D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_15D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_15D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_15D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_15A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_15A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_15A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_15A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_15A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_15A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_15B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_15B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_15B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_15B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_15B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_15B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_15C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_15C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_15C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_15C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_15C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_15C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_15D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_15D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_15D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_15D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_15D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_15D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_15A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_15A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_15A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_15A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_15A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_15A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_15B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_15B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_15B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_15B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_15B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_15B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_15C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_15C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_15C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_15C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_15C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_15C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_15D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_15D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_15D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_15D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_15D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_15D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
                    
                




