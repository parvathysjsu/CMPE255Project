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
 
## Description of the problem we will solve and the question we’ll investigate.
1. The trend of wildfires - Have they increased or decreased over the years. 
2. Main causes of the fire.
3. Geospatial visualization of the data.
4. Predict the area that will be affected given the region and year as input (Regression problem)

## Potential methods we will consider to apply On
### Washington Geospatial open Data Portal
1. Data Preparation - Removing anomalous values from the dataset, Eliminate columns whose values occur an abnormally large number of times as it does not contribute to analysing the data.
2. Extract number of wildfires that occur in each year to analyse the trend over time.
3. Identify maximum occurrence of the value(s) of cause column to uncover the major cause of fire in Washington region.
4. With the geojson file from the dataset, visualize the areas where the wildfires have occurred.
5. Using models like linear/polynomial regression or decision tree models to predict the area affected.

### Twitter data
1. Scrape the tweets related to wildfire and the duration of wildfires.
2. Data Preparation  - Extract relevant information from the tweets like region where the fire occurred, the year it happened, duration of the fire.
3. Analyze the duration of fire over the years.

## How will you measure success?
1. The analyzed output should match with the previously studied results.
2. Accurate visualization of the data.
3. Mean Square Error and accuracy.
