# ---
# Serve static files made for dataviz
# ---

import pandas as pd
import sqlite3
import msgpack
import json
import os



output_path = "../../output/data/gp_lap/"
os.makedirs(output_path, exist_ok=True)


def type_maker(x):
    if len(x)>1:
        x = [int(y) for y in x]
    return x


#Open connexion
con = sqlite3.connect("../../output/fast1.db")
cur = con.cursor()


#Get years list
year_list = pd.read_sql("SELECT DISTINCT year FROM races",con)['year'].tolist()

#year_list = [2024]      #for testing

exemple = 0

for year in year_list:

    result = pd.read_sql(f"""SELECT races.year, races.name, races.raceId, races.date, constructors.name AS constructorName, drivers.forename, drivers.surname, results.positionText, results.points, results.time, lap_times.lap, lap_times.position
        FROM races
        LEFT JOIN results ON races.raceId = results.raceId
        LEFT JOIN drivers ON results.driverId = drivers.driverId
        LEFT JOIN constructors ON results.constructorId = constructors.constructorId
        LEFT JOIN lap_times ON results.raceId = lap_times.raceId AND results.driverId = lap_times.driverId 
        WHERE year = {year}
        ORDER BY races.date ASC, results.positionOrder ASC, lap_times.lap ASC""",con)
    

    result['position'] = result['position'].astype(int,errors='ignore')
    result['lap'] = result['lap'].astype(int,errors='ignore')

    

    
    result_h = result.groupby(['year','name','date','constructorName','forename','surname','positionText','points','time'],as_index=False).agg({
        'lap': list,
        'position': list
    })

    result_h['lap'] = result_h['lap'].apply(type_maker)
    result_h['position'] = result_h['position'].apply(type_maker)


    #Lap format reader
    """if year == 2024:
        exemple = result_h.loc[(result['forename'] == 'Max') & (result['name'] == 'Bahrain Grand Prix'),'lap']
    """


    result_h = result_h.drop(columns='year')    #Useless data, encoded in the filename


    #Message pack it for smaller output
    with open(output_path + f"{year}.msgpack",'wb') as file:
        packed_data = msgpack.packb(result_h.to_dict(orient='records'),use_bin_type=True)
        file.write(packed_data)



    #Exemples for other results 
    """ For JSON format instead of msgpack
    json_result = result_h.to_json(orient='records',indent=4)
    json_result = result_h.to_json(orient='records',lines=False)

    with open('./output.json','w') as file:
        file.write(json_result)
    """


    """ For even smaller outputs 
    with open('./output_6.msgpack','wb') as file:
        packed_data = msgpack.packb(result_h.to_dict(orient='tight',index=False),use_bin_type=True)
        file.write(packed_data)

        with open('./extract-json6.json','w') as file2:
            json_string = json.dump(msgpack.unpackb(packed_data),file2)
            file2.write(json_string)
    """




#Closing DB
con.close()


