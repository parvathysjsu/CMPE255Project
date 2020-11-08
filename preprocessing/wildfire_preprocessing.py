import os
import pandas as pd


def load_data(path):
    fire_data = pd.read_csv(path)
    return fire_data


def remove_unnecessary_cols(fire_data, col_arr):
    for col in col_arr:
        fire_data.drop(col, axis=1, inplace=True)


def convert_to_date(column):
    column = pd.to_datetime(column).dt.date
    return column


def main():
    fire_data = load_data(os.path.join(DATA_DIR, 'Washington_Large_Fires_1973-2019.csv'))
    remove_unnecessary_cols(fire_data, ['OBJECTID', 'SHAPEAREA',
                                        'SHAPELEN', 'FIRENUM',
                                        'PERIMDATE'])
    fire_data['STARTDATE'] = convert_to_date(fire_data['STARTDATE'])
    print(fire_data)


if __name__ == '__main__':
    DATA_DIR = os.path.join(os.path.dirname(__file__), '../data/')
    main()
