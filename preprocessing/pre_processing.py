
# Team       : 7

import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(15,10))
data_dir="./data/"
graph_dir="./graphs/"

def load_data(filename):
    return pd.read_csv(data_dir+filename)

def number_of_fire_over_years(data):
    fire_over_the_years=data["YEAR"].value_counts()
    year=[]
    fires=[]
    index=[]
    count=0

    for i in sorted (fire_over_the_years.keys()) :  
        count+=1
        index.append(count)
        year.append(i)
        fires.append(fire_over_the_years[i])
    
    plt.bar(index,fires, width = 0.5)
    plt.xticks(index,year,rotation='vertical')
    plt.xlabel('Year') 
    plt.ylabel('No. of Fires') 
    plt.title('No. of Fires over the years') 
    
    plt.savefig(graph_dir+"No_Of_Fires_over_the years.png", format="png")    
   

def main():
    data=load_data("Washington_Large_Fires_1973-2019.csv")
    # drought_data=load_data("dm_export_19730101_20201102.csv")
    number_of_fire_over_years(data)

if __name__ == "__main__":
    main()
    