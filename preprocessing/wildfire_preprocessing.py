import os
import pandas as pd
import geopandas
import reverse_geocoder
pd.options.mode.chained_assignment = None


def load_data(path):
    """
    Load data from csv to a dataframe
    :param path: path of the csv file
    :return: dataframe
    """
    fire_data = pd.read_csv(path)
    return fire_data


def remove_unnecessary_cols(fire_data, col_arr):
    """
    remove unnecessary columns from the dataframe
    :param fire_data: given dataframe
    :param col_arr: array of columns to remove
    """
    for col in col_arr:
        fire_data.drop(col, axis=1, inplace=True)


def convert_to_date(column):
    """
    convert the string of date and time to date only
    :param column: date time column
    :return: column with date
    """
    column = pd.to_datetime(column).dt.date
    return column


def combine_redundant(column):
    """
    combine redundant values to one value and correct spellings
    :param column: column to operate - Cause column
    :return: return cleaned column
    """
    column.replace(['MISCELLANEOUS', 'UNDER INVESTIGATION', 'UNDETERMINED'],
                   ['UNKNOWN', 'UNKNOWN', 'UNKNOWN'], inplace=True)
    column.replace(['CHILDREN', 'SMOKER'],
                   ['HUMAN', 'HUMAN'], inplace=True)
    column.replace('BURNIN MATERIAL',
                   'BURNING MATERIAL', inplace=True)


def load_shapefile(path):
    """
    Load shapefile to generate dataframe
    :param path: path of the shapefile
    :return: dataframe
    """
    shapefile = geopandas.read_file(path)
    return shapefile


def convert_crs(file, epsg):
    """
    Convert coordinates to required format
    :param file: shape file to convert
    :param epsg: format to convert
    :return: convert shape file with desired coordinate format
    """
    if file.crs == 'epsg':
        return file
    else:
        file = file.to_crs(epsg=epsg)
        return file


def add_county(geometry):
    """
    from the geometry column in the shape file, extract the location
    :param geometry: geometry column
    :return: area and county
    """
    area = []
    county = []
    for shape in geometry:
        # find the centroid of the shape
        bounds = shape.centroid
        # coordinates of the shapefile
        coordinates = (bounds.y, bounds.x)
        # corresponding place given the coordinates
        place = reverse_geocoder.search(coordinates)
        # if county is empty, centroid in Canada
        # bring down the coordinates to Washington state
        if place[0]['admin2'] == '':
            coordinates = (bounds.y - 0.2, bounds.x)
            place = reverse_geocoder.search(coordinates)
        # append area and county
        area.append(place[0]['name'])
        county.append(place[0]['admin2'])
    return area, county


def merge_fire_shape(fire_data, shapefile):
    """
    Merge wildfire data with its corresponding shape file
    :param fire_data: cleaned wildfire data
    :param shapefile: shape file
    :return: wildfire dataset with area and county
    """
    for i in range(len(fire_data['FIRENAME'])):
        for j in range(len(shapefile['FIRENAME'])):
            name_flag = str(fire_data['FIRENAME'][i]).upper() == str(shapefile['FIRENAME'][j]).upper()
            if name_flag:
                fire_data['AREA'][i] = shapefile['AREA'][j]
                fire_data['COUNTY'][i] = shapefile['COUNTY'][j]
                break
        # if firename doesn't exist in shape file, get the location of the wildfire data
        # using the unitid. First occuring location of the given unitid corresponds to
        # location of the given wildfire data
        if fire_data['AREA'][i] == '':
            for j in range(len(shapefile['FIRENAME'])):
                if str(fire_data['UNITID'][i]).upper() == str(shapefile['UNITID'][j]).upper():
                    fire_data['AREA'][i] = shapefile['AREA'][j]
                    fire_data['COUNTY'][i] = shapefile['COUNTY'][j]
                    break
    return fire_data


def main():
    # load spreadsheet data
    fire_data = load_data(os.path.join(DATA_DIR, 'Washington_Large_Fires_1973-2019.csv'))
    # preprocess spreadsheet data
    remove_unnecessary_cols(fire_data, ['OBJECTID', 'SHAPEAREA',
                                        'SHAPELEN', 'FIRENUM',
                                        'PERIMDATE', 'YEAR'])
    fire_data['STARTDATE'] = convert_to_date(fire_data['STARTDATE'])
    combine_redundant(fire_data['CAUSE'])

    # load shapefile
    shapefile = load_shapefile(os.path.join(DATA_DIR, 'wa_lrg_fires.shp'))
    # preprocess shapefile
    shapefile = convert_crs(shapefile, 4326)
    shapefile['AREA'], shapefile['COUNTY'] = add_county(shapefile.geometry)
    remove_unnecessary_cols(shapefile, ['SHAPE_AREA',
                                        'SHAPE_LEN', 'FIRENUM',
                                        'PERIMDATE', 'YEAR'])
    # store shapefile
    shapefile.to_csv(os.path.join(DATA_DIR, 'preprocessed/shapefile.csv'), index=False)

    # merge shapefile and spreadsheet
    fire_data['AREA'] = ''
    fire_data['COUNTY'] = ''
    fire_data = merge_fire_shape(fire_data, shapefile)
    fire_data.to_csv(os.path.join(DATA_DIR, 'preprocessed/wildfire.csv'), index=False)


if __name__ == '__main__':
    DATA_DIR = os.path.join(os.path.dirname(__file__), '../data/')
    main()
