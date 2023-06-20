All – 0
One – 1
Datastream, Location 
Count in Binary 

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
------- Not really implementing
K. LSTM fusing together AE datastream separate and together? 

L. AE All locations separately (all datastreams)
M. LSTM on top of each AE location, separately (all datastreams)
N. LSTM fusing together AE locations (all datastreams) 
------------- Already technically done -------------- (H) 
O. AE All locations separately (one datastream)
P. LSTM on top of each AE location, separately (one datastream)
------------------

Q. LSTM fusing together AE locations (one datastream) 
------ Not really implementing 
R. LSTM fusing together AE datastream separate and together? 

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

Spatial Models:
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

