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
a model to identify the occurrence of wildfire given the temperature and precipitation details of the region. Four
different models are used namely - Logistic regression, KNN, SVM and Decision tree. From the experiments we have
identified that the Decision tree model performed the best with an accuracy of 94.07% and F1 score of 0.86 


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
Analysing the wildfire dataset we observed that -   <br>
1. There is an increasing trend in the occurrence of wildfires over the years from 1973 to 2019 as shown in the graph below. The maximum number was recorded in 2015 with over 70 wildfires.
<img src="graphs/wildfire_year_wise_chart.png" />
2. From the figure below we observe that major known cause of wildfires in the Washington state is mostly Lightening. This has accounted for almost 200 fires in the region. The other major causes of fire are human induced and arson. 
<img src="graphs/wildfire_causes_chart.png" >
3. Chelan county tops the list of wildfires per county with over 100 fires. Its followed by Okanogan county, Spokane county, and Klickitat county all having over 50 fires.
4. The figure shows a map of Washington state with all the areas that had wildfires. This map is constructed using the shape file that had coordinates for the locations.
<img src="graphs/wildfires_map.PNG"  />


### Scraping, preprocessing and analysis of temperature dataset
#### Salman Mal

### Merging the wildfire and temperature dataset
#### Steven

### Adding negative data
#### Data Ratios(Steven)

### Analysis of merged data
#### Salman Mal (Correlation Matrix)
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

### Classification models
We have four classification models to identify the occurrence of wildfire given the weather details - temperatures(max,
avg, min, hdd, cdd) and precipitation - of the region. The following are the models used - 

#### 1. Logistic regression  
Identifying the occurrence of wildfire is a binary classification problem which can be trained using a 
simple logistic regression model. The below experiments were performed to improve the performance of the model
    - Initially, the input data was trained using sklearn LogisticRegression().
    - The input data was normalized to scale before being fed into the model. This helped in removing anomalies and 
grouping the similar data together.
    - GridSearchCV - The hyperparameters of the model namely - C, scaler and penalty were experimented with different
variation to find the optimal values. The best results were obtained using C=10, scaler='liblinear' and penalty='l2'. 
     
    The results of the above experiments are recorded in the table below  
    <table>
      <tr>
        <td>Experiments</td>
        <td>Accuracy (%)</td>
      </tr>
      <tr>
        <td>Initial model</td>
        <td>70.00</td>
      </tr>
      <tr>
        <td>Normalizing input data</td>
        <td>75.12</td>
      </tr>
      <tr>
        <td>Hyperparameter search</td>
        <td>77.62</td>
      </tr>
     </table>
    The t-SNE plot of the dataset is shown below.

    <img src="model_visualization/logistic_regression/tsne.png" />

    From the t-SNE plot, we observe that the data is not easily separable. Therefore, we need a more sophisticated
    model to classify the occurrence of wildfire.

#### 2. KNN

#### 3. SVM

#### 4. Decision Trees

Preprocessing of data was done to remove unnecessary columns like start and end dates, acres, shapearea etc. 
The model analysis process started with data split into training and testing datasets with 8:2 ratio using sklearn.model_selection.train_test_split. The model used was sklearn.tree.DecisionTreeClassifier and it was trained using the training data. And the outcome was predicted for the test data and then compared with the expected result. This process was repeated multiple times once for each dataset of varying positive and negative data ratios. The results of those different datasets is given below.

Dataset Data Ratio | Accuracy | F1 Score
------------ | ------------- | -------------
1:1 | 88.1% | 0.89
1:2 | 92.04% | 0.88
1:4 | 94.07% | 0.86
1:8 | 95.22% | 0.78
1:16 | 97.75% | 0.79
1:32 | 98.75% | 0.81
1:300 | 99.89% | 0.79

An accuracy of over 99% was achieved with 1:300 ratio dataset, but it had lower F1 score and more false positives. The 1:1 ratio dataset had the lowest accuracy of 88%, but the fewest false positives and highest F1 score. As the count of negative data increased, accuracy increased, but number of false positives also increased and F1 score decreased. On an average, the dataset with best combination of accuracy and F1 score is selected as the 1:4 ratio dataset. The confusion matrix is shown below.

<img src="model_visualization/decision_tree/confusion_matrix_4.png" >
<br>The decision tree of the 1:4 ratio dataset is plotted below using sklearn.tree.plot_tree function.
<img src="model_visualization/decision_tree/decistion_tree_4.png" >

## Comparisons
Below are the consolidated performance of different models.
<table>
  <tr>
    <td>Classification models</td>
    <td>Accuracy (%)</td>
    <td>F1-Score</td>
  </tr>
  <tr>
    <td>Linear regression</td>
    <td>77.62</td>
    <td>0.75</td>
  </tr>
  <tr>
    <td>KNN</td>
    <td>75.12</td>
    <td>77.62</td>
  </tr>
  <tr>
    <td>SVM</td>
    <td>77.62</td>
    <td>77.62</td>
  </tr>
  <tr>
    <td>Decision tree</td>
    <td>94.07</td>
    <td>0.86</td>
  </tr>
 </table>

## Conclusion
From the above experiments, Decision Tree best identifies the occurrence of
wildfire with accuracy of 94.07% and F1 score of 0.86 

## Future Recommendations
There is scope for improving the performance of classification model with the help of - 
1. Availability of more wildfire data - This can promote the use of complex deep learning model to achieve exemplary
performance
2. Addition of input weather features, so to achieve a more separable cluster. 

