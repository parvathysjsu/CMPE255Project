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
    
    
### Merge wildfire and temperature data
[weather_dataset_visualization.py](./preprocessing/weather_dataset_visualization.py) runs the analysis on temperature dataset and saves the relevant graph in the [graphs](./graphs) directory.
```
# on mac run the following command from the git repo's root directory 
python ./preprocessing/weather_dataset_visualization.py
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
