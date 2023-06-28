We have here 15 locations and 4 "streams" of data. 

Base: 
A. (Base) All datastreams, all locations to LSTM
B. (Base) All datastreams, one location to LSTM 
C. (Base) One datastream, all locations to LSTM 
D. (Base) One datastream, one location to LSTM 

AE Separate Latent Space 
E. AE All datastreams separately (all locations)
F. LSTM on top of each AE datastreams, separately (all locations)
G. LSTM fusing together AE datastreams (all locations) 
H. AE All datastreams separately (one location)
I. LSTM on top of each AE datastreams, separately (one location)
J. LSTM fusing together AE datastreams (one location) 
------- Not implemented
K. LSTM fusing together AE datastream separate and together? 
------- End 

L. AE All locations separately (all datastreams)
M. LSTM on top of each AE location, separately (all datastreams)
N. LSTM fusing together AE locations (all datastreams) 
------------- Already technically done -------------- (H) 
O. AE All locations separately (one datastream)
P. LSTM on top of each AE location, separately (one datastream)
------------------ End 

Q. LSTM fusing together AE locations (one datastream) 
------ Not really implementing 
R. LSTM fusing together AE datastream separate and together? 
------- End 


AE Separate Latent Space, Then Together Latent Space
S. AE on top on ALL individual AE datastreams, all locations 
T. LSTM on top of S
U. AE on top of ALL individual AE datastreams, one location
V. LSTM on top of U
W. LSTM using U and fusing all locations 

X. AE on top of ALL individual AE locations, all datastreams
Y. LSTM on top of X
Z. AE on top of ALL individual AE locations, one datastream 
AA. LSTM on top of Z
AB. LSTM fusing all datastreams from AA. 


AE together Latent Space
AC.  AE on top of ALL datastreams, all locations
AD. LSTM on top of AC
AE. AE on top of ALL datastreams, one location 
AF. LSTM on top of AE
AG. LSTM fusing locations from AF
AH. AE on top of ALL locations, one datastream
AI. LSTM on top of AH
AJ. LSTM fusing datastreams from AI

Spatial Models: (Repeats)
A.
C.

F.
G.

N.
Q.

T.
W.

Y.
AA.
AB. 

AD. 
AG. 
AI.
AJ. 



### Better format 

We have here 15 locations and 4 "streams" of data. 

The NPP site locations:  
    ["c_cali", "c_grav", "c_sand", "g_basn", "g_ibpe", "g_summ", "m_nort", "m_rabb", "m_well", "p_coll", "p_smal", "p_tobo", "t_east", "t_tayl", "t_west"]

The 4 datastreams and the fields they include: 

    separate_data_streams = {
        "temp_hum": ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max', 'Relative_Humidity_Min'],
        "rain": ['Ppt_mm_Tot'],
        "wind_speed": ['WS_ms_300cm_Avg', 'WS_ms_300cm_Max', 'WS_ms_150cm_Avg', 'WS_ms_150cm_Max', 'WS_ms_75cm_Avg', 'WS_ms_75cm_Max'],
        "wind_direction": ['WinDir_mean_Resultant', 'WinDir_Std_Dev'],
    }



Here are the experiments that were run: (First Phase) 
--------------------------------------------
All experiments were tried with every combo of 30 or 60 inputs days and 1 or 7 output prediction days. 

All LSTM experiments were repeated with 8, 32, and 64 lstm nodes in one layer. 

All AE experiments with 30, 50, and 70% of the number of input fields. 

All LSTM networks that used AE preprocessing used the model with 50% of the input nodes for this phase. 

## Base: 
A. All datastreams from all locations were used to predict all datatstreams at all locations. A normal LSTM network was used. 

B. All datastreams from one location were used to predict all datastreams at that one location. A normal LSTM networks was used. 

C. One datastream from all locations was used to predict one datastream from all locations. A normal LSTM network was used. 

D. One datastream from one location was used to predict one datastream from one locations. A normal LSTM network was used. 

## AE Separate Latent Space 
### By Datastream
E. One datastream from all locations was used to recreate one datastream from all locations, using an autoencoder. 

F. One datastream from all locations was used to predict one datastream from all locations, using an LSTM network with data preprocessed by the autoencoders from E. 


G. All datastreams from all locations were used to predict all datastreams from all locations using an LSTM network with data preprocessed by the autoencoders from E and fused together for each datastream.

H.  One datastream from one location was used to recreate one datastream from one locations, using an autoencoder.

I. One datastream from one location was used to predict one datastream from one location, using an LSTM network with data preprocessed by the autoencoders from H. 


J. All datastreams from one location were used to predict all datastreams from one location using an LSTM network with data preprocessed by the autoencoders from H and fused together for each datastream.

### By Location 
L. All datastreams from one locations were used to recreate all datastream from one location, using an autoencoder.

M. All datastreams from one location were used to predict all datastream from one locations, using an LSTM network with data preprocessed by the autoencoders from L. 

N. All datastreams from all locations were used to predict all datastreams from all locations using an LSTM network with data preprocessed by the autoencoders from L and fused together for each location.

Q. One datastream from all locations was used to predict one datastream from all location using an LSTM network with data preprocessed by the autoencoders from H and fused together for each location.

### Missing Experiment Here! R - 


## AE Separate Latent Space, Then Together Latent Space
### By datastream 
S. All datastreams from all locations are recreated from all datastreams from all locations, preprocessing and fusing input from the autoencoders in E. 

T. All datastreams from all locations are predicted from all datastreams from all locations, after being preprocessed by the autoencoder from S. 

U. All datastreams from one location are recreated from all datastreams from one location, preprocessing and fusing input from the autoencoders in H. 

V. All datastreams from one location are predicted from all datastreams from one location, after being preprocessed by the autoencoder from U. 

W. All datastreams from all locations are predicted from all datastreams from all locations, after being preprocessed by the autoencoder from U and fusing the locations. 

### By Location
X. All datastreams from all locations are recreated from all datastreams from all locations, preprocessing and fusing input from the autoencoders in L. 

Y. All datastreams from all locations are predicted from all datastreams from all locations, after being preprocessed by the autoencoder from X. 

Z. One datastream from all locations are recreated from one datastream from all locations, preprocessing and fusing input from the autoencoders in H. 

AA. One datastream from all locations are predicted from one datastream from all location, after being preprocessed by the autoencoder from Z. 

AB. All datastreams from all locations are predicted from all datastreams from all locations, after being preprocessed by the autoencoder from AA and fusing the locations. 

## AE, datastreams/locations share Latent Space
AC.  All datastreams from all locations are recreated from all datastreams from all locations. 

AD. All datastreams from all locations are predicted from from all datastreams from all locations, after being preprocessed from the autoencoder from AC. 

AE. All datastreams from one location are recreated from all datastreams from one location. 

AF. All datastreams from one location are predicted from all datastreams from one location, after being preprocessed from the autoencoder from AE. 

AG. All datastreams from all locations are predicted from all datatstreams from all locations, after being preprocessed from the autoencoder from AE and fused together.

AH. One datastream from all locations is recreated from one datastream from all locations.

AI. One datastream from all locations is predicted from one datastream from all locations, after being preprocessed by the autencoder from AH. 

AJ. All datastreams from all locations are predicted from all datatstreams from all locations, after being preprocessed from the autoencoder from AI and fused together.



