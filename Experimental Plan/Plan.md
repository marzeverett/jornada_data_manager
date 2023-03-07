# Experimental Plan Considerations 

## What to Measure? What Data to Use

### Regression 

1. Site Next-Day Weather 
    Day Prior
    Week Prior
    Month Prior
    Year Prior? 
    Last Month for x amount of years?
    All the data? 
    
2. Site Next-Week Weather 
    Week Prior
    Month Prior
    Year Prior? 
    Last Month for x amount of years?
    All the data? 

3. Site Next-Month Weather
    Month Prior
    Year Prior? 
    Last Month for x amount of years?
    All the data? 

4. Same as above, for soil moisture content 
5. Same as above, for precipitation 

### Classification 

1. Vegetative Cover
2. Animal Presence
3. Dust 


## To Do 
- [ ] Figure out what data streams go where
- [ ] Get rid of NaNs/Clean Data
- [ ] Auto script to spatially align data 
- [ ] Auto script to pull in and out data streams as needed 
- [ ] Research best LSTM and AE practices
- [ ] Auto script for time refactoring
- [ ] Auto script to run models 
- [ ] Exactly how many models to run, figure out how to auto re-run 
- [ ] Auto-save, auto-evaluate models 
- [ ] Auto-save latent space to own datasets as needed 