#Proyecto_m1

import pandas as pd
import duckdb
import requests
from geopy.distance import geodesic
import geopandas as gpd 
from shapely.geometry import Point
import argparse

#FUNCTIONS USED
def to_mercator(lat, long):
    c = gpd.GeoSeries([Point(lat, long)], crs=4326)
    c = c.to_crs(3857)
    return c

def distance_meters(lat_start, long_start, lat_finish, long_finish):
    start = to_mercator(lat_start, long_start)
    finish = to_mercator(lat_finish, long_finish)
    return start.distance(finish)

#BICIMAD
con = duckdb.connect('./Data/bicimad3.db') 
bicimad_df= con.sql("SELECT * FROM bicimad_stations").df()

bicimad_df_filter= bicimad_df[['name', 'address', 'geometry.coordinates']]

lat_lon= bicimad_df_filter["geometry.coordinates"].str.strip('[]').str.split(",", expand=True)
bicimad_df_filter = bicimad_df_filter.assign(latitud=lat_lon[1].astype(float), longitud=lat_lon[0].astype(float))


bicimad_df_final= bicimad_df_filter.rename(columns={'name':'nameBM','address':'addressBM', 'latitud':'latitudeBM', 'longitud':'longitudeBM'}).drop(['geometry.coordinates'], axis=1)

bicimad_df_final['pointBM'] = bicimad_df_final.apply(lambda x:(gpd.GeoSeries([Point(x['latitudeBM'], x['longitudeBM'])], crs=4326).to_crs(3857)), axis=1)

#CENTER
c_cult_json_data = requests.get('https://datos.madrid.es/egob/catalogo/200304-0-centros-culturales.json').json()

c_cult_json_data['@graph']
c_cult_pd2= pd.json_normalize(c_cult_json_data['@graph']) 
c_cult_pd2.loc[:, 'Center_type'] = c_cult_pd2['@type'].str.split('/', expand=True)[6]
c_cult_pd2.loc[:,'Center_type']= c_cult_pd2['Center_type'].replace({'CentrosCulturales':'Centros Culturales', 'AuditoriosSalasConcierto': 'Auditorios Salas Concierto', 'CentrosAtencionSocial': 'Centros Atencion Social', 'SalasExposiciones':'Salas Exposiciones'})
c_cult_pd2_final= c_cult_pd2[['Center_type','title','address.street-address', 'location.latitude', 'location.longitude']]
c_cult_pd2_final= c_cult_pd2_final.rename(columns={'Center_type':'Center_type','title':'Place_of_interest', 'address.street-address':'address_center', 'location.latitude':'latitude_center', 'location.longitude':'longitude_center'})
c_cult_pd2_final['pointCC'] = c_cult_pd2_final.apply(lambda x:(gpd.GeoSeries([Point(x['latitude_center'], x['longitude_center'])], crs=4326).to_crs(3857)), axis=1)

#COMBINADOS
dataset_combined= c_cult_pd2_final.merge(bicimad_df_final, how='cross')

dataset_combined['distance'] = dataset_combined.apply(lambda row: distance_meters(row['latitude_center'], row['longitude_center'], row['latitudeBM'], row['longitudeBM']), axis=1)

newdataset_combined = dataset_combined.sort_values(by=['distance'], axis=0, ascending=True)
newdataset_combined2 = newdataset_combined.loc[newdataset_combined.groupby('Place_of_interest')['distance'].idxmin()][['Place_of_interest','Center_type','address_center','nameBM','addressBM','distance',]].reset_index(drop=True)

print("Herminia, cada uno tiene un ritmo, lo has hecho genial")

parser = argparse.ArgumentParser(description='Specific places or all places')
parser.add_argument("--myplace", type=str, help= 'Two options: "places" or "myplace"')
parser.add_argument("--places", type=str, help= 'Two options: "places" or "myplace"')
args = parser.parse_args()

def eleccion(args):
    if args.places:
        csv_allplaces = newdataset_combined2.to_csv('table_allplaces.csv')
        print("Your complete table is generating")
    elif args.myplace:
        place_of_interest = args.myplace
        table_for_user = newdataset_combined2[newdataset_combined2['Place_of_interest'].str.contains(place_of_interest, case=False)]
        if not table_for_user.empty:
            table_for_user.to_csv('table_for_user.csv')
            print("Your specific table is generating")
        else:
            print("The place is not in the list")
    else:
        print("The message is not correct")
eleccion(args)