import datetime
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from joblib import dump
# import for metrics

from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score


data_dir="./data/preprocessed/"
graph_dir="./model_visualization/knn_classifier/"
model_save_dir="./trained_models/"

def remove_unnecessary_cols(fire_data, col_arr):
    """
    remove unnecessary columns from the dataframe
    :param fire_data: given dataframe
    :param col_arr: array of columns to remove
    """
    for col in col_arr:
        fire_data.drop(col, axis=1, inplace=True)

def load_data(filename):
    """
    Load data from csv file
    :param path: Path for the csv file
    :return: return the data in the file
    """
    return pd.read_csv(data_dir+filename, encoding='utf-8')

def preprocess_input(X):
    """
    Remove uncessary column and convert date to ordinal data
    :param X: input data to preprocess
    :return: processed data
    """
    remove_unnecessary_cols(X, ['end','departure_temperature'])
    # X.drop(columns=['end'], inplace=True)
    X['start'] = pd.to_datetime(X['start'])
    X['start'] = X['start'].map(datetime.datetime.toordinal)
    X = pd.get_dummies(X)
    return X

def make_confusion_matrix(cf, categories,
                          group_names=None,
                          count=True,
                          percent=True,
                          color_bar=True,
                          xy_ticks=True,
                          xy_plot_labels=True,
                          sum_stats=True,
                          fig_size=None,
                          c_map='Blues',
                          title=None):
    """
    Code to generate text within each box and beautify confusion matrix.
    :param cf: Confusion matrix
    :param categories: array of classes
    :param group_names: classes in the project
    :param count: whether to display the count of each class
    :param percent: whether to display percentage for each class
    :param color_bar: whether to display color bar for the heat map
    :param xy_ticks: whether to display xy labels
    :param xy_plot_labels: whether to display xy title
    :param sum_stats: whether to display overall accuracy
    :param fig_size: size of the plot
    :param c_map: color scheme to use
    :param title: Title of the plot
    :return: Confusion matrix
    """
    blanks = ['' for i in range(cf.size)]

    if group_names and len(group_names) == cf.size:
        group_labels = ["{}\n".format(value) for value in group_names]
    else:
        group_labels = blanks

    if count:
        group_counts = ["{0:0.0f}\n".format(value) for value in cf.flatten()]
    else:
        group_counts = blanks

    if percent:
        row_size = np.size(cf, 0)
        col_size = np.size(cf, 1)
        group_percentages = []
        for i in range(row_size):
            for j in range(col_size):
                group_percentages.append(cf[i][j] / cf[i].sum())
        group_percentages = ["{0:.2%}".format(value)
                             for value in group_percentages]
    else:
        group_percentages = blanks

    box_labels = [f"{v1}{v2}{v3}".strip()
                  for v1, v2, v3 in zip(group_labels,
                                        group_counts,
                                        group_percentages)]
    box_labels = np.asarray(box_labels).reshape(cf.shape[0], cf.shape[1])

    # CODE TO GENERATE SUMMARY STATISTICS & TEXT FOR SUMMARY STATS
    if sum_stats:
        # Accuracy is sum of diagonal divided by total observations
        accuracy = np.trace(cf) / float(np.sum(cf))
        stats_text = "\n\nAccuracy={0:0.2%}".format(accuracy)
    else:
        stats_text = ""

    # SET FIGURE PARAMETERS ACCORDING TO OTHER ARGUMENTS
    if fig_size is None:
        # Get default figure size if not set
        fig_size = plt.rcParams.get('figure.figsize')

    if not xy_ticks:
        # Do not show categories if xyticks is False
        categories = False

    # MAKE THE HEAT MAP VISUALIZATION
    plt.figure(figsize=fig_size)
    sns.heatmap(cf, annot=box_labels, fmt="",
                cmap=c_map, cbar=color_bar,
                xticklabels=categories,
                yticklabels=categories)

    if xy_plot_labels:
        plt.ylabel('True label')
        plt.xlabel('Predicted label' + stats_text)
    else:
        plt.xlabel(stats_text)

    if title:
        plt.title(title)

def make_correlation_matrix(dataset,data_set_name):
    # Identify features Columns
    feature_columns=["max_temperature","min_temperature","avg_temperature","departure_temperature","hdd","cdd","percipitation"]
    plt.clf()
    # Correlation matrix between numerical values
    sns.heatmap(dataset[feature_columns].corr(),annot=True, fmt = ".2f", cmap = "coolwarm")
    plt.savefig('{}{}/correlation_matrix.png'.format(graph_dir,data_set_name))


def save_model(clf,weight,model_name,):
    print(f"Saving model {model_name}")
    dump(clf, '{}{}/{}/trained_model.joblib'.format(graph_dir,model_name,weight))

def calculate_metrics(Y_test,predicted_y):
    print("Calculating metrics...")
    new_dict={}
    new_dict["classification_report"]=classification_report(Y_test,predicted_y)
    ROC_SOCRE=roc_auc_score(Y_test, predicted_y)
    new_dict["roc_auc_score"]=ROC_SOCRE
    F1_SCORE=f1_score(Y_test, predicted_y)
    new_dict["f1_score"]=F1_SCORE
    ACC_SCORE=accuracy_score(Y_test, predicted_y)
    new_dict["accuracy_score"]=ACC_SCORE
    print("roc_auc_score: ", ROC_SOCRE)
    print("f1 score: ", F1_SCORE)
    print("accuracy score: ", ACC_SCORE)
    return new_dict

def io_trend(variable, output, data, data_set_name):
    """
    Identify positive or negative relation with the output label
    :param variable: input variable
    :param output: label
    :param data: wildfire data set
    :return: plot graph showing the relation
    """
    plt.clf()
    plt.figure(figsize=(15,15))
    sns.regplot(x=variable, y=output, data=data)
    plt.savefig('{}{}/{}_relation.png'.format(graph_dir,data_set_name,variable))


def main(data_file_name):
    # data_file_name = 'negative_data_merge_weather_forest.csv'
    print('Loading data...')

    data = load_data(data_file_name)
    data_set_name = data_file_name.replace(".csv","")
    print (data_set_name)
    # Plot relation between input and output variables
    print('Plot relations...')
    io_trend('max_temperature', 'label', data, data_set_name)
    io_trend('percipitation', 'label', data, data_set_name)
    make_correlation_matrix(data,data_set_name)
    # input data

    # X = data.iloc[:, 4:-1]
    X = data.iloc[:, 8:-1]
    X = preprocess_input(X)
    # output data
    y = data.iloc[:, -1]
    
    # Split train and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # KNN  classifier
    print('Classify data...')

    h = .02  # step size in the mesh

    # Create color maps
    cmap_light = ListedColormap(['orange', 'cornflowerblue'])
    cmap_bold = ListedColormap(['darkorange', 'darkblue'])

    n_neighbors=5
    
    all_metrics=[]
    for weights in ["uniform","distance"]:
        clf = KNeighborsClassifier(n_neighbors=n_neighbors,weights=weights)
        clf.fit(X_train, y_train)
        
        # plot confusion matrix
        prediction = clf.predict(X_test)
        print(f'Plot confusion matrix for {weights} uniform...')
        corr = confusion_matrix(y_test, prediction)
        plt.savefig('{}{}/{}_weight/confusion_matrix.png'.format(graph_dir,data_set_name,weights), bbox_inches='tight')
        plt.figure()
        make_confusion_matrix(corr,
                            categories=['YES', 'NO'],
                            count=True,
                            percent=True,
                            color_bar=False,
                            xy_ticks=True,
                            xy_plot_labels=True,
                            sum_stats=True,
                            fig_size=(8, 6),
                            c_map='OrRd',
                            title='Wildfire Occurrence')
        # error correction - cropped heat map
        b, t = plt.ylim()  # discover the values for bottom and top
        b += 0.5  # Add 0.5 to the bottom
        t -= 0.5  # Subtract 0.5 from the top
        plt.ylim(b, t)  # update the ylim(bottom, top) values
        plt.savefig('{}{}/{}_weight/confusion_matrix.png'.format(graph_dir,data_set_name,weights), bbox_inches='tight')
        metrics = calculate_metrics(y_test,prediction)
        metrics["weight"]=weights
        all_metrics.append(metrics)
        save_model(clf,f"{weights}_weight",data_set_name)
    return all_metrics


if __name__ == '__main__':
    list_of_dataset=["1.csv",
                    "2.csv",
                    "4.csv",
                    "8.csv",
                    "16.csv",
                    "32.csv",
                    "300.csv",
                    "negative_data_merge_weather_forest.csv"]
    new_dict={}
    for data_set_name in list_of_dataset:
        temp=data_set_name
        new_dict[temp.replace(".csv","")]=main(data_set_name)

    print("=============================================================================================")
    print("All Metrics for different dataset and weight")
    print("=============================================================================================")
    for data_set_name in list_of_dataset:
        temp=data_set_name.replace(".csv","")
        print(f"Dataset : {temp}")
        print("=============================================================================================")
        all_metrics=new_dict[temp]
        for metrics in all_metrics:
            print("-------------------------------- Weight : {} -----------------------------".format(metrics["weight"]))
            print("    Weight : {}".format(metrics["weight"]))
            print("    Classfication Report :")
            print(metrics["classification_report"])
            print()
            print("ROC AUC SCORE : {}".format(metrics["roc_auc_score"]))
            print("F1 Score : {}".format(metrics["f1_score"]))
            print("Accuracy Score : {}".format(metrics["accuracy_score"]))
            print()
            print()
        print("=============================================================================================")
    
