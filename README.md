# CMPE255 Project - Wildfire Analysis and Prediction

## Team Members
1. Mohmmadsalman Mal :[salmanmal](https://github.com/salmanmal)
2. Parvathy Kannankumarath Madom Krishnan :[parvathysjsu](https://github.com/parvathysjsu)
3. Sanjana Srinivas :[Sanjana7395](https://github.com/Sanjana7395)
4. Sung-Yin Yang :[SungYinYang](https://github.com/SungYinYang)

## Dataset and Source
1. Dataset from Washington Geospatial open Data Portal.  
Source : https://geo.wa.gov/datasets/6f31b076628d4f8ca5a964cbefd2cccc_0/data?geometry=-140.484%2C41.510%2C-99.131%2C52.000    
2. Temperature dataset.     
Source : https://w2.weather.gov/climate/xmacis.php?wfo=sew

## Preliminary Analysis
Washington Geospatial open Data Portal
From figure 1 we observe an increasing trend in the occurrence of wildfires over the years from 1973 to 2019.
2. Fig 

## Introduction
The year 2020 wreaked havoc in many states of the USA. Thus through this project, we analyze 
how the climate changes are worsening the wildfires. The objective is to investigate the 
following in the state of Washington:
1. The trend of wildfires - Have they increased or decreased over the years. 
2. Main causes of the fire.
3. Analyse the past wildfire occurrence to identify the regions prone to wildfire.
4. Analyse the effect of weather on the spread of wildfire.
5. Overlaying the temperature dataset in the region to predict the probability of the wildfire occurrence
given the weather details of the region.

## Method
### A. Preprocessing
Washington Geospatial open Data Portal      
1. Eliminate columns that do not contribute to analyzing the data.
2. Identify patterns, view distribution, fix outliers, and missing values.

Temperature data
1. Extract weather data for each city in Washington State through API.
2. Eliminate unnecessary columns and clean the dataset.

### B. Data Overlaying
Overlay the attributes of different datasets to feed as input to the model.

### B. Model
We propose to predict the probability of the occurrence of wildfire given area and weather 
conditions as input Following models are proposed to achieve the objective - 

Logistic Regression    
This model helps in predicting the probability of event success or failure. The major limitation of
this method is the assumption of linearity between input and output variables. 

Decision Tree       
Decision tree uses tree-like model to decide on predicting possible outcomes. Missing values
in the data are handled well. However, the training time is higher and is more prone to
over-fitting.

Convolution Neural Network      
The CNN model will learn a function that maps the sequence of input observations to predict
the occurrence of wildfire. The estimated predictive accuracy will be good. However, it mostly
performs well on a large datasets.


## Expected Outcome
### A. Visualization
1. The increasing/decreasing trend of wildfires.
2. Major causes for wildfire in th Washington region.

### B. Prediction result
1. The wildfire dataset constituent of only the positive occurrences and not negative occurrences.
Therefore there exists a class imbalance. This is eliminated by adding negative occurrence data.
The outcome of the classifier is expected to predict a range of probability from 0-1(wildfire occurred
or not)
2. Expected to achieve good accuracy on the test data.
