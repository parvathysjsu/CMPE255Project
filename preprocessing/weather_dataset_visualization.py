import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_dir="./data/"
graph_dir="./graphs/"

def load_data(filename):
    return pd.read_csv(data_dir+filename, encoding='utf-8')


def visualise_max_temp_over_the_years(df):
    data=df.groupby(df['date'].dt.year)['max_temperature'].agg([ 'max'])
    fig, ax = plt.subplots(figsize=(15,7))
    plt.plot(np.unique(data['max'].keys().astype(str)), data['max'].values )
    plt.title('Max temperature over the years')
    plt.xlabel('Year')
    plt.ylabel('Max Temperature (°F)')
    plt.savefig(graph_dir+'max_temp_over_the_years.png')

def visualise_mean_temp_over_the_years(df):
    data=df.groupby(df['date'].dt.year)['max_temperature'].agg([ 'mean'])
    fig, ax = plt.subplots(figsize=(15,7))
    plt.plot(np.unique(data['mean'].keys().astype(str)), data['mean'].values )
    plt.title('Mean temperature over the years')
    plt.xlabel('Year')
    plt.ylabel('Mean Temperature (°F)')
    plt.savefig(graph_dir+'avg_temp_over_the_years.png')



# Filters data before visualising it
def filterdata(df):
    # removes records where temperature is missing
    df.drop(df.loc[df['max_temperature']=='M'].index, inplace=True)
    
    
    # Converts to proper type so grouping on year becomes easy
    df['date']= pd.to_datetime(df['date'])

    # Converts to proper type so aggregate functions can be applied
    df['max_temperature']= pd.to_numeric(df['max_temperature'])
    return df


def main():
    df=load_data("weather_data.csv")
    df=filterdata(df)
    visualise_max_temp_over_the_years(df)
    visualise_mean_temp_over_the_years(df)

if __name__ == "__main__":
    main()
    pass