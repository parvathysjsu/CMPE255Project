# CMPE255 Project - Wildfire Analysis and Prediction

## Team Members
1. Mohmmadsalman Mal :[salmanmal](https://github.com/salmanmal)
2. Parvathy Kannankumarath Madom Krishnan :[parvathysjsu](https://github.com/parvathysjsu)
3. Sanjana Srinivas :[Sanjana7395](https://github.com/Sanjana7395)
4. Sung-Yin Yang :[SungYinYang](https://github.com/SungYinYang)

## Dataset and Source
1. Wildfires Dataset from Washington Geospatial Open Data Portal.  
Source : https://geo.wa.gov/datasets/6f31b076628d4f8ca5a964cbefd2cccc_0/data?geometry=-140.484%2C41.510%2C-99.131%2C52.000    
2. Temperature Dataset.     
Source : https://w2.weather.gov/climate/xmacis.php?wfo=sew

## Scrape wildfire data
Description

    run scraping code
    
## Preprocessing
### Wildfire data
The wildfire dataset from Washington Geospatial Open Data Portal contains information related to 
wildfires in Washington state from 1973-2019. The preprocessing is performed by running the below
code in the project directory 

    python preprocessing/wildfire_preprocessing.py
    
## Models
To predict the occurrence of a wildfire given the temperature data, the following models are used.
### Logistic regression
The model output can be visualized in model_visualization/logistic_regression

    python models/logistic_regression.py

