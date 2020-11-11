import os
import pandas as pd
import geopandas
import reverse_geocoder
pd.options.mode.chained_assignment = None


def load_data(path):
    fire_data = pd.read_csv(path)
    return fire_data


def remove_unnecessary_cols(fire_data, col_arr):
    for col in col_arr:
        fire_data.drop(col, axis=1, inplace=True)


def convert_to_date(column):
    column = pd.to_datetime(column).dt.date
    return column


def combine_redundant(column):
    column.replace(['MISCELLANEOUS', 'UNDER INVESTIGATION', 'UNDETERMINED'],
                   ['UNKNOWN', 'UNKNOWN', 'UNKNOWN'], inplace=True)
    column.replace(['CHILDREN', 'SMOKER'],
                   ['HUMAN', 'HUMAN'], inplace=True)
    column.replace('BURNIN MATERIAL',
                   'BURNING MATERIAL', inplace=True)


def load_shapefile(path):
    shapefile = geopandas.read_file(path)
    return shapefile


def convert_crs(file, epsg):
    if file.crs == 'epsg':
        return file
    else:
        file = file.to_crs(epsg=epsg)
        return file


def add_county(geometry):
    area = []
    county = []
    for shape in geometry:
        bounds = shape.centroid
        coordinates = (bounds.y, bounds.x)
        place = reverse_geocoder.search(coordinates)
        if place[0]['admin2'] == '':
            coordinates = (bounds.y - 0.2, bounds.x)
            place = reverse_geocoder.search(coordinates)
        area.append(place[0]['name'])
        county.append(place[0]['admin2'])
    return area, county


def merge_fire_shape(fire_data, shapefile):
    for i in range(len(fire_data['FIRENAME'])):
        for j in range(len(shapefile['FIRENAME'])):
            name_flag = str(fire_data['FIRENAME'][i]).upper() == str(shapefile['FIRENAME'][j]).upper()
            if name_flag:
                fire_data['AREA'][i] = shapefile['AREA'][j]
                fire_data['COUNTY'][i] = shapefile['COUNTY'][j]
                break
        if fire_data['AREA'][i] == '':
            for j in range(len(shapefile['FIRENAME'])):
                if str(fire_data['UNITID'][i]).upper() == str(shapefile['UNITID'][j]).upper():
                    fire_data['AREA'][i] = shapefile['AREA'][j]
                    fire_data['COUNTY'][i] = shapefile['COUNTY'][j]
                    break
    return fire_data


def main():
    fire_data = load_data(os.path.join(DATA_DIR, 'Washington_Large_Fires_1973-2019.csv'))
    remove_unnecessary_cols(fire_data, ['OBJECTID', 'SHAPEAREA',
                                        'SHAPELEN', 'FIRENUM',
                                        'PERIMDATE', 'YEAR'])
    fire_data['STARTDATE'] = convert_to_date(fire_data['STARTDATE'])
    combine_redundant(fire_data['CAUSE'])

    shapefile = load_shapefile(os.path.join(DATA_DIR, 'wa_lrg_fires.shp'))
    shapefile = convert_crs(shapefile, 4326)
    shapefile['AREA'], shapefile['COUNTY'] = add_county(shapefile.geometry)
    remove_unnecessary_cols(shapefile, ['SHAPE_AREA',
                                        'SHAPE_LEN', 'FIRENUM',
                                        'PERIMDATE', 'YEAR', 'geometry'])
    shapefile.to_csv(os.path.join(DATA_DIR, 'preprocessed/shapefile.csv'), index=False)

    fire_data['AREA'] = ''
    fire_data['COUNTY'] = ''
    fire_data = merge_fire_shape(fire_data, shapefile)
    fire_data.to_csv(os.path.join(DATA_DIR, 'preprocessed/wildfire.csv'), index=False)


if __name__ == '__main__':
    DATA_DIR = os.path.join(os.path.dirname(__file__), '../data/')
    main()
