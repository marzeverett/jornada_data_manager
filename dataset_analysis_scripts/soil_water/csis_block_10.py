# Package ID: knb-lter-jrn.210548085.30 Cataloging System:https://pasta.edirepository.org.
# Data set title: Jornada Basin LTER Cross-scale Interactions Study (CSIS) Block 10 meteorological station: Daily average soil volumetric water content data: 2013 - ongoing.
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

infile1  ="https://pasta.lternet.edu/package/data/eml/knb-lter-jrn/210548085/30/3f593bd72a8b04dcd65aeb5c1b5a8073".strip() 
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
                    "Vwc_10A_Bare_10cm_Avg",     
                    "Flag_Vwc_10A_Bare_10cm_Avg",     
                    "Vwc_10A_Grass_10cm_Avg",     
                    "Flag_Vwc_10A_Grass_10cm_Avg",     
                    "Vwc_10A_Shrub_10cm_Avg",     
                    "Flag_Vwc_10A_Shrub_10cm_Avg",     
                    "Vwc_10B_Bare_10cm_Avg",     
                    "Flag_Vwc_10B_Bare_10cm_Avg",     
                    "Vwc_10B_Grass_10cm_Avg",     
                    "Flag_Vwc_10B_Grass_10cm_Avg",     
                    "Vwc_10B_Shrub_10cm_Avg",     
                    "Flag_Vwc_10B_Shrub_10cm_Avg",     
                    "Vwc_10C_Bare_10cm_Avg",     
                    "Flag_Vwc_10C_Bare_10cm_Avg",     
                    "Vwc_10C_Grass_10cm_Avg",     
                    "Flag_Vwc_10C_Grass_10cm_Avg",     
                    "Vwc_10C_Shrub_10cm_Avg",     
                    "Flag_Vwc_10C_Shrub_10cm_Avg",     
                    "Vwc_10D_Bare_10cm_Avg",     
                    "Flag_Vwc_10D_Bare_10cm_Avg",     
                    "Vwc_10D_Grass_10cm_Avg",     
                    "Flag_Vwc_10D_Grass_10cm_Avg",     
                    "Vwc_10D_Shrub_10cm_Avg",     
                    "Flag_Vwc_10D_Shrub_10cm_Avg",     
                    "Ec_10A_Bare_10cm_Avg",     
                    "Flag_Ec_10A_Bare_10cm_Avg",     
                    "Ec_10A_Grass_10cm_Avg",     
                    "Flag_Ec_10A_Grass_10cm_Avg",     
                    "Ec_10A_Shrub_10cm_Avg",     
                    "Flag_Ec_10A_Shrub_10cm_Avg",     
                    "Ec_10B_Bare_10cm_Avg",     
                    "Flag_Ec_10B_Bare_10cm_Avg",     
                    "Ec_10B_Grass_10cm_Avg",     
                    "Flag_Ec_10B_Grass_10cm_Avg",     
                    "Ec_10B_Shrub_10cm_Avg",     
                    "Flag_Ec_10B_Shrub_10cm_Avg",     
                    "Ec_10C_Bare_10cm_Avg",     
                    "Flag_Ec_10C_Bare_10cm_Avg",     
                    "Ec_10C_Grass_10cm_Avg",     
                    "Flag_Ec_10C_Grass_10cm_Avg",     
                    "Ec_10C_Shrub_10cm_Avg",     
                    "Flag_Ec_10C_Shrub_10cm_Avg",     
                    "Ec_10D_Bare_10cm_Avg",     
                    "Flag_Ec_10D_Bare_10cm_Avg",     
                    "Ec_10D_Grass_10cm_Avg",     
                    "Flag_Ec_10D_Grass_10cm_Avg",     
                    "Ec_10D_Shrub_10cm_Avg",     
                    "Flag_Ec_10D_Shrub_10cm_Avg",     
                    "Tsoil_10A_Bare_10cm_Avg",     
                    "Flag_Tsoil_10A_Bare_10cm_Avg",     
                    "Tsoil_10A_Grass_10cm_Avg",     
                    "Flag_Tsoil_10A_Grass_10cm_Avg",     
                    "Tsoil_10A_Shrub_10cm_Avg",     
                    "Flag_Tsoil_10A_Shrub_10cm_Avg",     
                    "Tsoil_10B_Bare_10cm_Avg",     
                    "Flag_Tsoil_10B_Bare_10cm_Avg",     
                    "Tsoil_10B_Grass_10cm_Avg",     
                    "Flag_Tsoil_10B_Grass_10cm_Avg",     
                    "Tsoil_10B_Shrub_10cm_Avg",     
                    "Flag_Tsoil_10B_Shrub_10cm_Avg",     
                    "Tsoil_10C_Bare_10cm_Avg",     
                    "Flag_Tsoil_10C_Bare_10cm_Avg",     
                    "Tsoil_10C_Grass_10cm_Avg",     
                    "Flag_Tsoil_10C_Grass_10cm_Avg",     
                    "Tsoil_10C_Shrub_10cm_Avg",     
                    "Flag_Tsoil_10C_Shrub_10cm_Avg",     
                    "Tsoil_10D_Bare_10cm_Avg",     
                    "Flag_Tsoil_10D_Bare_10cm_Avg",     
                    "Tsoil_10D_Grass_10cm_Avg",     
                    "Flag_Tsoil_10D_Grass_10cm_Avg",     
                    "Tsoil_10D_Shrub_10cm_Avg",     
                    "Flag_Tsoil_10D_Shrub_10cm_Avg",     
                    "Perm_10A_Bare_10cm_Avg",     
                    "Flag_Perm_10A_Bare_10cm_Avg",     
                    "Perm_10A_Grass_10cm_Avg",     
                    "Flag_Perm_10A_Grass_10cm_Avg",     
                    "Perm_10A_Shrub_10cm_Avg",     
                    "Flag_Perm_10A_Shrub_10cm_Avg",     
                    "Perm_10B_Bare_10cm_Avg",     
                    "Flag_Perm_10B_Bare_10cm_Avg",     
                    "Perm_10B_Grass_10cm_Avg",     
                    "Flag_Perm_10B_Grass_10cm_Avg",     
                    "Perm_10B_Shrub_10cm_Avg",     
                    "Flag_Perm_10B_Shrub_10cm_Avg",     
                    "Perm_10C_Bare_10cm_Avg",     
                    "Flag_Perm_10C_Bare_10cm_Avg",     
                    "Perm_10C_Grass_10cm_Avg",     
                    "Flag_Perm_10C_Grass_10cm_Avg",     
                    "Perm_10C_Shrub_10cm_Avg",     
                    "Flag_Perm_10C_Shrub_10cm_Avg",     
                    "Perm_10D_Bare_10cm_Avg",     
                    "Flag_Perm_10D_Bare_10cm_Avg",     
                    "Perm_10D_Grass_10cm_Avg",     
                    "Flag_Perm_10D_Grass_10cm_Avg",     
                    "Perm_10D_Shrub_10cm_Avg",     
                    "Flag_Perm_10D_Shrub_10cm_Avg",     
                    "Period_10A_Bare_10cm_Avg",     
                    "Flag_Period_10A_Bare_10cm_Avg",     
                    "Period_10A_Grass_10cm_Avg",     
                    "Flag_Period_10A_Grass_10cm_Avg",     
                    "Period_10A_Shrub_10cm_Avg",     
                    "Flag_Period_10A_Shrub_10cm_Avg",     
                    "Period_10B_Bare_10cm_Avg",     
                    "Flag_Period_10B_Bare_10cm_Avg",     
                    "Period_10B_Grass_10cm_Avg",     
                    "Flag_Period_10B_Grass_10cm_Avg",     
                    "Period_10B_Shrub_10cm_Avg",     
                    "Flag_Period_10B_Shrub_10cm_Avg",     
                    "Period_10C_Bare_10cm_Avg",     
                    "Flag_Period_10C_Bare_10cm_Avg",     
                    "Period_10C_Grass_10cm_Avg",     
                    "Flag_Period_10C_Grass_10cm_Avg",     
                    "Period_10C_Shrub_10cm_Avg",     
                    "Flag_Period_10C_Shrub_10cm_Avg",     
                    "Period_10D_Bare_10cm_Avg",     
                    "Flag_Period_10D_Bare_10cm_Avg",     
                    "Period_10D_Grass_10cm_Avg",     
                    "Flag_Period_10D_Grass_10cm_Avg",     
                    "Period_10D_Shrub_10cm_Avg",     
                    "Flag_Period_10D_Shrub_10cm_Avg",     
                    "Vratio_10A_Bare_10cm_Avg",     
                    "Flag_Vratio_10A_Bare_10cm_Avg",     
                    "Vratio_10A_Grass_10cm_Avg",     
                    "Flag_Vratio_10A_Grass_10cm_Avg",     
                    "Vratio_10A_Shrub_10cm_Avg",     
                    "Flag_Vratio_10A_Shrub_10cm_Avg",     
                    "Vratio_10B_Bare_10cm_Avg",     
                    "Flag_Vratio_10B_Bare_10cm_Avg",     
                    "Vratio_10B_Grass_10cm_Avg",     
                    "Flag_Vratio_10B_Grass_10cm_Avg",     
                    "Vratio_10B_Shrub_10cm_Avg",     
                    "Flag_Vratio_10B_Shrub_10cm_Avg",     
                    "Vratio_10C_Bare_10cm_Avg",     
                    "Flag_Vratio_10C_Bare_10cm_Avg",     
                    "Vratio_10C_Grass_10cm_Avg",     
                    "Flag_Vratio_10C_Grass_10cm_Avg",     
                    "Vratio_10C_Shrub_10cm_Avg",     
                    "Flag_Vratio_10C_Shrub_10cm_Avg",     
                    "Vratio_10D_Bare_10cm_Avg",     
                    "Flag_Vratio_10D_Bare_10cm_Avg",     
                    "Vratio_10D_Grass_10cm_Avg",     
                    "Flag_Vratio_10D_Grass_10cm_Avg",     
                    "Vratio_10D_Shrub_10cm_Avg",     
                    "Flag_Vratio_10D_Shrub_10cm_Avg"    ]
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
#             'Vwc_10A_Bare_10cm_Avg':'float' ,  
#             'Flag_Vwc_10A_Bare_10cm_Avg':'str' , 
#             'Vwc_10A_Grass_10cm_Avg':'float' ,  
#             'Flag_Vwc_10A_Grass_10cm_Avg':'str' , 
#             'Vwc_10A_Shrub_10cm_Avg':'float' ,  
#             'Flag_Vwc_10A_Shrub_10cm_Avg':'str' , 
#             'Vwc_10B_Bare_10cm_Avg':'float' ,  
#             'Flag_Vwc_10B_Bare_10cm_Avg':'str' , 
#             'Vwc_10B_Grass_10cm_Avg':'float' ,  
#             'Flag_Vwc_10B_Grass_10cm_Avg':'str' , 
#             'Vwc_10B_Shrub_10cm_Avg':'float' ,  
#             'Flag_Vwc_10B_Shrub_10cm_Avg':'str' , 
#             'Vwc_10C_Bare_10cm_Avg':'float' ,  
#             'Flag_Vwc_10C_Bare_10cm_Avg':'str' , 
#             'Vwc_10C_Grass_10cm_Avg':'float' ,  
#             'Flag_Vwc_10C_Grass_10cm_Avg':'str' , 
#             'Vwc_10C_Shrub_10cm_Avg':'float' ,  
#             'Flag_Vwc_10C_Shrub_10cm_Avg':'str' , 
#             'Vwc_10D_Bare_10cm_Avg':'float' ,  
#             'Flag_Vwc_10D_Bare_10cm_Avg':'str' , 
#             'Vwc_10D_Grass_10cm_Avg':'float' ,  
#             'Flag_Vwc_10D_Grass_10cm_Avg':'str' , 
#             'Vwc_10D_Shrub_10cm_Avg':'float' ,  
#             'Flag_Vwc_10D_Shrub_10cm_Avg':'str' , 
#             'Ec_10A_Bare_10cm_Avg':'float' ,  
#             'Flag_Ec_10A_Bare_10cm_Avg':'str' , 
#             'Ec_10A_Grass_10cm_Avg':'float' ,  
#             'Flag_Ec_10A_Grass_10cm_Avg':'str' , 
#             'Ec_10A_Shrub_10cm_Avg':'float' ,  
#             'Flag_Ec_10A_Shrub_10cm_Avg':'str' , 
#             'Ec_10B_Bare_10cm_Avg':'float' ,  
#             'Flag_Ec_10B_Bare_10cm_Avg':'str' , 
#             'Ec_10B_Grass_10cm_Avg':'float' ,  
#             'Flag_Ec_10B_Grass_10cm_Avg':'str' , 
#             'Ec_10B_Shrub_10cm_Avg':'float' ,  
#             'Flag_Ec_10B_Shrub_10cm_Avg':'str' , 
#             'Ec_10C_Bare_10cm_Avg':'float' ,  
#             'Flag_Ec_10C_Bare_10cm_Avg':'str' , 
#             'Ec_10C_Grass_10cm_Avg':'float' ,  
#             'Flag_Ec_10C_Grass_10cm_Avg':'str' , 
#             'Ec_10C_Shrub_10cm_Avg':'float' ,  
#             'Flag_Ec_10C_Shrub_10cm_Avg':'str' , 
#             'Ec_10D_Bare_10cm_Avg':'float' ,  
#             'Flag_Ec_10D_Bare_10cm_Avg':'str' , 
#             'Ec_10D_Grass_10cm_Avg':'float' ,  
#             'Flag_Ec_10D_Grass_10cm_Avg':'str' , 
#             'Ec_10D_Shrub_10cm_Avg':'float' ,  
#             'Flag_Ec_10D_Shrub_10cm_Avg':'str' , 
#             'Tsoil_10A_Bare_10cm_Avg':'float' ,  
#             'Flag_Tsoil_10A_Bare_10cm_Avg':'str' , 
#             'Tsoil_10A_Grass_10cm_Avg':'float' ,  
#             'Flag_Tsoil_10A_Grass_10cm_Avg':'str' , 
#             'Tsoil_10A_Shrub_10cm_Avg':'float' ,  
#             'Flag_Tsoil_10A_Shrub_10cm_Avg':'str' , 
#             'Tsoil_10B_Bare_10cm_Avg':'float' ,  
#             'Flag_Tsoil_10B_Bare_10cm_Avg':'str' , 
#             'Tsoil_10B_Grass_10cm_Avg':'float' ,  
#             'Flag_Tsoil_10B_Grass_10cm_Avg':'str' , 
#             'Tsoil_10B_Shrub_10cm_Avg':'float' ,  
#             'Flag_Tsoil_10B_Shrub_10cm_Avg':'str' , 
#             'Tsoil_10C_Bare_10cm_Avg':'float' ,  
#             'Flag_Tsoil_10C_Bare_10cm_Avg':'str' , 
#             'Tsoil_10C_Grass_10cm_Avg':'float' ,  
#             'Flag_Tsoil_10C_Grass_10cm_Avg':'str' , 
#             'Tsoil_10C_Shrub_10cm_Avg':'float' ,  
#             'Flag_Tsoil_10C_Shrub_10cm_Avg':'str' , 
#             'Tsoil_10D_Bare_10cm_Avg':'float' ,  
#             'Flag_Tsoil_10D_Bare_10cm_Avg':'str' , 
#             'Tsoil_10D_Grass_10cm_Avg':'float' ,  
#             'Flag_Tsoil_10D_Grass_10cm_Avg':'str' , 
#             'Tsoil_10D_Shrub_10cm_Avg':'float' ,  
#             'Flag_Tsoil_10D_Shrub_10cm_Avg':'str' , 
#             'Perm_10A_Bare_10cm_Avg':'float' ,  
#             'Flag_Perm_10A_Bare_10cm_Avg':'str' , 
#             'Perm_10A_Grass_10cm_Avg':'float' ,  
#             'Flag_Perm_10A_Grass_10cm_Avg':'str' , 
#             'Perm_10A_Shrub_10cm_Avg':'float' ,  
#             'Flag_Perm_10A_Shrub_10cm_Avg':'str' , 
#             'Perm_10B_Bare_10cm_Avg':'float' ,  
#             'Flag_Perm_10B_Bare_10cm_Avg':'str' , 
#             'Perm_10B_Grass_10cm_Avg':'float' ,  
#             'Flag_Perm_10B_Grass_10cm_Avg':'str' , 
#             'Perm_10B_Shrub_10cm_Avg':'float' ,  
#             'Flag_Perm_10B_Shrub_10cm_Avg':'str' , 
#             'Perm_10C_Bare_10cm_Avg':'float' ,  
#             'Flag_Perm_10C_Bare_10cm_Avg':'str' , 
#             'Perm_10C_Grass_10cm_Avg':'float' ,  
#             'Flag_Perm_10C_Grass_10cm_Avg':'str' , 
#             'Perm_10C_Shrub_10cm_Avg':'float' ,  
#             'Flag_Perm_10C_Shrub_10cm_Avg':'str' , 
#             'Perm_10D_Bare_10cm_Avg':'float' ,  
#             'Flag_Perm_10D_Bare_10cm_Avg':'str' , 
#             'Perm_10D_Grass_10cm_Avg':'float' ,  
#             'Flag_Perm_10D_Grass_10cm_Avg':'str' , 
#             'Perm_10D_Shrub_10cm_Avg':'float' ,  
#             'Flag_Perm_10D_Shrub_10cm_Avg':'str' , 
#             'Period_10A_Bare_10cm_Avg':'float' ,  
#             'Flag_Period_10A_Bare_10cm_Avg':'str' , 
#             'Period_10A_Grass_10cm_Avg':'float' ,  
#             'Flag_Period_10A_Grass_10cm_Avg':'str' , 
#             'Period_10A_Shrub_10cm_Avg':'float' ,  
#             'Flag_Period_10A_Shrub_10cm_Avg':'str' , 
#             'Period_10B_Bare_10cm_Avg':'float' ,  
#             'Flag_Period_10B_Bare_10cm_Avg':'str' , 
#             'Period_10B_Grass_10cm_Avg':'float' ,  
#             'Flag_Period_10B_Grass_10cm_Avg':'str' , 
#             'Period_10B_Shrub_10cm_Avg':'float' ,  
#             'Flag_Period_10B_Shrub_10cm_Avg':'str' , 
#             'Period_10C_Bare_10cm_Avg':'float' ,  
#             'Flag_Period_10C_Bare_10cm_Avg':'str' , 
#             'Period_10C_Grass_10cm_Avg':'float' ,  
#             'Flag_Period_10C_Grass_10cm_Avg':'str' , 
#             'Period_10C_Shrub_10cm_Avg':'float' ,  
#             'Flag_Period_10C_Shrub_10cm_Avg':'str' , 
#             'Period_10D_Bare_10cm_Avg':'float' ,  
#             'Flag_Period_10D_Bare_10cm_Avg':'str' , 
#             'Period_10D_Grass_10cm_Avg':'float' ,  
#             'Flag_Period_10D_Grass_10cm_Avg':'str' , 
#             'Period_10D_Shrub_10cm_Avg':'float' ,  
#             'Flag_Period_10D_Shrub_10cm_Avg':'str' , 
#             'Vratio_10A_Bare_10cm_Avg':'float' ,  
#             'Flag_Vratio_10A_Bare_10cm_Avg':'str' , 
#             'Vratio_10A_Grass_10cm_Avg':'float' ,  
#             'Flag_Vratio_10A_Grass_10cm_Avg':'str' , 
#             'Vratio_10A_Shrub_10cm_Avg':'float' ,  
#             'Flag_Vratio_10A_Shrub_10cm_Avg':'str' , 
#             'Vratio_10B_Bare_10cm_Avg':'float' ,  
#             'Flag_Vratio_10B_Bare_10cm_Avg':'str' , 
#             'Vratio_10B_Grass_10cm_Avg':'float' ,  
#             'Flag_Vratio_10B_Grass_10cm_Avg':'str' , 
#             'Vratio_10B_Shrub_10cm_Avg':'float' ,  
#             'Flag_Vratio_10B_Shrub_10cm_Avg':'str' , 
#             'Vratio_10C_Bare_10cm_Avg':'float' ,  
#             'Flag_Vratio_10C_Bare_10cm_Avg':'str' , 
#             'Vratio_10C_Grass_10cm_Avg':'float' ,  
#             'Flag_Vratio_10C_Grass_10cm_Avg':'str' , 
#             'Vratio_10C_Shrub_10cm_Avg':'float' ,  
#             'Flag_Vratio_10C_Shrub_10cm_Avg':'str' , 
#             'Vratio_10D_Bare_10cm_Avg':'float' ,  
#             'Flag_Vratio_10D_Bare_10cm_Avg':'str' , 
#             'Vratio_10D_Grass_10cm_Avg':'float' ,  
#             'Flag_Vratio_10D_Grass_10cm_Avg':'str' , 
#             'Vratio_10D_Shrub_10cm_Avg':'float' ,  
#             'Flag_Vratio_10D_Shrub_10cm_Avg':'str'  
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
                  'Vwc_10A_Bare_10cm_Avg':[
                          'NaN',],
                  'Vwc_10A_Grass_10cm_Avg':[
                          'NaN',],
                  'Vwc_10A_Shrub_10cm_Avg':[
                          'NaN',],
                  'Vwc_10B_Bare_10cm_Avg':[
                          'NaN',],
                  'Vwc_10B_Grass_10cm_Avg':[
                          'NaN',],
                  'Vwc_10B_Shrub_10cm_Avg':[
                          'NaN',],
                  'Vwc_10C_Bare_10cm_Avg':[
                          'NaN',],
                  'Vwc_10C_Grass_10cm_Avg':[
                          'NaN',],
                  'Vwc_10C_Shrub_10cm_Avg':[
                          'NaN',],
                  'Vwc_10D_Bare_10cm_Avg':[
                          'NaN',],
                  'Vwc_10D_Grass_10cm_Avg':[
                          'NaN',],
                  'Vwc_10D_Shrub_10cm_Avg':[
                          'NaN',],
                  'Ec_10A_Bare_10cm_Avg':[
                          'NaN',],
                  'Ec_10A_Grass_10cm_Avg':[
                          'NaN',],
                  'Ec_10A_Shrub_10cm_Avg':[
                          'NaN',],
                  'Ec_10B_Bare_10cm_Avg':[
                          'NaN',],
                  'Ec_10B_Grass_10cm_Avg':[
                          'NaN',],
                  'Ec_10B_Shrub_10cm_Avg':[
                          'NaN',],
                  'Ec_10C_Bare_10cm_Avg':[
                          'NaN',],
                  'Ec_10C_Grass_10cm_Avg':[
                          'NaN',],
                  'Ec_10C_Shrub_10cm_Avg':[
                          'NaN',],
                  'Ec_10D_Bare_10cm_Avg':[
                          'NaN',],
                  'Ec_10D_Grass_10cm_Avg':[
                          'NaN',],
                  'Ec_10D_Shrub_10cm_Avg':[
                          'NaN',],
                  'Tsoil_10A_Bare_10cm_Avg':[
                          'NaN',],
                  'Tsoil_10A_Grass_10cm_Avg':[
                          'NaN',],
                  'Tsoil_10A_Shrub_10cm_Avg':[
                          'NaN',],
                  'Tsoil_10B_Bare_10cm_Avg':[
                          'NaN',],
                  'Tsoil_10B_Grass_10cm_Avg':[
                          'NaN',],
                  'Tsoil_10B_Shrub_10cm_Avg':[
                          'NaN',],
                  'Tsoil_10C_Bare_10cm_Avg':[
                          'NaN',],
                  'Tsoil_10C_Grass_10cm_Avg':[
                          'NaN',],
                  'Tsoil_10C_Shrub_10cm_Avg':[
                          'NaN',],
                  'Tsoil_10D_Bare_10cm_Avg':[
                          'NaN',],
                  'Tsoil_10D_Grass_10cm_Avg':[
                          'NaN',],
                  'Tsoil_10D_Shrub_10cm_Avg':[
                          'NaN',],
                  'Perm_10A_Bare_10cm_Avg':[
                          'NaN',],
                  'Perm_10A_Grass_10cm_Avg':[
                          'NaN',],
                  'Perm_10A_Shrub_10cm_Avg':[
                          'NaN',],
                  'Perm_10B_Bare_10cm_Avg':[
                          'NaN',],
                  'Perm_10B_Grass_10cm_Avg':[
                          'NaN',],
                  'Perm_10B_Shrub_10cm_Avg':[
                          'NaN',],
                  'Perm_10C_Bare_10cm_Avg':[
                          'NaN',],
                  'Perm_10C_Grass_10cm_Avg':[
                          'NaN',],
                  'Perm_10C_Shrub_10cm_Avg':[
                          'NaN',],
                  'Perm_10D_Bare_10cm_Avg':[
                          'NaN',],
                  'Perm_10D_Grass_10cm_Avg':[
                          'NaN',],
                  'Perm_10D_Shrub_10cm_Avg':[
                          'NaN',],
                  'Period_10A_Bare_10cm_Avg':[
                          'NaN',],
                  'Period_10A_Grass_10cm_Avg':[
                          'NaN',],
                  'Period_10A_Shrub_10cm_Avg':[
                          'NaN',],
                  'Period_10B_Bare_10cm_Avg':[
                          'NaN',],
                  'Period_10B_Grass_10cm_Avg':[
                          'NaN',],
                  'Period_10B_Shrub_10cm_Avg':[
                          'NaN',],
                  'Period_10C_Bare_10cm_Avg':[
                          'NaN',],
                  'Period_10C_Grass_10cm_Avg':[
                          'NaN',],
                  'Period_10C_Shrub_10cm_Avg':[
                          'NaN',],
                  'Period_10D_Bare_10cm_Avg':[
                          'NaN',],
                  'Period_10D_Grass_10cm_Avg':[
                          'NaN',],
                  'Period_10D_Shrub_10cm_Avg':[
                          'NaN',],
                  'Vratio_10A_Bare_10cm_Avg':[
                          'NaN',],
                  'Vratio_10A_Grass_10cm_Avg':[
                          'NaN',],
                  'Vratio_10A_Shrub_10cm_Avg':[
                          'NaN',],
                  'Vratio_10B_Bare_10cm_Avg':[
                          'NaN',],
                  'Vratio_10B_Grass_10cm_Avg':[
                          'NaN',],
                  'Vratio_10B_Shrub_10cm_Avg':[
                          'NaN',],
                  'Vratio_10C_Bare_10cm_Avg':[
                          'NaN',],
                  'Vratio_10C_Grass_10cm_Avg':[
                          'NaN',],
                  'Vratio_10C_Shrub_10cm_Avg':[
                          'NaN',],
                  'Vratio_10D_Bare_10cm_Avg':[
                          'NaN',],
                  'Vratio_10D_Grass_10cm_Avg':[
                          'NaN',],
                  'Vratio_10D_Shrub_10cm_Avg':[
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
dt1.Vwc_10A_Bare_10cm_Avg=pd.to_numeric(dt1.Vwc_10A_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_10A_Bare_10cm_Avg=dt1.Flag_Vwc_10A_Bare_10cm_Avg.astype('category') 
dt1.Vwc_10A_Grass_10cm_Avg=pd.to_numeric(dt1.Vwc_10A_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_10A_Grass_10cm_Avg=dt1.Flag_Vwc_10A_Grass_10cm_Avg.astype('category') 
dt1.Vwc_10A_Shrub_10cm_Avg=pd.to_numeric(dt1.Vwc_10A_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_10A_Shrub_10cm_Avg=dt1.Flag_Vwc_10A_Shrub_10cm_Avg.astype('category') 
dt1.Vwc_10B_Bare_10cm_Avg=pd.to_numeric(dt1.Vwc_10B_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_10B_Bare_10cm_Avg=dt1.Flag_Vwc_10B_Bare_10cm_Avg.astype('category') 
dt1.Vwc_10B_Grass_10cm_Avg=pd.to_numeric(dt1.Vwc_10B_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_10B_Grass_10cm_Avg=dt1.Flag_Vwc_10B_Grass_10cm_Avg.astype('category') 
dt1.Vwc_10B_Shrub_10cm_Avg=pd.to_numeric(dt1.Vwc_10B_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_10B_Shrub_10cm_Avg=dt1.Flag_Vwc_10B_Shrub_10cm_Avg.astype('category') 
dt1.Vwc_10C_Bare_10cm_Avg=pd.to_numeric(dt1.Vwc_10C_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_10C_Bare_10cm_Avg=dt1.Flag_Vwc_10C_Bare_10cm_Avg.astype('category') 
dt1.Vwc_10C_Grass_10cm_Avg=pd.to_numeric(dt1.Vwc_10C_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_10C_Grass_10cm_Avg=dt1.Flag_Vwc_10C_Grass_10cm_Avg.astype('category') 
dt1.Vwc_10C_Shrub_10cm_Avg=pd.to_numeric(dt1.Vwc_10C_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_10C_Shrub_10cm_Avg=dt1.Flag_Vwc_10C_Shrub_10cm_Avg.astype('category') 
dt1.Vwc_10D_Bare_10cm_Avg=pd.to_numeric(dt1.Vwc_10D_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_10D_Bare_10cm_Avg=dt1.Flag_Vwc_10D_Bare_10cm_Avg.astype('category') 
dt1.Vwc_10D_Grass_10cm_Avg=pd.to_numeric(dt1.Vwc_10D_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_10D_Grass_10cm_Avg=dt1.Flag_Vwc_10D_Grass_10cm_Avg.astype('category') 
dt1.Vwc_10D_Shrub_10cm_Avg=pd.to_numeric(dt1.Vwc_10D_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Vwc_10D_Shrub_10cm_Avg=dt1.Flag_Vwc_10D_Shrub_10cm_Avg.astype('category') 
dt1.Ec_10A_Bare_10cm_Avg=pd.to_numeric(dt1.Ec_10A_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_10A_Bare_10cm_Avg=dt1.Flag_Ec_10A_Bare_10cm_Avg.astype('category') 
dt1.Ec_10A_Grass_10cm_Avg=pd.to_numeric(dt1.Ec_10A_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_10A_Grass_10cm_Avg=dt1.Flag_Ec_10A_Grass_10cm_Avg.astype('category') 
dt1.Ec_10A_Shrub_10cm_Avg=pd.to_numeric(dt1.Ec_10A_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_10A_Shrub_10cm_Avg=dt1.Flag_Ec_10A_Shrub_10cm_Avg.astype('category') 
dt1.Ec_10B_Bare_10cm_Avg=pd.to_numeric(dt1.Ec_10B_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_10B_Bare_10cm_Avg=dt1.Flag_Ec_10B_Bare_10cm_Avg.astype('category') 
dt1.Ec_10B_Grass_10cm_Avg=pd.to_numeric(dt1.Ec_10B_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_10B_Grass_10cm_Avg=dt1.Flag_Ec_10B_Grass_10cm_Avg.astype('category') 
dt1.Ec_10B_Shrub_10cm_Avg=pd.to_numeric(dt1.Ec_10B_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_10B_Shrub_10cm_Avg=dt1.Flag_Ec_10B_Shrub_10cm_Avg.astype('category') 
dt1.Ec_10C_Bare_10cm_Avg=pd.to_numeric(dt1.Ec_10C_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_10C_Bare_10cm_Avg=dt1.Flag_Ec_10C_Bare_10cm_Avg.astype('category') 
dt1.Ec_10C_Grass_10cm_Avg=pd.to_numeric(dt1.Ec_10C_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_10C_Grass_10cm_Avg=dt1.Flag_Ec_10C_Grass_10cm_Avg.astype('category') 
dt1.Ec_10C_Shrub_10cm_Avg=pd.to_numeric(dt1.Ec_10C_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_10C_Shrub_10cm_Avg=dt1.Flag_Ec_10C_Shrub_10cm_Avg.astype('category') 
dt1.Ec_10D_Bare_10cm_Avg=pd.to_numeric(dt1.Ec_10D_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_10D_Bare_10cm_Avg=dt1.Flag_Ec_10D_Bare_10cm_Avg.astype('category') 
dt1.Ec_10D_Grass_10cm_Avg=pd.to_numeric(dt1.Ec_10D_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_10D_Grass_10cm_Avg=dt1.Flag_Ec_10D_Grass_10cm_Avg.astype('category') 
dt1.Ec_10D_Shrub_10cm_Avg=pd.to_numeric(dt1.Ec_10D_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Ec_10D_Shrub_10cm_Avg=dt1.Flag_Ec_10D_Shrub_10cm_Avg.astype('category') 
dt1.Tsoil_10A_Bare_10cm_Avg=pd.to_numeric(dt1.Tsoil_10A_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_10A_Bare_10cm_Avg=dt1.Flag_Tsoil_10A_Bare_10cm_Avg.astype('category') 
dt1.Tsoil_10A_Grass_10cm_Avg=pd.to_numeric(dt1.Tsoil_10A_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_10A_Grass_10cm_Avg=dt1.Flag_Tsoil_10A_Grass_10cm_Avg.astype('category') 
dt1.Tsoil_10A_Shrub_10cm_Avg=pd.to_numeric(dt1.Tsoil_10A_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_10A_Shrub_10cm_Avg=dt1.Flag_Tsoil_10A_Shrub_10cm_Avg.astype('category') 
dt1.Tsoil_10B_Bare_10cm_Avg=pd.to_numeric(dt1.Tsoil_10B_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_10B_Bare_10cm_Avg=dt1.Flag_Tsoil_10B_Bare_10cm_Avg.astype('category') 
dt1.Tsoil_10B_Grass_10cm_Avg=pd.to_numeric(dt1.Tsoil_10B_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_10B_Grass_10cm_Avg=dt1.Flag_Tsoil_10B_Grass_10cm_Avg.astype('category') 
dt1.Tsoil_10B_Shrub_10cm_Avg=pd.to_numeric(dt1.Tsoil_10B_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_10B_Shrub_10cm_Avg=dt1.Flag_Tsoil_10B_Shrub_10cm_Avg.astype('category') 
dt1.Tsoil_10C_Bare_10cm_Avg=pd.to_numeric(dt1.Tsoil_10C_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_10C_Bare_10cm_Avg=dt1.Flag_Tsoil_10C_Bare_10cm_Avg.astype('category') 
dt1.Tsoil_10C_Grass_10cm_Avg=pd.to_numeric(dt1.Tsoil_10C_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_10C_Grass_10cm_Avg=dt1.Flag_Tsoil_10C_Grass_10cm_Avg.astype('category') 
dt1.Tsoil_10C_Shrub_10cm_Avg=pd.to_numeric(dt1.Tsoil_10C_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_10C_Shrub_10cm_Avg=dt1.Flag_Tsoil_10C_Shrub_10cm_Avg.astype('category') 
dt1.Tsoil_10D_Bare_10cm_Avg=pd.to_numeric(dt1.Tsoil_10D_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_10D_Bare_10cm_Avg=dt1.Flag_Tsoil_10D_Bare_10cm_Avg.astype('category') 
dt1.Tsoil_10D_Grass_10cm_Avg=pd.to_numeric(dt1.Tsoil_10D_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_10D_Grass_10cm_Avg=dt1.Flag_Tsoil_10D_Grass_10cm_Avg.astype('category') 
dt1.Tsoil_10D_Shrub_10cm_Avg=pd.to_numeric(dt1.Tsoil_10D_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Tsoil_10D_Shrub_10cm_Avg=dt1.Flag_Tsoil_10D_Shrub_10cm_Avg.astype('category') 
dt1.Perm_10A_Bare_10cm_Avg=pd.to_numeric(dt1.Perm_10A_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_10A_Bare_10cm_Avg=dt1.Flag_Perm_10A_Bare_10cm_Avg.astype('category') 
dt1.Perm_10A_Grass_10cm_Avg=pd.to_numeric(dt1.Perm_10A_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_10A_Grass_10cm_Avg=dt1.Flag_Perm_10A_Grass_10cm_Avg.astype('category') 
dt1.Perm_10A_Shrub_10cm_Avg=pd.to_numeric(dt1.Perm_10A_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_10A_Shrub_10cm_Avg=dt1.Flag_Perm_10A_Shrub_10cm_Avg.astype('category') 
dt1.Perm_10B_Bare_10cm_Avg=pd.to_numeric(dt1.Perm_10B_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_10B_Bare_10cm_Avg=dt1.Flag_Perm_10B_Bare_10cm_Avg.astype('category') 
dt1.Perm_10B_Grass_10cm_Avg=pd.to_numeric(dt1.Perm_10B_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_10B_Grass_10cm_Avg=dt1.Flag_Perm_10B_Grass_10cm_Avg.astype('category') 
dt1.Perm_10B_Shrub_10cm_Avg=pd.to_numeric(dt1.Perm_10B_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_10B_Shrub_10cm_Avg=dt1.Flag_Perm_10B_Shrub_10cm_Avg.astype('category') 
dt1.Perm_10C_Bare_10cm_Avg=pd.to_numeric(dt1.Perm_10C_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_10C_Bare_10cm_Avg=dt1.Flag_Perm_10C_Bare_10cm_Avg.astype('category') 
dt1.Perm_10C_Grass_10cm_Avg=pd.to_numeric(dt1.Perm_10C_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_10C_Grass_10cm_Avg=dt1.Flag_Perm_10C_Grass_10cm_Avg.astype('category') 
dt1.Perm_10C_Shrub_10cm_Avg=pd.to_numeric(dt1.Perm_10C_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_10C_Shrub_10cm_Avg=dt1.Flag_Perm_10C_Shrub_10cm_Avg.astype('category') 
dt1.Perm_10D_Bare_10cm_Avg=pd.to_numeric(dt1.Perm_10D_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_10D_Bare_10cm_Avg=dt1.Flag_Perm_10D_Bare_10cm_Avg.astype('category') 
dt1.Perm_10D_Grass_10cm_Avg=pd.to_numeric(dt1.Perm_10D_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_10D_Grass_10cm_Avg=dt1.Flag_Perm_10D_Grass_10cm_Avg.astype('category') 
dt1.Perm_10D_Shrub_10cm_Avg=pd.to_numeric(dt1.Perm_10D_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Perm_10D_Shrub_10cm_Avg=dt1.Flag_Perm_10D_Shrub_10cm_Avg.astype('category') 
dt1.Period_10A_Bare_10cm_Avg=pd.to_numeric(dt1.Period_10A_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Period_10A_Bare_10cm_Avg=dt1.Flag_Period_10A_Bare_10cm_Avg.astype('category') 
dt1.Period_10A_Grass_10cm_Avg=pd.to_numeric(dt1.Period_10A_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Period_10A_Grass_10cm_Avg=dt1.Flag_Period_10A_Grass_10cm_Avg.astype('category') 
dt1.Period_10A_Shrub_10cm_Avg=pd.to_numeric(dt1.Period_10A_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Period_10A_Shrub_10cm_Avg=dt1.Flag_Period_10A_Shrub_10cm_Avg.astype('category') 
dt1.Period_10B_Bare_10cm_Avg=pd.to_numeric(dt1.Period_10B_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Period_10B_Bare_10cm_Avg=dt1.Flag_Period_10B_Bare_10cm_Avg.astype('category') 
dt1.Period_10B_Grass_10cm_Avg=pd.to_numeric(dt1.Period_10B_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Period_10B_Grass_10cm_Avg=dt1.Flag_Period_10B_Grass_10cm_Avg.astype('category') 
dt1.Period_10B_Shrub_10cm_Avg=pd.to_numeric(dt1.Period_10B_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Period_10B_Shrub_10cm_Avg=dt1.Flag_Period_10B_Shrub_10cm_Avg.astype('category') 
dt1.Period_10C_Bare_10cm_Avg=pd.to_numeric(dt1.Period_10C_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Period_10C_Bare_10cm_Avg=dt1.Flag_Period_10C_Bare_10cm_Avg.astype('category') 
dt1.Period_10C_Grass_10cm_Avg=pd.to_numeric(dt1.Period_10C_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Period_10C_Grass_10cm_Avg=dt1.Flag_Period_10C_Grass_10cm_Avg.astype('category') 
dt1.Period_10C_Shrub_10cm_Avg=pd.to_numeric(dt1.Period_10C_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Period_10C_Shrub_10cm_Avg=dt1.Flag_Period_10C_Shrub_10cm_Avg.astype('category') 
dt1.Period_10D_Bare_10cm_Avg=pd.to_numeric(dt1.Period_10D_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Period_10D_Bare_10cm_Avg=dt1.Flag_Period_10D_Bare_10cm_Avg.astype('category') 
dt1.Period_10D_Grass_10cm_Avg=pd.to_numeric(dt1.Period_10D_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Period_10D_Grass_10cm_Avg=dt1.Flag_Period_10D_Grass_10cm_Avg.astype('category') 
dt1.Period_10D_Shrub_10cm_Avg=pd.to_numeric(dt1.Period_10D_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Period_10D_Shrub_10cm_Avg=dt1.Flag_Period_10D_Shrub_10cm_Avg.astype('category') 
dt1.Vratio_10A_Bare_10cm_Avg=pd.to_numeric(dt1.Vratio_10A_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_10A_Bare_10cm_Avg=dt1.Flag_Vratio_10A_Bare_10cm_Avg.astype('category') 
dt1.Vratio_10A_Grass_10cm_Avg=pd.to_numeric(dt1.Vratio_10A_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_10A_Grass_10cm_Avg=dt1.Flag_Vratio_10A_Grass_10cm_Avg.astype('category') 
dt1.Vratio_10A_Shrub_10cm_Avg=pd.to_numeric(dt1.Vratio_10A_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_10A_Shrub_10cm_Avg=dt1.Flag_Vratio_10A_Shrub_10cm_Avg.astype('category') 
dt1.Vratio_10B_Bare_10cm_Avg=pd.to_numeric(dt1.Vratio_10B_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_10B_Bare_10cm_Avg=dt1.Flag_Vratio_10B_Bare_10cm_Avg.astype('category') 
dt1.Vratio_10B_Grass_10cm_Avg=pd.to_numeric(dt1.Vratio_10B_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_10B_Grass_10cm_Avg=dt1.Flag_Vratio_10B_Grass_10cm_Avg.astype('category') 
dt1.Vratio_10B_Shrub_10cm_Avg=pd.to_numeric(dt1.Vratio_10B_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_10B_Shrub_10cm_Avg=dt1.Flag_Vratio_10B_Shrub_10cm_Avg.astype('category') 
dt1.Vratio_10C_Bare_10cm_Avg=pd.to_numeric(dt1.Vratio_10C_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_10C_Bare_10cm_Avg=dt1.Flag_Vratio_10C_Bare_10cm_Avg.astype('category') 
dt1.Vratio_10C_Grass_10cm_Avg=pd.to_numeric(dt1.Vratio_10C_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_10C_Grass_10cm_Avg=dt1.Flag_Vratio_10C_Grass_10cm_Avg.astype('category') 
dt1.Vratio_10C_Shrub_10cm_Avg=pd.to_numeric(dt1.Vratio_10C_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_10C_Shrub_10cm_Avg=dt1.Flag_Vratio_10C_Shrub_10cm_Avg.astype('category') 
dt1.Vratio_10D_Bare_10cm_Avg=pd.to_numeric(dt1.Vratio_10D_Bare_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_10D_Bare_10cm_Avg=dt1.Flag_Vratio_10D_Bare_10cm_Avg.astype('category') 
dt1.Vratio_10D_Grass_10cm_Avg=pd.to_numeric(dt1.Vratio_10D_Grass_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_10D_Grass_10cm_Avg=dt1.Flag_Vratio_10D_Grass_10cm_Avg.astype('category') 
dt1.Vratio_10D_Shrub_10cm_Avg=pd.to_numeric(dt1.Vratio_10D_Shrub_10cm_Avg,errors='coerce')  
dt1.Flag_Vratio_10D_Shrub_10cm_Avg=dt1.Flag_Vratio_10D_Shrub_10cm_Avg.astype('category') 
      
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
                    
print(dt1.Vwc_10A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_10A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_10A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_10A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_10A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_10A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_10B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_10B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_10B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_10B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_10B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_10B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_10C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_10C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_10C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_10C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_10C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_10C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_10D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_10D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_10D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_10D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vwc_10D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vwc_10D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_10A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_10A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_10A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_10A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_10A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_10A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_10B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_10B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_10B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_10B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_10B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_10B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_10C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_10C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_10C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_10C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_10C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_10C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_10D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_10D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_10D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_10D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Ec_10D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Ec_10D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_10A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_10A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_10A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_10A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_10A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_10A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_10B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_10B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_10B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_10B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_10B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_10B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_10C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_10C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_10C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_10C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_10C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_10C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_10D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_10D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_10D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_10D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Tsoil_10D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Tsoil_10D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_10A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_10A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_10A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_10A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_10A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_10A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_10B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_10B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_10B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_10B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_10B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_10B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_10C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_10C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_10C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_10C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_10C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_10C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_10D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_10D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_10D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_10D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Perm_10D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Perm_10D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_10A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_10A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_10A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_10A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_10A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_10A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_10B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_10B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_10B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_10B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_10B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_10B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_10C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_10C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_10C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_10C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_10C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_10C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_10D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_10D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_10D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_10D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Period_10D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Period_10D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_10A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_10A_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_10A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_10A_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_10A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_10A_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_10B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_10B_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_10B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_10B_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_10B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_10B_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_10C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_10C_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_10C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_10C_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_10C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_10C_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_10D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_10D_Bare_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_10D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_10D_Grass_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Vratio_10D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
print(dt1.Flag_Vratio_10D_Shrub_10cm_Avg.describe())               
print("--------------------\n\n")
                    
                    
                




