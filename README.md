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

# How to Run Code?

## Scrape temperature data
[weather_scrapper.py](./data/weather_scrapper.py) downloads data from api and preprocesses and saves it in [weather_data.csv](./data/weather_data.csv)
```
# on mac run the following command from the git repo's root directory

python ./data/weather_scrapper.py

```

    
## Preprocessing
### Wildfire data
The wildfire dataset from Washington Geospatial Open Data Portal contains information related to 
wildfires in Washington state from 1973-2019. The preprocessing is performed by running the below
code in the project directory 
```
    python preprocessing/wildfire_preprocessing.py
    
    # to visualize wildfire dataset run below script. The visualization images are saved in the graphs/ directory.
    python preprocessing/wildfire_dataset_visualization.py
    
 ```   
    
    
### Visualization Code
[weather_dataset_visualization.py](./preprocessing/weather_dataset_visualization.py) runs the analysis on temperature dataset and saves the relevant graph in the [graphs](./graphs) directory.
```
# on mac run the following command from the git repo's root directory 
python ./preprocessing/weather_dataset_visualization.py
```

### Merge wildfire and temperature data
[Combine_two_data.ipynb](./mergeingData/Combine_two_data.ipynb) merge the wildfire and temperature dataset
```
# run the notebook file in mergeingData/Combine_two_data.ipynb
```

## Models
To predict the occurrence of a wildfire given the temperature data, the following models are used.
### Logistic Regression
The model output can be visualized in model_visualization/logistic_regression

    python models/logistic_regression.py


### KNN Classifier
[knn_classifier.py](./models/knn_classifier.py) runs the K nearest neighbor implementation of SKlearn library for multiple dataset with different positive and negative data ratio and saves the confusion matrix and other graphs in [./model_visualization/knn_classifier](./model_visualization/knn_classifier) directory.
```
# on mac run the following command to navigate to ./models directory

cd models

# Run the following command to run the script

python knn_classifier.py


# running python models/knn_classifier.py could throw path not found exception
```

### SVM Classifier
[svm.ipynb](./models/svm.ipynb) runs the C-Support Vector Classification of SKlearn library for multiple dataset with different positive and negative data ratio and saves the confusion matrix.

```
# Use anaconda to open .ipynb files

# All of the running result are saved in the jupyter notebook
# To rerun all of the result, simply click Run All in the jupyter notebook
```

### Decision Tree
[decision_tree.ipynb](./models/decision_tree.ipynb) is the Decision Tree implementation code for the dataset. It can be run for different datasets with varying positive and negative data ratios by providing the dataset csv filename in the notebook. It saves the confusion matrix and other graphs in [./model_visualization/decision_tree](./model_visualization/decision_tree) directory.

```
# Use anaconda to open .ipynb files

# All of the running result are saved in the jupyter notebook
# To rerun all of the result, simply click Run All in the jupyter notebook
```


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
different models are used namely - Logistic regression, KNN, SVM, and Decision tree. From the experiments, we have
identified that the Decision tree model performed the best with an accuracy of 94.07% and an F1 score of 0.86 


## Experiments/Analysis
The experimentation involved preprocessing analyzing the wildfire and temperature datasets, merging the two datasets and 
classifying the occurrence.

### Preprocessing wildfire dataset
The wildfire dataset consisted of a spreadsheet, which included the start and end date of the fire, cause, firename
etc and a geospatial shapefile which included the geographical points of the shape of the corresponding wildfire. To
use these data to analyze and predict the occurrence of wildfire the following preprocessing steps were performed - 
1. Removing unnecessary columns and redundant values (eg - 'human' and 'adult' in cause field), and rectifying spelling
errors in the spreadsheet.
2. Extracting the center coordinate values from the geographical shapes in the shapefile. The center coordinates are
used to identify the city and county details of the corresponding wildfire.
3. Finally, the spreadsheet contents are mapped with its corresponding city and county values from the shapefile using
the common feature firename.

### Analysis and visualization of wildfire dataset
Analyzing the wildfire dataset we observed that -   <br>
1. There is an increasing trend in the occurrence of wildfires over the years from 1973 to 2019 as shown in the graph below. The maximum number was recorded in 2015 with over 70 wildfires.

<table>
  <tr>
    <td>Wildfires over the years</td>
    <td>Causes of wildfires</td>
  </tr>
  <tr>
    <td><img src="graphs/wildfire_year_wise_chart.png"></td>
    <td><img src="graphs/wildfire_causes_chart.png" width=700 height=300></td>
  </tr>
 </table>
2. From the figure below we observe that major known cause of wildfires in the Washington state is mostly Lightening. This has accounted for almost 200 fires in the region. The other major causes of fire are human induced and arson. 
3. Chelan county tops the list of wildfires per county with over 100 fires. Its followed by Okanogan county, Spokane county, and Klickitat county all having over 50 fires.
4. The figure shows a map of Washington state with all the areas that had wildfires. This map is constructed using the shape file that had coordinates for the locations.
<img src="graphs/wildfires_map.PNG"  />


### Scraping, preprocessing, and analysis of temperature dataset

To analyze the correlation between these wildfires and weather, we extracted the past 20 years' weather data from https://w2.weather.gov for all the weather stations in Washington state using our [wather_scrapper.py](data/weather_scrapper.py) script. 

The process of extracting and cleaning the data involved -

* Understanding the REST API request body and finding Washington state's weather station ids.
* Removed records which had missing values of temperature, precipitation, and other attributes.
* Append station ids and station names to later identify county and city, which will eventually help in merging the wildfire and weather data.
* Saved as [weather_data.csv](data/weather_data.csv) to later analyze and merge with wildfire dataset.

Analyzing the temperature dataset we observed that -
*  The following mean temperature over the years graph shows the history of average temperature over the last 20 years period. From the data, it is evident that there is a rise in average temperature over this period with some fluctuation. Between the period 2011 to 2015 temperature had a steep rise from 55 °F to 62 °F.
On comparing both of the following graphs, we can clearly see the positive relationship between temperature and the number of wildfires in that year. The year 2015 had a record-breaking average temperature of 62 °F and a maximum number of wildfires.
 
 <img src="graphs/avg_temp_over_the_years.png" />
 <img src="graphs/wildfire_year_wise_chart.png" />
 
*  The following graph shows the max temperature over the years. The max temperature over the period has risen from 96 °F to 105 °F. The spike in the year 2007 lies way beyond the normal distance from the others and could easily be identified as an outlier. To reduce such a misleading sample, instead of taking max from the year, in training the model we decided to take the average of the first 10 max values for that year.
 
 <img src="graphs/max_temp_over_the_years.png" />
 

### Merging the wildfire and temperature dataset
#### Merged dataset  
In our wildfire dataset, there is no weather information such as temperature, humidity, and precipitation. Thus, we need to merge the weather dataset and the wildfire dataset.

The two datasets would be merged based on the location of the time and the range of the wildfire date. Additional cleaning in the weather dataset and forest dataset is required. The goal is to add new attributes such as max_temperature, min_temperature, average_temperature, average_precipitation, average_humid_degree, average_cooling_degreeday into the wildfire dataset.

Additional cleaning in Weather Dataset involved:
* Remove rows with 'M' values in max_temperature, min_temperature, avg_temperature departure_temperature, hdd, cdd, and precipitation columns.
* Remove non-numeric value in the numeric attribute field.
* Add latitude coordinates and longitude coordinates for each station.
* Update the date attribute to the format of Python Time Object for better comparison.

The following pictures show examples of the weather dataset.

<img src="graphs/weather_example1.png" />
<img src="graphs/weather_example2.png" />

Additional cleaning in Wildfire Dataset involved:
* Add Attribute "Centroid," which is calculated based on the geometry polygon given by the geojson file.
* Add Attribute "nearest Station." Euclidean distance is used to calculate the nearest weather station where the wildfire happens. This attribute contains the longitude and latitude coordinates of the station.
* Update the date attribute to the format of Python Time Object for better comparison.

The following picture shows the added attribute.

<img src="graphs/wild_fire_example.png" />

Steps of merging the two dataset
* First, additional cleaning would be performed on the two datasets.
* Second, each wildfire record would map to rows of weather data based on the nearest station. The rows of weather data would be the range of the date that the wildfire is happening.
* Finally, the average value of the weather data would be calculated and add to the wildfire dataset.

The following pictures show the merged dataset.

<img src="graphs/merge_data_example1.png" />
<img src="graphs/merge_data_example2.png" />

### Adding negative data
Since we only have the dataset that has the wildfire occurs, we need to add some negative data (weather data that does not has wildfire occur) into our dataset for training.

For experiment purposes, we are not sure how many negative data need to be added. Thus, we add a different ratio of negative data into our final dataset. 
In the folder data/preprocessed, many datasets start with a number such as 1.csv, 2.csv, 4.csv, 8.csv, 16.csv, 32.csv, 64.csv.
The number means the ratio of positive data to negative data is 1 to that number. For example, 4.csv implies that the rate of positive data and the negative dataset is 1 to 4.

The negative data are added by randomly choosing other days that do not have wildfire for each positive data. For example, if a wildfire happened at latitude -121.33 and longitude 46.1, then our final data set would randomly add another day's weather information from that location. The negative ratio determines how many random weather data was added for each wildfire occurrence.

<p float="left">
  <img src="https://github.com/parvathysjsu/CMPE255Project/blob/main/graphs/weather_info0.png" width="350" />
  <img src="https://github.com/parvathysjsu/CMPE255Project/blob/main/graphs/weather_info1.png" width="350" /> 
</p>

The left graph above represents one of the positive data. The right graph represents the added negative data, which is a randomly chosen day from the weather dataset with the same latitude and longitude information.

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
 
 From the figure we see that the temperature has a positive relationship with the occurrence of wildfire i.e. as the
 temperature increases the probability of the wildfire occurrence is high. And precipitation has a negative relation - the lower the precipitation value in the region, the higher the probability of wildfire occurrence.

#### Correlation Matrix

This shows correlations between the stated importance of various things to people. The line of 1.00s going from the top left to the bottom right is the main diagonal, which shows that each variable always perfectly correlates with itself. This matrix is symmetrical, with the same correlation is shown above the main diagonal being a mirror image of those below the main diagonal. Correlation matrix changes with the proportion of negative data in the dataset. 
<table>
<tr>
<td>Positive-negative data ration</td>
<td>Correlation Matrix</td>
</tr>
<tr>
<td>1:1</td>
<td><img src="model_visualization/knn_classifier/1/correlation_matrix.png"  /></td>
</tr>
<tr>
<td>1:2</td>
<td><img src="model_visualization/knn_classifier/2/correlation_matrix.png"  /></td>
</tr>
<tr>
<td>1:4</td>
<td><img src="model_visualization/knn_classifier/4/correlation_matrix.png"  /></td>
</tr>
<tr>
<td>1:8</td>
<td><img src="model_visualization/knn_classifier/8/correlation_matrix.png"  /></td>
</tr>
<tr>
<td>1:16</td>
<td><img src="model_visualization/knn_classifier/16/correlation_matrix.png"  /></td>
</tr>
<tr>
<td>1:32</td>
<td><img src="model_visualization/knn_classifier/32/correlation_matrix.png"  /></td>
</tr>
<tr>
<td>1:300</td>
<td><img src="model_visualization/knn_classifier/300/correlation_matrix.png"  /></td>
</tr>
</table>

### Classification models
We have four classification models to identify the occurrence of wildfire given the weather details - temperatures(max,
avg, min, hdd, cdd) and precipitation - of the region. The following are the models used - 

#### 1. Logistic regression  
Identifying the occurrence of wildfire is a binary classification problem that can be trained using a 
simple logistic regression model. The below experiments were performed to improve the performance of the model
- Initially, the input data was trained using sklearn LogisticRegression().
- The input data was normalized to scale before being fed into the model. This helped in removing anomalies and 
grouping similar data together.
- GridSearchCV - The hyperparameters of the model namely - C, scaler, and penalty were experimented with different
variations to find the optimal values. The best results were obtained using C=10, scaler='liblinear' and penalty='l2'.
- Polynomial feature transform - Since the separation between the clusters is not linear, a polynomial feature
transform was performed to improve the process of fitting an appropriate curve to classify the data. 
     
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
  <tr>
     <td>Polynomial feature transform</td>
     <td>84.29</td>
  </tr>
</table>
The confusion matrix of the final model is given by - 

<img src="model_visualization/logistic_regression/confusion_matrix.png"  width=400 height=300/>

The t-SNE plot of the dataset is shown below.

<img src="model_visualization/logistic_regression/tsne.png" width=400 height=300/ />

From the t-SNE plot, we observe that the data is not easily separable. Therefore, we need a more sophisticated
model to classify the occurrence of wildfire.

#### 2. K Nearest Neighbor (KNN)
In KNN classification, the output is a class membership. An object is classified by a plurality vote of its neighbors, with the object being assigned to the class most common among its k nearest neighbors (k is a positive integer, typically small). 

Trained model for all ratio dataset for weight(hyperparameter) value uniform and distance. In distance weight, the algorithm assigns weights to the contributions of the neighbors, so that the nearer neighbors contribute more to the average than the more distant ones. For example, a common weighting scheme consists of giving each neighbor a weight of 1/d, where d is the distance to the neighbor. In uniform weights, all nearest object contributes the same to the classification. As the negative data ratio is increased the accuracy is increasing and the F1 score and AUC score are inversely affected. Below are the metrics for each iteration.
- Red is the lowest in the column
- Greens are the max in the column
- Yellow highlights the optimal model with a tradeoff between accuracy and F1 score.
<img src="model_visualization/knn_classifier/metrics_comparison.png"  alt="KNN metrics Comparison"/>

- Confusion matrix for optimal model
<img src="model_visualization/knn_classifier/4/distance_weight/confusion_matrix.png">

Distance weighted classification is performing well over the uniform weighted classification. Though accuracy is good, the False Positive rate is higher and that negatively affects the precision. 

#### 3. SVM

After removing unnecessary columns like start, end, acres, and shape area, there are still 7 attributes left. 
The remaining attributes are max_temperature, min_temperature, avg_temperature, departure temperature, hdd, cdd, precipitation.

The default SVM model is running on the kernel "rbf". Different ratios of the dataset are applied to the default model. 
The result shows a reasonable accuracy, ROC, and F1 score when the negative ratio is low. However, as more negative data added, the F1 score decrease fast.
The default SVM model even reaches an F1 score = 0 when the ratio of pos to neg is 300. 

<img src="graphs/attribute_comparison.png" width=560 height=400/>

Notice that by adding more negative data, the dataset would become more unbalanced. 
In wildfire detection, it is more important to correctly label an occurrence as wildfire, as opposed to labeling the non-wildfire one. 
Thus, it is better to pick a classifier that has a decentF1 score. In order to solve the decreasing F1 score, three attributes are eliminated.
The training result shows that using four attributes receive a better F1 score than using all the seven attributes.

Later then, using only four attributes, multiple SVM kernels such as 'rbf', 'linear', and 'sigmoid' are trained and compared with each other.

<img src="graphs/svm_model.png" width=560 height=400/>

As the graph above shown, the accuracy increases as more negative data were added.
Conversely, the F1 score decreases as more negative data were added.
Overall the rbf kernel reaches the best performance in the SVM model with high accuracy and a decent F1-Score.
Notice that linear kernel also achieves a decent F1 score. It can be interpreted that the dataset that we used does not have a high dimension.



#### 4. Decision Trees

Preprocessing of data was done to remove unnecessary columns like start and end dates, acres, shapearea, etc. 
The model analysis process started with data split into training and testing datasets with an 8:2 ratio using sklearn.model_selection.train_test_split. The model used was sklearn.tree.DecisionTreeClassifier and was trained using the training data. And the outcome was predicted for the test data and then compared with the expected result. This process was repeated multiple times once for each dataset of varying positive and negative data ratios. The results of those different datasets are given below.

Dataset Data Ratio | Accuracy | F1 Score
------------ | ------------- | -------------
1:1 | 88.1% | 0.89
1:2 | 92.04% | 0.88
1:4 | 94.07% | 0.86
1:8 | 95.22% | 0.78
1:16 | 97.75% | 0.79
1:32 | 98.75% | 0.81
1:300 | 99.89% | 0.79

An accuracy of over 99% was achieved with the 1:300 ratio dataset, but it had a lower F1 score and more false positives. The 1:1 ratio dataset had the lowest accuracy of 88%, but the fewest false positives and highest F1 score. As the count of negative data increased, accuracy increased, but the number of false positives also increased and F1 score decreased. On average, the dataset with the best combination of accuracy and F1 score is selected as the 1:4 ratio dataset. The confusion matrix is shown below.

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
    <td>84.29</td>
    <td>0.83</td>
  </tr>
  <tr>
    <td>KNN</td>
    <td>96.00</td>
    <td>0.48</td>
  </tr>
  <tr>
    <td>SVM</td>
    <td>71.86</td>
    <td>0.96</td>
  </tr>
  <tr>
    <td>Decision tree</td>
    <td>94.07</td>
    <td>0.86</td>
  </tr>
 </table>

## Conclusion
From the above experiments, we found out that the given dataset does not need a complicated model.
Our data does not have high dimensions because we only have seven useful attributes.
We add different negative data to test how the model can handle an unbalance situation when there are more negative data than positive data.
Overall, the decision tree is the best model because it identifies the occurrence of wildfire with an accuracy of 94.07% and an F1 score of 0.86. 
Even in extremely unbalanced situations (the ratio of positive to negative data is 1:300), the decision tree model still performs well with a high F1 score of 0.79.

## Future Recommendations
There are scopes for improving the performance of the classification model with the help of - 
1. Availability of more wildfire data - This can promote the use of a complex deep learning model to achieve exemplary
performance
2. Addition of input weather features, so to achieve a more separable cluster. 
