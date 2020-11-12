
# CMPE 255 Team 7 Project
# Scrappes and filters the temperature data for different stations in Washigton states for date range 2000-01-01 to 2020-10-31

import requests
import pandas as pd
import numpy as np

def fetch_data():
    station_list=["OLMthr 9","UILthr 9","SEAthr 9","450008 2","450257 2","450587 2","450574 2","450729 2","450872 2","451205 2","451233 2","451233 2","451246 2","451484 2","451679 2","451939 2","452157 2","452675 2","452914 2","453807 2","454084 2","454169 2","454748 2","454764 2","455110 2","455305 2","455525 2","455704 2","455774 2","455840 2","456114 2","456262 2","456295 2","456846 2","456858 2","456896 2","456898 2","456909 2","456914 2","457185 2","457473 2","457507 2","457773 2","457773 2","458009 2","458034 2","458278 2","458508 2","458715 2"]
    # station_list=["OLMthr 9"]
    
    # To Get the unique values in the list
    stations=set(station_list)

    request_body={
        "params":
            {
                "elems":[
                        {"name":"maxt"},
                        {"name":"mint"},
                        {"name":"avgt"},
                        {"name":"avgt","normal":"departure"},
                        {"name":"hdd"},
                        {"name":"cdd"},
                        {"name":"pcpn"},
                        {"name":"snow"},
                        {"name":"snwd"}
                        ],
                "sid":"SEAthr 9",# replace by station id from stations set
                "sDate":"2000-01-01",
                "eDate":"2020-10-31"
            },
        "output":"json"
    }

    data=[]
    total_rows=0
    total_deleted=0
    for station in stations:
        request_body["params"]["sid"]=station
        res=requests.post("https://data.rcc-acis.org/StnData",json=request_body)
        temp_data=res.json()
        name=""
        state=""
        uid=0
        if "meta" in temp_data:
            name=temp_data["meta"]["name"]
            uid=temp_data["meta"]["uid"]
            state=temp_data["meta"]["state"]

        
        if "data" in temp_data:
            
            for i in range(len(temp_data["data"])):
                total_rows+=1
                remove=False
                if temp_data["data"][i][1]==temp_data["data"][i][2]==temp_data["data"][i][3]==temp_data["data"][i][4]==temp_data["data"][i][5]==temp_data["data"][i][6]==temp_data["data"][i][7]==temp_data["data"][i][8]==temp_data["data"][i][9]=="M":
                    total_deleted+=1
                    remove=True
                    
                temp_data["data"][i].append(station)
                temp_data["data"][i].append(name)
                temp_data["data"][i].append(state)
                temp_data["data"][i].append(uid)
                temp_data["data"][i].append(remove)
            
            data.extend(temp_data["data"])
    
    print("total Rows")
    print(total_rows)
    print("total Deleted")
    print(total_deleted)
    return pd.DataFrame(np.array(data),columns=['date','max_temperature','min_temperature','avg_temperature','departure_temperature','hdd','cdd','percipitation','new_snow','snow_depth','station_id','name','state','uid','remove'])


def filter_data(df):
    df.drop(df.loc[df['remove']==True].index, inplace=True)
    df.drop(["remove"],axis=1,inplace=True)
    print(df.head(5))
    return df


def main():
    df=fetch_data()
    df=filter_data(df)
    df.to_csv("./data/weather_data.csv",index=False)

if __name__ == "__main__":
    main()
    pass