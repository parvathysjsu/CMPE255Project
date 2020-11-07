import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_shape_file():
    print("--- creating map from shape file ---")
    sns.set(style="whitegrid", palette="pastel", color_codes=True)
    sns.mpl.rc("figure", figsize=(10,6))
    #opening the vector map
    shp_path = "./../data/wa_lrg_fires.shp"
    #reading the shape file by using reader function of the shape lib
    sf = shp.Reader(shp_path)
    print("Shape: ", len(sf.shapes()))
    print("Sample record: ", sf.records()[0])
    df= read_shapefile(sf)
    print("Dataframe shape: ",df.shape)
    print("Sample Data: ")
    print(df.sample(5))
    plot_map(sf)
    # y_lim = (1000000,3000000) # latitude
    # x_lim = (1300000,1700000) # longitude
    # plot_map(sf, x_lim, y_lim)

def read_shapefile(sf):
    #fetching the headings from the shape file
    fields = [x[0] for x in sf.fields][1:]
    #fetching the records from the shape file
    records = [list(i) for i in sf.records()]
    shps = [s.points for s in sf.shapes()]
    #converting shapefile data into pandas dataframe
    df = pd.DataFrame(columns=fields, data=records)
    #assigning the coordinates
    df = df.assign(coords=shps)
    return df

def plot_map(sf, x_lim = None, y_lim = None, figsize = (11,9)):
    print("Creating map from shapefile data...")
    plt.figure(figsize = figsize)
    id=0
    for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        plt.plot(x, y, 'k')
        
        if (x_lim == None) & (y_lim == None):
            x0 = np.mean(x)
            y0 = np.mean(y)
            plt.text(x0, y0, id, fontsize=10)
        id = id+1
    
    if (x_lim != None) & (y_lim != None):     
        plt.xlim(x_lim)
        plt.ylim(y_lim) 
    plt.savefig('./../graphs/wildfire_data_map_from_shapefile.png')

def main():
    """ Data visualization
    """
    visualize_shape_file()
   

if __name__ == "__main__":
    main()