# Import pandas 
import pandas as pd
#Import duckdb databases system
import duckdb
# Import libraries to create environment variables
import requests

bm_path= './Data/bicimad1.db'
center= 'https://datos.madrid.es/egob/catalogo/200304-0-centros-culturales.json'

def acquisition(file_path1, table_name, file_path2):
    con = duckdb.connect(file_path1)
    df_acquisition1 = con.sql((f"SELECT * FROM {table_name}")).df()  #FOR BICIMAD
    
    c_cult_json_data = requests.get(file_path2).json()
    df_acquisition2 = pd.json_normalize(c_cult_json_data['@graph'])         #FOR CENTERS
    
    df_resultado = pd.concat([df_acquisition1, df_acquisition2], axis=1)
    return df_resultado

df_acquisition = acquisition('./Data/bicimad1.db', 'bicimad_stations', 'https://datos.madrid.es/egob/catalogo/200304-0-centros-culturales.json')