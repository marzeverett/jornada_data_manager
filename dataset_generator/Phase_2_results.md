
# Phase 2 Results 
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

Q. One datastream from one location was used to predict one datastream from one location using an LSTM network with data preprocessed by the autoencoders from H and fused together for each location.



## AE Separate Latent Space, Then Together Latent Space
### By datastream 
S. All datastreams from all locations are recreated from all datastreams from all locations, preprocessing and fusing input from the autoencoders in E. 

T. All datastreams from all locations are predicted from all datastreams from all locations, after being preprocessed by the autoencoder from S. 

U. All datastreams from one location are recreated from all datastreams from one location, preprocessing and fusing input from the autoencoders in H. 

V. All datastreams from one location are predicted from all datastreams from one location, after being preprocessed by the autoencoder from U. 

W. All datastreams from all locations are predicted from all datastreams from all locations, after being preprocessed by the autoencoder from U and fusing the locations. 

### By Location
X. All datastreams from all locations are recreated from all datastreams from all locations, preprocessing and fusing input from the autoencoders in L. (12 experiements)


Y. All datastreams from all locations are predicted from all datastreams from all locations, after being preprocessed by the autoencoder from X. 

Z. One datastream from all locations are recreated from one datastream from all locations, preprocessing and fusing input from the autoencoders in H. 

AA. One datastream from all locations are predicted from one datastream from all location, after being preprocessed by the autoencoder from Z. 

AB. All datastreams from all locations are predicted from all datastreams from all locations, after being preprocessed by the autoencoder from AA and fusing the locations. 

## AE, datatsreams/locations share Latent Space
### All together
AC.  All datastreams from all locations are recreated from all datastreams from all locations. 

AD. All datastreams from all locations are predicted from from all datastreams from all locations, after being preprocessed from the autoencoder from AC. 

### By datastream 
AE. All datastreams from one location are recreated from all datastreams from one location. 

AF. All datastreams from one location are predicted from all datatsreams from one location, after being preprocessed from the autoencoder from AE. 

AG. All datastreams from all locations are predicted from all datatstreams from all locations, after being preprocessed from the autoencoder from AE and fused together.

###  By location 
AH. One datastream from all locations is recreated from one datastream from all locations.

AI. One datastream from all locations is predicted from one datastream from all locations, after being preprocessed by the autencoder from AH. 

AJ. All datastreams from all locations are predicted from all datatstreams from all locations, after being preprocessed from the autoencoder from AI and fused together.



# Results (Predictions Only): 
## All datastreams predicted from all locations: 
### A (Base) (12 experiments)
Second Highest Mean MSE 
Second highest Max MSE 
### G (Separate Latent Space, Datastream) (12 experiments)
Second Lowest Mean MSE 
Second Highest Min MSE 
Second Lowest Max MSE 
Lowest Stdev 
### N (Separate Latent Space, Datastream) (12 experiments)
Lowest Min MSE 
highest Max MSE 

### T (Separate Latent Space on datastream, Then Combined Latent Space, fuse datastream) (12 experiments)
Second lowest stdev 

### W (Separate Latent Space Then Combined Latent Space, fuse datastream) (12 experiments)
Second Lowest Min MSE 
### Y  (Separate Latent Space Then Combined Latent Space (fuse location) (12 experiments)
Lowest Max MSE 
### AB  (Separate Latent Space Then Combined Latent Space, fuse location) (12 experiments)
Highest Mean MSE 
Highest Min MSE 
### AD (Shared Latent Space, all)  (12 experiments)
Lowest Mean MSE 
### AG (Shared Latent Datastream, fused) (12 experiments)
### AJ (Shared Latent Location, fused) (12 experiments)

Overall Min Mean mse: 0.01394
Overall Mean Mean mse: 0.014275 
Overall Min Min: 0.01064 
Overall Mean Min: 0.11559 

## All datastreams predicted from one location:
### B (Base) (180 experiments)
Lowest mean MSE 
Second lowest min (barely!)
Lowest max 

### J (Separate Latent Space, Datastream) (180 experiments)
### M (Separate Latent Space, Location) (180 experiments)
### V (Separate Latent Space, Then Together) (180 experiments)
### AF (Shared Latent) (180 experiments)
Second Lowest Mean MSE 
Lowest Min (barely!)
Second lowest max 


Overall Min Mean mse: 0.01392
Overall Mean Mean mse: 0.017728
Overall Min Min: 0.0055
Overall Mean Min: 0.008556 


## One datastream predicted from all locations:
### C (Base) (48 experiments)
Lowest Mean MSE 

### F (Separate Latent Space, Datastream) (48 experiments)
### Q (Separate Latent Space, Location) (48 experiments)
Second Lowest Mean MSE 
Second Lowest Min MSE 

### AA (Separate, then Together) (48 experiments)
### AI (Shared Latent Space) (48 experiments)
Lowest Min MSE



Overall Min Mean mse: 0.01557
Overall Mean Mean mse: 0.015748
Overall Min Min: 0.00204
Overall Mean Min: 0.002546 



## One datastream predicted from one location: 
### D (Case) (696 experiments)
Lower Mean 

### I (Separate Latent) (696 experiments)
Lower Min 

Overall Min Mean mse: 0.01515
Overall Mean Mean mse: 0.03099 (Doesn't mean much)
Overall Min Min: 0.00062
Overall Mean Min: 0.00071 (Doesn't mean much)


ToDo: Check variance by location and by datastream. 