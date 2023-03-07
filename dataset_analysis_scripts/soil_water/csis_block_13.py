# Package ID: knb-lter-jrn.210548088.30 Cataloging System:https://pasta.edirepository.org.
# Data set title: Jornada Basin LTER Cross-scale Interactions Study (CSIS) Block 13 meteorological station: Daily average soil volumetric water content data: 2013 - ongoing.
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

infile1  ="https://pasta.lternet.edu/package/data/eml/knb-lter-jrn/210548088/30/9e3f049653ffd9790788ea407e496ea0".strip() 
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
                    "Vwc_13A_Bare_10cm_Avg",     
                    "Flag_Vwc_13A_Bare_10cm_Avg",     
                    "Vwc_13A_Grass_10cm_Avg",     
                    "Flag_Vwc_13A_Grass_10cm_Avg",     
                    "Vwc_13A_Shrub_10cm_Avg",     
                    "Flag_Vwc_13A_Shrub_10cm_Avg",     
                    "Vwc_13B_Bare_10cm_Avg",     
                    "Flag_Vwc_13B_Bare_10cm_Avg",     
                    "Vwc_13B_Grass_10cm_Avg",     
                    "Flag_Vwc_13B_Grass_10cm_Avg",     
                    "Vwc_13B_Shrub_10cm_Avg",     
                    "Flag_Vwc_13B_Shrub_10cm_Avg",     
                    "Vwc_13C_Bare_10cm_Avg",     
                    "Flag_Vwc_13C_Bare_10cm_Avg",     
                    "Vwc_13C_Grass_10cm_Avg",     
                    "Flag_Vwc_13C_Grass_10cm_Avg",     
                    "Vwc_13C_Shrub_10cm_Avg",     
                    "Flag_Vwc_13C_Shrub_10cm_Avg",     
                    "Vwc_13D_Bare_10cm_Avg",     
                    "Flag_Vwc_13D_Bare_10cm_Avg",     
                    "Vwc_13D_Grass_10cm_Avg",     
                    "Flag_Vwc_13D_Grass_10cm_Avg",     
                    "Vwc_13D_Shrub_10cm_Avg",     
                    "Flag_Vwc_13D_Shrub_10cm_Avg",     
                    "Ec_13A_Bare_10cm_Avg",     
                    "Flag_Ec_13A_Bare_10cm_Avg",     
                    "Ec_13A_Grass_10cm_Avg",     
                    "Flag_Ec_13A_Grass_10cm_Avg",     
                    "Ec_13A_Shrub_10cm_Avg",     
                    "Flag_Ec_13A_Shrub_10cm_Avg",     
                    "Ec_13B_Bare_10cm_Avg",     
                    "Flag_Ec_13B_Bare_10cm_Avg",     
                    "Ec_13B_Grass_10cm_Avg",     
                    "Flag_Ec_13B_Grass_10cm_Avg",     
                    "Ec_13B_Shrub_10cm_Avg",     
                    "Flag_Ec_13B_Shrub_10cm_Avg",     
                    "Ec_13C_Bare_10cm_Avg",     
                    "Flag_Ec_13C_Bare_10cm_Avg",     
                    "Ec_13C_Grass_10cm_Avg",     
                    "Flag_Ec_13C_Grass_10cm_Avg",     
                    "Ec_13C_Shrub_10cm_Avg",     
                    "Flag_Ec_13C_Shrub_10cm_Avg",     
                    "Ec_13D_Bare_10cm_Avg",     
                    "Flag_Ec_13D_Bare_10cm_Avg",     
                    "Ec_13D_Grass_10cm_Avg",     
                    "Flag_Ec_13D_Grass_10cm_Avg",     
                    "Ec_13D_Shrub_10cm_Avg",     
                    "Flag_Ec_13D_Shrub_10cm_Avg",     
                    "Tsoil_13A_Bare_10cm_Avg",     
                    "Flag_Tsoil_13A_Bare_10cm_Avg",     
                    "Tsoil_13A_Grass_10cm_Avg",     
                    "Flag_Tsoil_13A_Grass_10cm_Avg",     
                    "Tsoil_13A_Shrub_10cm_Avg",     
                    "Flag_Tsoil_13A_Shrub_10cm_Avg",     
                    "Tsoil_13B_Bare_10cm_Avg",     
                    "Flag_Tsoil_13B_Bare_10cm_Avg",     
                    "Tsoil_13B_Grass_10cm_Avg",     
                    "Flag_Tsoil_13B_Grass_10cm_Avg",     
                    "Tsoil_13B_Shrub_10cm_Avg",     
                    "Flag_Tsoil_13B_Shrub_10cm_Avg",     
                    "Tsoil_13C_Bare_10cm_Avg",     
                    "Flag_Tsoil_13C_Bare_10cm_Avg",     
                    "Tsoil_13C_Grass_10cm_Avg",     
                    "Flag_Tsoil_13C_Grass_10cm_Avg",     
                    "Tsoil_13C_Shrub_10cm_Avg",     
                    "Flag_Tsoil_13C_Shrub_10cm_Avg",     
                    "Tsoil_13D_Bare_10cm_Avg",     
                    "Flag_Tsoil_13D_Bare_10cm_Avg",     
                    "Tsoil_13D_Grass_10cm_Avg",     
                    "Flag_Tsoil_13D_Grass_10cm_Avg",     
                    "Tsoil_13D_Shrub_10cm_Avg",     
                    "Flag_Tsoil_13D_Shrub_10cm_Avg",     
                    "Perm_13A_Bare_10cm_Avg",     
                    "Flag_Perm_13A_Bare_10cm_Avg",     
                    "Perm_13A_Grass_10cm_Avg",     
                    "Flag_Perm_13A_Grass_10cm_Avg",     
                    "Perm_13A_Shrub_10cm_Avg",     
                    "Flag_Perm_13A_Shrub_10cm_Avg",     
                    "Perm_13B_Bare_10cm_Avg",     
                    "Flag_Perm_13B_Bare_10cm_Avg",     
                    "Perm_13B_Grass_10cm_Avg",     
                    "Flag_Perm_13B_Grass_10cm_Avg",     
                    "Perm_13B_Shrub_10cm_Avg",     
                    "Flag_Perm_13B_Shrub_10cm_Avg",     
                    "Perm_13C_Bare_10cm_Avg",     
                    "Flag_Perm_13C_Bare_10cm_Avg",     
                    "Perm_13C_Grass_10cm_Avg",     
                    "Flag_Perm_13C_Grass_10cm_Avg",     
                    "Perm_13C_Shrub_10cm_Avg",     
                    "Flag_Perm_13C_Shrub_10cm_Avg",     
                    "Perm_13D_Bare_10cm_Avg",     
                    "Flag_Perm_13D_Bare_10cm_Avg",     
                    "Perm_13D_Grass_10cm_Avg",     
                    "Flag_Perm_13D_Grass_10cm_Avg",     
                    "Perm_13D_Shrub_10cm_Avg",     
                    "Flag_Perm_13D_Shrub_10cm_Avg",     
                    "Period_13A_Bare_10cm_Avg",     
                    "Flag_Period_13A_Bare_10cm_Avg",     
                    "Period_13A_Grass_10cm_Avg",     
                    "Flag_Period_13A_Grass_10cm_Avg",     
                    "Period_13A_Shrub_10cm_Avg",     
                    "Flag_Period_13A_Shrub_10cm_Avg",     
                    "Period_13B_Bare_10cm_Avg",     
                    "Flag_Period_13B_Bare_10cm_Avg",     
                    "Period_13B_Grass_10cm_Avg",     
                    "Flag_Period_13B_Grass_10cm_Avg",     
                    "Period_13B_Shrub_10cm_Avg",     
                    "Flag_Period_13B_Shrub_10cm_Avg",     
                    "Period_13C_Bare_10cm_Avg",     
                    "Flag_Period_13C_Bare_10cm_Avg",     
                    "Period_13C_Grass_10cm_Avg",     
                    "Flag_Period_13C_Grass_10cm_Avg",     
                    "Period_13C_Shrub_10cm_Avg",     
                    "Flag_Period_13C_Shrub_10cm_Avg",     
                    "Period_13D_Bare_10cm_Avg",     
                    "Flag_Period_13D_Bare_10cm_Avg",     
                    "Period_13D_Grass_10cm_Avg",     
                    "Flag_Period_13D_Grass_10cm_Avg",     
                    "Period_13D_Shrub_10cm_Avg",     
                    "Flag_Period_13D_Shrub_10cm_Avg",     
                    "Vratio_13A_Bare_10cm_Avg",     
                    "Flag_Vratio_13A_Bare_10cm_Avg",     
                    "Vratio_13A_Grass_10cm_Avg",     
                    "Flag_Vratio_13A_Grass_10cm_Avg",     
                    "Vratio_13A_Shrub_10cm_Avg",     
                    "Flag_Vratio_13A_Shrub_10cm_Avg",     
                    "Vratio_13B_Bare_10cm_Avg",     
                    "Flag_Vratio_13B_Bare_10cm_Avg",     
                    "Vratio_13B_Grass_10cm_Avg",     
                    "Flag_Vratio_13B_Grass_10cm_Avg",     
                    "Vratio_13B_Shrub_10cm_Avg",     
                    "Flag_Vratio_13B_Shrub_10cm_Avg",     
                    "Vratio_13C_Bare_10cm_Avg",     
                    "Flag_Vratio_13C_Bare_10cm_Avg",     
                    "Vratio_13C_Grass_10cm_Avg",     
                    "Flag_Vratio_13C_Grass_10cm_Avg",     
                    "Vratio_13C_Shrub_10cm_Avg",     
                    "Flag_Vratio_13C_Shrub_10cm_Avg",     
                    "Vratio_13D_Bare_10cm_Avg",     
                    "Flag_Vratio_13D_Bare_10cm_Avg",     
                    "Vratio_13D_Grass_10cm_Avg",     
                    "Flag_Vratio_13D_Grass_10cm_Avg",     
                    "Vratio_13D_Shrub_10cm_Avg",     
                    "Flag_Vratio_13D_Shrub_10cm_Avg"    ]
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
#             'Vwc_13A_Bare_10cm_Avg':'float' ,  
#             'Flag_Vwc_13A_Bare_10cm_Avg':'str' , 
#             'Vwc_13A_Grass_10cm_Avg':'float' ,  
#             'Flag_Vwc_13A_Grass_10cm_Avg':'str' , 
#             'Vwc_13A_Shrub_10cm_Avg':'float' ,  
#             'Flag_Vwc_13A_Shrub_10cm_Avg':'str' , 
#             'Vwc_13B_Bare_10cm_Avg':'float' ,  
#             'Flag_Vwc_13B_Bare_10cm_Avg':'str' , 
#             'Vwc_13B_Grass_10cm_Avg':'float' ,  
#             'Flag_Vwc_13B_Grass_10cm_Avg':'str' , 
#             'Vwc_13B_Shrub_10cm_Avg':'float' ,  
#             'Flag_Vwc_13B_Shrub_10cm_Avg':'str' , 
#             'Vwc_13C_Bare_10cm_Avg':'float' ,  
#             'Flag_Vwc_13C_Bare_10cm_Avg':'str' , 
#             'Vwc_13C_Grass_10cm_Avg':'float' ,  
#             'Flag_Vwc_13C_Grass_10cm_Avg':'str' , 
#             'Vwc_13C_Shrub_10cm_Avg':'float' ,  
#             'Flag_Vwc_13C_Shrub_10cm_Avg':'str' , 
#             'Vwc_13D_Bare_10cm_Avg':'float' ,  
#             'Flag_Vwc_13D_Bare_10cm_Avg':'str' , 
#             'Vwc_13D_Grass_10cm_Avg':'float' ,  
#             'Flag_Vwc_13D_Grass_10cm_Avg':'str' , 
#             'Vwc_13D_Shrub_10cm_Avg':'float' ,  
#             'Flag_Vwc_13D_Shrub_10cm_Avg':'str' , 
#             'Ec_13A_Bare_10cm_Avg':'float' ,  
#             'Flag_Ec_13A_Bare_10cm_Avg':'str' , 
#             'Ec_13A_Grass_10cm_Avg':'float' ,  
#             'Flag_Ec_13A_Grass_10cm_Avg':'str' , 
#             'Ec_13A_Shrub_10cm_Avg':'float' ,  
#             'Flag_Ec_13A_Shrub_10cm_Avg':'str' , 
#             'Ec_13B_Bare_10cm_Avg':'float' ,  
#             'Flag_Ec_13B_Bare_10cm_Avg':'str' , 
#             'Ec_13B_Grass_10cm_Avg':'float' ,  
#             'Flag_Ec_13B_Grass_10cm_Avg':'str' , 
#             'Ec_13B_Shrub_10cm_Avg':'float' ,  
#             'Flag_Ec_13B_Shrub_10cm_Avg':'str' , 
#             'Ec_13C_Bare_10cm_Avg':'float' ,  
#             'Flag_Ec_13C_Bare_10cm_Avg':'str' , 
#             'Ec_13C_Grass_10cm_Avg':'float' ,  
#             'Flag_Ec_13C_Grass_10cm_Avg':'str' , 
#             'Ec_13C_Shrub_10cm_Avg':'float' ,  
#             'Flag_Ec_13C_Shrub_10cm_Avg':'str' , 
#             'Ec_13D_Bare_10cm_Avg':'float' ,  
#             'Flag_Ec_13D_Bare_10cm_Avg':'str' , 
#             'Ec_13D_Grass_10cm_Avg':'float' ,  
#             'Flag_Ec_13D_Grass_10cm_Avg':'str' , 
#             'Ec_13D_Shrub_10cm_Avg':'float' ,  
#             'Flag_Ec_13D_Shrub_10cm_Avg':'str' , 
#             'Tsoil_13A_Bare_10cm_Avg':'float' ,  
#             'Flag_Tsoil_13A_Bare_10cm_Avg':'str' , 
#             'Tsoil_13A_Grass_10cm_Avg':'float' ,  
#             'Flag_Tsoil_13A_Grass_10cm_Avg':'str' , 
#             'Tsoil_13A_Shrub_10cm_Avg':'float' ,  
#             'Flag_Tsoil_13A_Shrub_10cm_Avg':'str' , 
#             'Tsoil_13B_Bare_10cm_Avg':'float' ,  
#             'Flag_Tsoil_13B_Bare_10cm_Avg':'str' , 
#             'Tsoil_13B_Grass_10cm_Avg':'float' ,  
#             'Flag_Tsoil_13B_Grass_10cm_Avg':'str' , 
#             'Tsoil_13B_Shrub_10cm_Avg':'float' ,  
#             'Flag_Tsoil_13B_Shrub_10cm_Avg':'str' , 
#             'Tsoil_13C_Bare_10cm_Avg':'float' ,  
#             'Flag_Tsoil_13C_Bare_10cm_Avg':'str' , 
#             'Tsoil_13C_Grass_10cm_Avg':'float' ,  
#             'Flag_Tsoil_13C_Grass_10cm_Avg':'str' , 
#             'Tsoil_13C_Shrub_10cm_Avg':'float' ,  
#             'Flag_Tsoil_13C_Shrub_10cm_Avg':'str' , 
#             'Tsoil_13D_Bare_10cm_Avg':'float' ,  
#             'Flag_Tsoil_13D_Bare_10cm_Avg':'str' , 
#             'Tsoil_13D_Grass_10cm_Avg':'float' ,  
#             'Flag_Tsoil_13D_Grass_10cm_Avg':'str' , 
#             'Tsoil_13D_Shrub_10cm_Avg':'float' ,  
#             'Flag_Tsoil_13D_Shrub_10cm_Avg':'str' , 
#             'Perm_13A_Bare_10cm_Avg':'float' ,  
#             'Flag_Perm_13A_Bare_10cm_Avg':'str' , 
#             'Perm_13A_Grass_10cm_Avg':'float' ,  
#             'Flag_Perm_13A_Grass_10cm_Avg':'str' , 
#             'Perm_13A_Shrub_10cm_Avg':'float' ,  
#             'Flag_Perm_13A_Shrub_10cm_Avg':'str' , 
#             'Perm_13B_Bare_10cm_Avg':'float' ,  
#             'Flag_Perm_13B_Bare_10cm_Avg':'str' , 
#             'Perm_13B_Grass_10cm_Avg':'float' ,  
#             'Flag_Perm_13B_Grass_10cm_Avg':'str' , 
#             'Perm_13B_Shrub_10cm_Avg':'float' ,  
#             'Flag_Perm_13B_Shrub_10cm_Avg':'str' , 
#             'Perm_13C_Bare_10cm_Avg':'float' ,  
#             'Flag_Perm_13C_Bare_10cm_Avg':'str' , 
#             'Perm_13C_Grass_10cm_Avg':'float' ,  
#             'Flag_Perm_13C_Grass_10cm_Avg':'str' , 
#             'Perm_13C_Shrub_10cm_Avg':'float' ,  
#             'Flag_Perm_13C_Shrub_10cm_Avg':'str' , 
#             'Perm_13D_Bare_10cm_Avg':'float' ,  
#             'Flag_Perm_13D_Bare_10cm_Avg':'str' , 
#             'Perm_13D_Grass_10cm_Avg':'float' ,  
#             'Flag_Perm_13D_Grass_10cm_Avg':'str' , 
#             'Perm_13D_Shrub_10cm_Avg':'float' ,  
#             'Flag_Perm_13D_Shrub_10cm_Avg':'str' , 
#             'Period_13A_Bare_10cm_Avg':'float' ,  
#             'Flag_Period_13A_Bare_10cm_Avg':'str' , 
#             'Period_13A_Grass_10cm_Avg':'float' ,  
#             'Flag_Period_13A_Grass_10cm_Avg':'str' , 
#             'Period_13A_Shrub_10cm_Avg':'float' ,  
#             'Flag_Period_13A_Shrub_10cm_Avg':'str' , 
#             'Period_13B_Bare_10cm_Avg':'float' ,  
#             'Flag_Period_13B_Bare_10cm_Avg':'str' , 
#             'Period_13B_Grass_10cm_Avg':'float' ,  
#             'Flag_Period_13B_Grass_10cm_Avg':'str' , 
#             'Period_13B_Shrub_10cm_Avg':'float' ,  
#             'Flag_Period_13B_Shrub_10cm_Avg':'str' , 
#             'Period_13C_Bare_10cm_Avg':'float' ,  
#             'Flag_Period_13C_Bare_10cm_Avg':'str' , 
#             'Period_13C_Grass_10cm_Avg':'float' ,  
#             'Flag_Period_13C_Grass_10cm_Avg':'str' , 
#             'Period_13C_Shrub_10cm_Avg':'float' ,  
#             'Flag_Period_13C_Shrub_10cm_Avg':'str' , 
#             'Period_13D_Bare_10cm_Avg':'float' ,  
#             'Flag_Period_13D_Bare_10cm_Avg':'str' , 
#             'Period_13D_Grass_10cm_Avg':'float' ,  
#             'Flag_Period_13D_Grass_10cm_Avg':'str' , 
#             'Period_13D_Shrub_10cm_Avg':'float' ,  
#             'Flag_Period_13D_Shrub_10cm_Avg':'str' , 
#             'Vratio_13A_Bare_10cm_Avg':'float' ,  
#             'Flag_Vratio_13A_Bare_10cm_Avg':'str' , 
#             'Vratio_13A_Grass_10cm_Avg':'float' ,  
#             'Flag_Vratio_13A_Grass_10cm_Avg':'str' , 
#             'Vratio_13A_Shrub_10cm_Avg':'float' ,  
#             'Flag_Vratio_13A_Shrub_10cm_Avg':'str' , 
#             'Vratio_13B_Bare_10cm_Avg':'float' ,  
#             'Flag_Vratio_13B_Bare_10cm_Avg':'str' , 
#             'Vratio_13B_Grass_10cm_Avg':'float' ,  
#             'Flag_Vratio_13B_Grass_10cm_Avg':'str' , 
#             'Vratio_13B_Shrub_10cm_Avg':'float' ,  
#             'Flag_Vratio_13B_Shrub_10cm_Avg':'str' , 
#             'Vratio_13C_Bare_10cm_Avg':'float' ,  
#             'Flag_Vratio_13C_Bare_10cm_Avg':'str' , 
#             'Vratio_13C_Grass_10cm_Avg':'float' ,  
#             'Flag_Vratio_13C_Grass_10cm_Avg':'str' , 
#             'Vratio_13C_Shrub_10cm_Avg':'float' ,  
#             'Flag_Vratio_13C_Shrub_10cm_Avg':'str' , 
#             'Vratio_13D_Bare_10cm_Avg':'float' ,  
#             'Flag_Vratio_13D_Bare_10cm_Avg':'str' , 
#             'Vratio_13D_Grass_10cm_Avg':'float' ,  
#             'Flag_Vratio_13D_Grass_10cm_Avg':'str' , 
#             'Vratio_13D_Shrub_10cm_Avg':'float' ,  
#             'Flag_Vratio_13D_Shrub_10cm_Avg':'str'  
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
                  'Vwc_13A_Bare_10cm_Avg':[
                          'NaN',],
                  'Vwc_13A_Grass_10cm_Avg':[
                          'NaN',],
                  'Vwc_13A_Shrub_10cm_Avg':[
                          'NaN',],
                  'Vwc_13B_Bare_10cm_Avg':[
                          'NaN',],
                  'Vwc_13B_Grass_10cm_Avg':[
                          'NaN',],
                  'Vwc_13B_Shrub_10cm_Avg':[
                          'NaN',],
                  'Vwc_13C_Bare_10cm_Avg':[
                          'NaN',],
                  'Vwc_13C_Grass_10cm_Avg':[
                          'NaN',],
                  'Vwc_13C_Shrub_10cm_Avg':[
                          'NaN',],
                  'Vwc_13D_Bare_10cm_Avg':[
                          'NaN',],
                  'Vwc_13D_Grass_10cm_Avg':[
                          'NaN',],
                  'Vwc_13D_Shrub_10cm_Avg':[
                          'NaN',],
                  'Ec_13A_Bare_10cm_Avg':[
                          'NaN',],
                  'Ec_13A_Grass_10cm_Avg':[
                          'NaN',],
                  'Ec_13A_Shrub_10cm_Avg':[
                          'NaN',],
                  'Ec_13B_Bare_10cm_Avg':[
                          'NaN',],
                  'Ec_13B_Grass_10cm_Avg':[
                          'NaN',],
                  'Ec_13B_Shrub_10cm_Avg':[
                          'NaN',],
                  'Ec_13C_Bare_10cm_Avg':[
                          'NaN',],
                  'Ec_13C_Grass_10cm_Avg':[
                          'NaN',],
                  'Ec_13C_Shrub_10cm_Avg':[
                          'NaN',],
                  'Ec_13D_Bare_10cm_Avg':[
                          'NaN',],
                  'Ec_13D_Grass_10cm_Avg':[
                          'NaN',],
                  'Ec_13D_Shrub_10cm_Avg':[
                          'NaN',],
                  'Tsoil_13A_Bare_10cm_Avg':[
                          'NaN',],
                  'Tsoil_13A_Grass_10cm_Avg':[
                          'NaN',],
                  'Tsoil_13A_Shrub_10cm_Avg':[
                          'NaN',],
                  'Tsoil_13B_Bare_10cm_Avg':[
                          'NaN',],
                  'Tsoil_13B_Grass_10cm_Avg':[
                          'NaN',],
                  'Tsoil_13B_Shrub_10cm_Avg':[
                          'NaN',],
                  'Tsoil_13C_Bare_10cm_Avg':[
                          'NaN',],
                  'Tsoil_13C_Grass_10cm_Avg':[
                          'NaN',],
                  'Tsoil_13C_Shrub_10cm_Avg':[
                          'NaN',],
                  'Tsoil_13D_Bare_10cm_Avg':[
                          'NaN',],
                  'Tsoil_13D_Grass_10cm_Avg':[
                          'NaN',],
                  'Tsoil_13D_Shrub_10cm_Avg':[
                          'NaN',],
                  'Perm_13A_Bare_10cm_Avg':[
                          'NaN',],
                  'Perm_13A_Grass_10cm_Avg':[
                          'NaN',],
                  'Perm_13A_Shrub_10cm_Avg':[
                          'NaN',],
                  'Perm_13B_Bare_10cm_Avg':[
                          'NaN',],
                  'Perm_13B_Grass_10cm_Avg':[
                          'NaN',],
                  'Perm_13B_Shrub_10cm_Avg':[
                          'NaN',],
                  'Perm_13C_Bare_10cm_Avg':[
                          'NaN',],
                  'Perm_13C_Grass_10cm_Avg':[
                          'NaN',],
                  'Perm_13C_Shrub_10cm_Avg':[
                          'NaN',],
                  'Perm_13D_Bare_10cm_Avg':[
                          'NaN',],
                  'Perm_13D_Grass_10cm_Avg':[
                          'NaN',],
                  'Perm_13D_Shrub_10cm_Avg':[
                          'NaN',],
                  'Period_13A_Bare_10cm_Avg':[
                          'NaN',],
                  'Period_13A_Grass_10cm_Avg':[
                          'NaN',],
                  'Period_13A_Shrub_10cm_Avg':[
                          'NaN',],
                  'Period_13B_Bare_10cm_Avg':[
                          'NaN',],
                  'Period_13B_Grass_10cm_Avg':[
                          'NaN',],
                  'Period_13B_Shrub_10cm_Avg':[
                          'NaN',],
                  'Period_13C_Bare_10cm_Avg':[
                          'NaN',],
                  'Period_13C_Grass_10cm_Avg':[
                          'NaN',],
                  'Period_13C_Shrub_10cm_Avg':[
                          'NaN',],
                  'Period_13D_Bare_10cm_Avg':[
                          'NaN',],
                  'Period_13D_Grass_10cm_Avg':[
                          'NaN',],
                  'Period_13D_Shrub_10cm_Avg':[
                          'NaN',],
                  'Vratio_13A_Bare_10cm_Avg':[
                          'NaN',],
                  'Vratio_13A_Grass_10cm_Avg':[
                          'NaN',],
                  'Vratio_13A_Shrub_10cm_Avg':[
                          'NaN',],
                  'Vratio_13B_Bare_10cm_Avg':[
                          'NaN',],
                  'Vratio_13B_Grass_10cm_Avg':[
                          'NaN',],
                  'Vratio_13B_Shrub_10cm_Avg':[
                          'NaN',],
                  'Vratio_13C_Bare_10cm_Avg':[
                          'NaN',],
                  'Vratio_13C_Grass_10cm_Avg':[
                          'NaN',],
                  'Vratio_13C_Shrub_10cm_Avg':[
                          'NaN',],
                  'Vratio_13D_Bare_10cm_Avg':[
                          'NaN',],
                  'Vratio_13D_Grass_10cm_Avg':[
                          'NaN',],
                  'Vratio_13D_Shrub_10cm_Avg':[
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
dt1.Vwc_13A_Bare_10cm_Avg=pd.to_numeric(dt1.Vwc_13A_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_13A_Bare_10cm_Avg=dt1.Flag_Vwc_13A_Bare_10cm_Avg.astype('category') 
dt1.Vwc_13A_Grass_10cm_Avg=pd.to_numeric(dt1.Vwc_13A_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_13A_Grass_10cm_Avg=dt1.Flag_Vwc_13A_Grass_10cm_Avg.astype('category') 
dt1.Vwc_13A_Shrub_10cm_Avg=pd.to_numeric(dt1.Vwc_13A_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_13A_Shrub_10cm_Avg=dt1.Flag_Vwc_13A_Shrub_10cm_Avg.astype('category') 
dt1.Vwc_13B_Bare_10cm_Avg=pd.to_numeric(dt1.Vwc_13B_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_13B_Bare_10cm_Avg=dt1.Flag_Vwc_13B_Bare_10cm_Avg.astype('category') 
dt1.Vwc_13B_Grass_10cm_Avg=pd.to_numeric(dt1.Vwc_13B_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_13B_Grass_10cm_Avg=dt1.Flag_Vwc_13B_Grass_10cm_Avg.astype('category') 
dt1.Vwc_13B_Shrub_10cm_Avg=pd.to_numeric(dt1.Vwc_13B_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_13B_Shrub_10cm_Avg=dt1.Flag_Vwc_13B_Shrub_10cm_Avg.astype('category') 
dt1.Vwc_13C_Bare_10cm_Avg=pd.to_numeric(dt1.Vwc_13C_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_13C_Bare_10cm_Avg=dt1.Flag_Vwc_13C_Bare_10cm_Avg.astype('category') 
dt1.Vwc_13C_Grass_10cm_Avg=pd.to_numeric(dt1.Vwc_13C_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_13C_Grass_10cm_Avg=dt1.Flag_Vwc_13C_Grass_10cm_Avg.astype('category') 
dt1.Vwc_13C_Shrub_10cm_Avg=pd.to_numeric(dt1.Vwc_13C_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_13C_Shrub_10cm_Avg=dt1.Flag_Vwc_13C_Shrub_10cm_Avg.astype('category') 
dt1.Vwc_13D_Bare_10cm_Avg=pd.to_numeric(dt1.Vwc_13D_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_13D_Bare_10cm_Avg=dt1.Flag_Vwc_13D_Bare_10cm_Avg.astype('category') 
dt1.Vwc_13D_Grass_10cm_Avg=pd.to_numeric(dt1.Vwc_13D_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_13D_Grass_10cm_Avg=dt1.Flag_Vwc_13D_Grass_10cm_Avg.astype('category') 
dt1.Vwc_13D_Shrub_10cm_Avg=pd.to_numeric(dt1.Vwc_13D_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_13D_Shrub_10cm_Avg=dt1.Flag_Vwc_13D_Shrub_10cm_Avg.astype('category') 
dt1.Ec_13A_Bare_10cm_Avg=pd.to_numeric(dt1.Ec_13A_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_13A_Bare_10cm_Avg=dt1.Flag_Ec_13A_Bare_10cm_Avg.astype('category') 
dt1.Ec_13A_Grass_10cm_Avg=pd.to_numeric(dt1.Ec_13A_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_13A_Grass_10cm_Avg=dt1.Flag_Ec_13A_Grass_10cm_Avg.astype('category') 
dt1.Ec_13A_Shrub_10cm_Avg=pd.to_numeric(dt1.Ec_13A_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_13A_Shrub_10cm_Avg=dt1.Flag_Ec_13A_Shrub_10cm_Avg.astype('category') 
dt1.Ec_13B_Bare_10cm_Avg=pd.to_numeric(dt1.Ec_13B_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_13B_Bare_10cm_Avg=dt1.Flag_Ec_13B_Bare_10cm_Avg.astype('category') 
dt1.Ec_13B_Grass_10cm_Avg=pd.to_numeric(dt1.Ec_13B_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_13B_Grass_10cm_Avg=dt1.Flag_Ec_13B_Grass_10cm_Avg.astype('category') 
dt1.Ec_13B_Shrub_10cm_Avg=pd.to_numeric(dt1.Ec_13B_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_13B_Shrub_10cm_Avg=dt1.Flag_Ec_13B_Shrub_10cm_Avg.astype('category') 
dt1.Ec_13C_Bare_10cm_Avg=pd.to_numeric(dt1.Ec_13C_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_13C_Bare_10cm_Avg=dt1.Flag_Ec_13C_Bare_10cm_Avg.astype('category') 
dt1.Ec_13C_Grass_10cm_Avg=pd.to_numeric(dt1.Ec_13C_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_13C_Grass_10cm_Avg=dt1.Flag_Ec_13C_Grass_10cm_Avg.astype('category') 
dt1.Ec_13C_Shrub_10cm_Avg=pd.to_numeric(dt1.Ec_13C_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_13C_Shrub_10cm_Avg=dt1.Flag_Ec_13C_Shrub_10cm_Avg.astype('category') 
dt1.Ec_13D_Bare_10cm_Avg=pd.to_numeric(dt1.Ec_13D_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_13D_Bare_10cm_Avg=dt1.Flag_Ec_13D_Bare_10cm_Avg.astype('category') 
dt1.Ec_13D_Grass_10cm_Avg=pd.to_numeric(dt1.Ec_13D_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_13D_Grass_10cm_Avg=dt1.Flag_Ec_13D_Grass_10cm_Avg.astype('category') 
dt1.Ec_13D_Shrub_10cm_Avg=pd.to_numeric(dt1.Ec_13D_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_13D_Shrub_10cm_Avg=dt1.Flag_Ec_13D_Shrub_10cm_Avg.astype('category') 
dt1.Tsoil_13A_Bare_10cm_Avg=pd.to_numeric(dt1.Tsoil_13A_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_13A_Bare_10cm_Avg=dt1.Flag_Tsoil_13A_Bare_10cm_Avg.astype('category') 
dt1.Tsoil_13A_Grass_10cm_Avg=pd.to_numeric(dt1.Tsoil_13A_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_13A_Grass_10cm_Avg=dt1.Flag_Tsoil_13A_Grass_10cm_Avg.astype('category') 
dt1.Tsoil_13A_Shrub_10cm_Avg=pd.to_numeric(dt1.Tsoil_13A_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_13A_Shrub_10cm_Avg=dt1.Flag_Tsoil_13A_Shrub_10cm_Avg.astype('category') 
dt1.Tsoil_13B_Bare_10cm_Avg=pd.to_numeric(dt1.Tsoil_13B_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_13B_Bare_10cm_Avg=dt1.Flag_Tsoil_13B_Bare_10cm_Avg.astype('category') 
dt1.Tsoil_13B_Grass_10cm_Avg=pd.to_numeric(dt1.Tsoil_13B_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_13B_Grass_10cm_Avg=dt1.Flag_Tsoil_13B_Grass_10cm_Avg.astype('category') 
dt1.Tsoil_13B_Shrub_10cm_Avg=pd.to_numeric(dt1.Tsoil_13B_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_13B_Shrub_10cm_Avg=dt1.Flag_Tsoil_13B_Shrub_10cm_Avg.astype('category') 
dt1.Tsoil_13C_Bare_10cm_Avg=pd.to_numeric(dt1.Tsoil_13C_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_13C_Bare_10cm_Avg=dt1.Flag_Tsoil_13C_Bare_10cm_Avg.astype('category') 
dt1.Tsoil_13C_Grass_10cm_Avg=pd.to_numeric(dt1.Tsoil_13C_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_13C_Grass_10cm_Avg=dt1.Flag_Tsoil_13C_Grass_10cm_Avg.astype('category') 
dt1.Tsoil_13C_Shrub_10cm_Avg=pd.to_numeric(dt1.Tsoil_13C_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_13C_Shrub_10cm_Avg=dt1.Flag_Tsoil_13C_Shrub_10cm_Avg.astype('category') 
dt1.Tsoil_13D_Bare_10cm_Avg=pd.to_numeric(dt1.Tsoil_13D_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_13D_Bare_10cm_Avg=dt1.Flag_Tsoil_13D_Bare_10cm_Avg.astype('category') 
dt1.Tsoil_13D_Grass_10cm_Avg=pd.to_numeric(dt1.Tsoil_13D_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_13D_Grass_10cm_Avg=dt1.Flag_Tsoil_13D_Grass_10cm_Avg.astype('category') 
dt1.Tsoil_13D_Shrub_10cm_Avg=pd.to_numeric(dt1.Tsoil_13D_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_13D_Shrub_10cm_Avg=dt1.Flag_Tsoil_13D_Shrub_10cm_Avg.astype('category') 
dt1.Perm_13A_Bare_10cm_Avg=pd.to_numeric(dt1.Perm_13A_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_13A_Bare_10cm_Avg=dt1.Flag_Perm_13A_Bare_10cm_Avg.astype('category') 
dt1.Perm_13A_Grass_10cm_Avg=pd.to_numeric(dt1.Perm_13A_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_13A_Grass_10cm_Avg=dt1.Flag_Perm_13A_Grass_10cm_Avg.astype('category') 
dt1.Perm_13A_Shrub_10cm_Avg=pd.to_numeric(dt1.Perm_13A_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_13A_Shrub_10cm_Avg=dt1.Flag_Perm_13A_Shrub_10cm_Avg.astype('category') 
dt1.Perm_13B_Bare_10cm_Avg=pd.to_numeric(dt1.Perm_13B_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_13B_Bare_10cm_Avg=dt1.Flag_Perm_13B_Bare_10cm_Avg.astype('category') 
dt1.Perm_13B_Grass_10cm_Avg=pd.to_numeric(dt1.Perm_13B_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_13B_Grass_10cm_Avg=dt1.Flag_Perm_13B_Grass_10cm_Avg.astype('category') 
dt1.Perm_13B_Shrub_10cm_Avg=pd.to_numeric(dt1.Perm_13B_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_13B_Shrub_10cm_Avg=dt1.Flag_Perm_13B_Shrub_10cm_Avg.astype('category') 
dt1.Perm_13C_Bare_10cm_Avg=pd.to_numeric(dt1.Perm_13C_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_13C_Bare_10cm_Avg=dt1.Flag_Perm_13C_Bare_10cm_Avg.astype('category') 
dt1.Perm_13C_Grass_10cm_Avg=pd.to_numeric(dt1.Perm_13C_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_13C_Grass_10cm_Avg=dt1.Flag_Perm_13C_Grass_10cm_Avg.astype('category') 
dt1.Perm_13C_Shrub_10cm_Avg=pd.to_numeric(dt1.Perm_13C_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_13C_Shrub_10cm_Avg=dt1.Flag_Perm_13C_Shrub_10cm_Avg.astype('category') 
dt1.Perm_13D_Bare_10cm_Avg=pd.to_numeric(dt1.Perm_13D_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_13D_Bare_10cm_Avg=dt1.Flag_Perm_13D_Bare_10cm_Avg.astype('category') 
dt1.Perm_13D_Grass_10cm_Avg=pd.to_numeric(dt1.Perm_13D_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_13D_Grass_10cm_Avg=dt1.Flag_Perm_13D_Grass_10cm_Avg.astype('category') 
dt1.Perm_13D_Shrub_10cm_Avg=pd.to_numeric(dt1.Perm_13D_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_13D_Shrub_10cm_Avg=dt1.Flag_Perm_13D_Shrub_10cm_Avg.astype('category') 
dt1.Period_13A_Bare_10cm_Avg=pd.to_numeric(dt1.Period_13A_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Period_13A_Bare_10cm_Avg=dt1.Flag_Period_13A_Bare_10cm_Avg.astype('category') 
dt1.Period_13A_Grass_10cm_Avg=pd.to_numeric(dt1.Period_13A_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Period_13A_Grass_10cm_Avg=dt1.Flag_Period_13A_Grass_10cm_Avg.astype('category') 
dt1.Period_13A_Shrub_10cm_Avg=pd.to_numeric(dt1.Period_13A_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Period_13A_Shrub_10cm_Avg=dt1.Flag_Period_13A_Shrub_10cm_Avg.astype('category') 
dt1.Period_13B_Bare_10cm_Avg=pd.to_numeric(dt1.Period_13B_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Period_13B_Bare_10cm_Avg=dt1.Flag_Period_13B_Bare_10cm_Avg.astype('category') 
dt1.Period_13B_Grass_10cm_Avg=pd.to_numeric(dt1.Period_13B_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Period_13B_Grass_10cm_Avg=dt1.Flag_Period_13B_Grass_10cm_Avg.astype('category') 
dt1.Period_13B_Shrub_10cm_Avg=pd.to_numeric(dt1.Period_13B_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Period_13B_Shrub_10cm_Avg=dt1.Flag_Period_13B_Shrub_10cm_Avg.astype('category') 
dt1.Period_13C_Bare_10cm_Avg=pd.to_numeric(dt1.Period_13C_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Period_13C_Bare_10cm_Avg=dt1.Flag_Period_13C_Bare_10cm_Avg.astype('category') 
dt1.Period_13C_Grass_10cm_Avg=pd.to_numeric(dt1.Period_13C_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Period_13C_Grass_10cm_Avg=dt1.Flag_Period_13C_Grass_10cm_Avg.astype('category') 
dt1.Period_13C_Shrub_10cm_Avg=pd.to_numeric(dt1.Period_13C_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Period_13C_Shrub_10cm_Avg=dt1.Flag_Period_13C_Shrub_10cm_Avg.astype('category') 
dt1.Period_13D_Bare_10cm_Avg=pd.to_numeric(dt1.Period_13D_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Period_13D_Bare_10cm_Avg=dt1.Flag_Period_13D_Bare_10cm_Avg.astype('category') 
dt1.Period_13D_Grass_10cm_Avg=pd.to_numeric(dt1.Period_13D_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Period_13D_Grass_10cm_Avg=dt1.Flag_Period_13D_Grass_10cm_Avg.astype('category') 
dt1.Period_13D_Shrub_10cm_Avg=pd.to_numeric(dt1.Period_13D_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Period_13D_Shrub_10cm_Avg=dt1.Flag_Period_13D_Shrub_10cm_Avg.astype('category') 
dt1.Vratio_13A_Bare_10cm_Avg=pd.to_numeric(dt1.Vratio_13A_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_13A_Bare_10cm_Avg=dt1.Flag_Vratio_13A_Bare_10cm_Avg.astype('category') 
dt1.Vratio_13A_Grass_10cm_Avg=pd.to_numeric(dt1.Vratio_13A_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_13A_Grass_10cm_Avg=dt1.Flag_Vratio_13A_Grass_10cm_Avg.astype('category') 
dt1.Vratio_13A_Shrub_10cm_Avg=pd.to_numeric(dt1.Vratio_13A_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_13A_Shrub_10cm_Avg=dt1.Flag_Vratio_13A_Shrub_10cm_Avg.astype('category') 
dt1.Vratio_13B_Bare_10cm_Avg=pd.to_numeric(dt1.Vratio_13B_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_13B_Bare_10cm_Avg=dt1.Flag_Vratio_13B_Bare_10cm_Avg.astype('category') 
dt1.Vratio_13B_Grass_10cm_Avg=pd.to_numeric(dt1.Vratio_13B_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_13B_Grass_10cm_Avg=dt1.Flag_Vratio_13B_Grass_10cm_Avg.astype('category') 
dt1.Vratio_13B_Shrub_10cm_Avg=pd.to_numeric(dt1.Vratio_13B_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_13B_Shrub_10cm_Avg=dt1.Flag_Vratio_13B_Shrub_10cm_Avg.astype('category') 
dt1.Vratio_13C_Bare_10cm_Avg=pd.to_numeric(dt1.Vratio_13C_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_13C_Bare_10cm_Avg=dt1.Flag_Vratio_13C_Bare_10cm_Avg.astype('category') 
dt1.Vratio_13C_Grass_10cm_Avg=pd.to_numeric(dt1.Vratio_13C_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_13C_Grass_10cm_Avg=dt1.Flag_Vratio_13C_Grass_10cm_Avg.astype('category') 
dt1.Vratio_13C_Shrub_10cm_Avg=pd.to_numeric(dt1.Vratio_13C_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_13C_Shrub_10cm_Avg=dt1.Flag_Vratio_13C_Shrub_10cm_Avg.astype('category') 
dt1.Vratio_13D_Bare_10cm_Avg=pd.to_numeric(dt1.Vratio_13D_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_13D_Bare_10cm_Avg=dt1.Flag_Vratio_13D_Bare_10cm_Avg.astype('category') 
dt1.Vratio_13D_Grass_10cm_Avg=pd.to_numeric(dt1.Vratio_13D_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_13D_Grass_10cm_Avg=dt1.Flag_Vratio_13D_Grass_10cm_Avg.astype('category') 
dt1.Vratio_13D_Shrub_10cm_Avg=pd.to_numeric(dt1.Vratio_13D_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_13D_Shrub_10cm_Avg=dt1.Flag_Vratio_13D_Shrub_10cm_Avg.astype('category') 
      
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
                    
print(dt1.Vwc_13A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_13A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_13A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_13A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_13A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_13A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_13B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_13B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_13B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_13B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_13B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_13B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_13C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_13C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_13C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_13C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_13C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_13C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_13D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_13D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_13D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_13D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_13D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_13D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_13A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_13A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_13A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_13A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_13A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_13A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_13B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_13B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_13B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_13B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_13B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_13B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_13C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_13C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_13C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_13C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_13C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_13C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_13D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_13D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_13D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_13D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_13D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_13D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_13A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_13A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_13A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_13A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_13A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_13A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_13B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_13B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_13B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_13B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_13B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_13B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_13C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_13C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_13C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_13C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_13C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_13C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_13D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_13D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_13D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_13D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_13D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_13D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_13A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_13A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_13A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_13A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_13A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_13A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_13B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_13B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_13B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_13B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_13B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_13B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_13C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_13C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_13C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_13C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_13C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_13C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_13D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_13D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_13D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_13D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_13D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_13D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_13A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_13A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_13A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_13A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_13A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_13A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_13B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_13B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_13B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_13B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_13B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_13B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_13C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_13C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_13C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_13C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_13C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_13C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_13D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_13D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_13D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_13D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_13D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_13D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_13A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_13A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_13A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_13A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_13A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_13A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_13B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_13B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_13B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_13B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_13B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_13B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_13C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_13C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_13C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_13C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_13C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_13C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_13D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_13D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_13D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_13D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_13D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_13D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
                    
                




