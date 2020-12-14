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

## Abstract
Wildfire is the most common form of a natural disaster. It is an unplanned and unwanted fire in areas with
combustible vegetation. Wildfires wreaked havoc in many states of the USA in the year 2020.
In this year alone, more than 8 million acres had been burnt. Wildfires affect forest cover, wildlife,
human habitat, and adversely influence climatic changes. A NICC report states that
on average, around 2500 homes are destroyed or impacted every year due to wildfires. Therefore, it
is essential to adopt measures to tackle this situation. Early detection or prediction
can promote early response, thereby minimizing the adversities caused by the fire. Through this project, we propose
a model to predict the occurrence of wildfire given the temperature and precipitation details of the region. 


## Experiments/Analysis
The experimentation involved preprocessing analysing the wildfire and temperature datasets, merging the two datasets and 
classifying the occurrence.

### Preprocessing wildfire dataset
The wildfire dataset consisted of a spreedsheet, which included the start and end date of the fire, cause, firename
etc and a geospatial shapefile which included the geographical points of the shape of the corresponding wildfire. To
use these data to analyze and predict the occurrence of wildfire the following preprocessing steps were performed - 
1. Removing unnecessary columns and redundant values (eg - 'human' and 'adult' in cause field), and rectifying spelling
errors in the spreadsheet.
2. Extracting the centre coordinate values from the geographical shapes in the shapefile. The centre coordinates are
used to identifying the city and county details of the corresponding wildfire.
3. Finally, the spreadsheet contents are mapped with its corresponding city and county values from the shapefile using
the common feature firename.

### Analysis/visualization of wildfire dataset

### Scraping, preprocessing and analysis of temperature dataset

### Merging the wildfire and temperature dataset

### Analysis of merged data
The objective of the classification model is to predict the occurrence of wildfire given the weather details of
the region. The input features include - temperatures (min, max, hdd and cdd) and precipitation. The relation between
the input features - max_temperature and precipitation - with the output data is shown below - 
<table>
  <tr>
    <td>Max temperature with output</td>
    <td>Precipitation with output</td>
  </tr>
  <tr>
    <td><img src="model_visualization/logistic_regression/max_temperature_relation.png" width=400 height=300></td>
    <td><img src="model_visualization/logistic_regression/percipitation_relation.png" width=400 height=300></td>
  </tr>
 </table>
 
 From the figure we see that the temperature has positive relation with the occurrence of wildfire i.e. as the
 temperature increases the probability of the wildfire occurrence is high. And precipitation has a negative
 relation - the lower the precipitation value in the region, the higher the probability of wildfire occurrence.

### Data Ratios

## Comparisons
### Decision Trees

Dataset Data Ratio | Accuracy | Confusion Matrix
------------ | ------------- | -------------
1:1 | 88.1% | <img src="model_visualization/decision_tree/confusion_matrix.png" />
1:2 | 92.04% | <img src="model_visualization/decision_tree/confusion_matrix_2.png" />
1:4 | 94.07% | <img src="model_visualization/decision_tree/confusion_matrix_4.png" />
1:8 | 95.22% | <img src="model_visualization/decision_tree/confusion_matrix_8.png" />
1:16 | 97.75% | <img src="model_visualization/decision_tree/confusion_matrix_16.png" />
1:32 | 98.75% | <img src="model_visualization/decision_tree/confusion_matrix_32.png" />
1:300 | 99.89% | <img src="model_visualization/decision_tree/confusion_matrix_300.png" />

## Conclusion

