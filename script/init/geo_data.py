# ----
# Add geo data to output bundle 
# ----


import sqlite3
import pandas as pd
import os
import glob
import json
from unidecode import unidecode
import shutil


#Connect to database
con = sqlite3.connect("../../output/fast1.db")
cur = con.cursor()


#Get the dataframe from sql
geo_df = pd.read_sql("SELECT * FROM circuits",con,index_col="circuitId")
geo_db_name = list(geo_df["name"])
geo_db_location = [unidecode(x)for x in list(geo_df["location"])]



#Get geo data
path_input = "../../data/geo/"

#store geo static files
path_output = "/static/geo/"
os.makedirs("../../output"+path_output, exist_ok=True)

geo_files_name = [f[-15:] for f in glob.glob(path_input+"*.geojson")]     #retrieve file names of geojson in the specific foler
#print("geo files found : ", len(geo_files_name))


for f in geo_files_name:

    with open(path_input+f,'r',encoding="utf-8") as geo_data_file:
        geo_data = json.load(geo_data_file)
        circuit_code = geo_data['features'][0]['properties']['Name']
        circuit_location = geo_data['features'][0]['properties']['Location']
        #print(circuit_code)

        if circuit_code in geo_db_name : 
            filename = str(geo_df.loc[geo_df['name'] == circuit_code, "circuitRef"].iloc[0])


            complete_db_path = path_output + filename + ".geojson"
            source_path = path_input + f

            shutil.copy2(source_path,"../../output" + complete_db_path)
            geo_df.loc[geo_df['name'] == circuit_code, "static_geo_path"] = complete_db_path
            
        
        elif circuit_location in geo_db_location:

            filename = str(geo_df.loc[geo_df['location'].apply(unidecode) == circuit_location, "circuitRef"].iloc[0])
            
            complete_db_path = path_output + filename + ".geojson"
            source_path = path_input + f

            shutil.copy2(source_path,"../../output" + complete_db_path)
            geo_df.loc[geo_df['location'] == circuit_location, "static_geo_path"] = complete_db_path
    
        else : 
            print("No circuit found for this geo data : ", circuit_code)
        

geo_df.to_sql("circuits",con,if_exists="replace")



#Closing DB
con.close()