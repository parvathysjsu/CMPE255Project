# CMPE255 Project - Wildfire Analysis and Prediction

## Team Members
1. Mohmmadsalman Mal :[salmanmal](https://github.com/salmanmal)
2. Parvathy Kannankumarath Madom Krishnan :[parvathysjsu](https://github.com/parvathysjsu)
3. Sanjana Srinivas :[Sanjana7395](https://github.com/Sanjana7395)
4. Sung-Yin Yang :[SungYinYang](https://github.com/SungYinYang)

## Dataset and Source
1. Dataset from Washington Geospatial open Data Portal.  
Source : https://geo.wa.gov/datasets/6f31b076628d4f8ca5a964cbefd2cccc_0/data?geometry=-140.484%2C41.510%2C-99.131%2C52.000    
2. Tweets on wildfire.  
Source : https://developer.twitter.com/en 
3. Drought data.
Source : https://droughtmonitor.unl.edu/

## Introduction
The year 2020 wreaked havoc in many states of the USA. Thus through this project, we analyze 
how the changes in climate is boosting the wildfires.The objective is to investigate following in Washington State - 
1. The trend of wildfires - Have they increased or decreased over the years. 
2. Main causes of the fire.
3. Overlaying the weather dataset with drought dataset in the region to identify the impact of drought in causing wildfires. We extract information about the intensity of the drought just before the wildfire to analyse the area that is being affected.  
4. Predict the area that will be affected given some useful variables as input (Regression problem)  
   
Predicting the area that could be affected by wildfire can help in preparing for the impending adversities.

## Method
### A. Preprocessing
Washington Geospatial open Data Portal      
1. Eliminate columns that does not contribute to analyzing the data.
2. Identify patterns, view distribution, fix outliers and missing values.

Twitter data
1. Scrape the tweets related to wildfire and the duration of wildfires.
2. Extract relevant information from the tweets like region where the fire occurred, 
the year it happened, duration of the fire.
3. Analyze the duration of fire over the years.

Drought data
1. Identify patterns, view distribution, fix outliers and missing values.
2. Extract duration and intensity of draught. Overlay accordingly with wildfire dataset.

### B. Method
We propose to predict the area affected by wildfire given input variables like - year,
fire start-date, region of fire, cause of fire, recently occurred draught intensity.
Following models are proposed to achieve the objective - 

Multiple Linear Regression      
This model helps in predicting a line that describes how the mean response changes with 
the input variables.

Decision Tree regression


## Expected Outcome
### A. Visualization
1. The increasing/decreasing trend of wildfires.
2. Major causes for wildfire in Washington region.

### B. Prediction result
1. Expected to achieve minimal root mean square error or an 
higher R-squared value on the test data.
