# ----
# Data loader and connection to db 
# ----

import sqlite3
import pandas as pd



# DB connection
con = sqlite3.connect("../../output/fast1.db")
cur = con.cursor()

path = "../../data/csv/"
nav = ["\\N"]


#Read csv - one by one for specific loading parameters
races_df = pd.read_csv(path+"races.csv", sep=',', na_values=nav, index_col="raceId")
circuits_df = pd.read_csv(path+"circuits.csv", sep=',', na_values=nav, index_col=0)
constructor_results_df = pd.read_csv(path+"constructor_results.csv", sep=',', na_values=nav, index_col=0)
constructor_standings_df = pd.read_csv(path+"constructor_standings.csv", sep=',', na_values=nav, index_col=0)
constructors_df = pd.read_csv(path+"constructors.csv", sep=',', na_values=nav, index_col=0)
driver_standings_df = pd.read_csv(path+"driver_standings.csv", sep=',', na_values=nav, index_col=0)
drivers_df = pd.read_csv(path+"drivers.csv", sep=',', na_values=nav, index_col=0)

lap_times_df = pd.read_csv(path+"lap_times.csv", sep=',', na_values=nav)
pit_stops_df = pd.read_csv(path+"pit_stops.csv", sep=',', na_values=nav)

qualifying_df = pd.read_csv(path+"qualifying.csv", sep=',', na_values=nav, index_col=0)
results_df = pd.read_csv(path+"results.csv", sep=',', na_values=nav, index_col=0)
seasons_df = pd.read_csv(path+"seasons.csv", sep=',', na_values=nav, index_col=0)
sprint_results_df = pd.read_csv(path+"sprint_results.csv", sep=',', na_values=nav, index_col=0)
status_df = pd.read_csv(path+"status.csv", sep=',', na_values=nav, index_col=0)


# Create id and keys
lap_times_df.insert(0,"lap_times_id", lap_times_df["raceId"].astype(str) + "-" + lap_times_df["driverId"].astype(str) + "-" + lap_times_df["lap"].astype(str))
lap_times_df = lap_times_df.set_index("lap_times_id")

pit_stops_df.insert(0,"pit_stops_id", pit_stops_df["raceId"].astype(str) + "-" + pit_stops_df["driverId"].astype(str) + "-" + pit_stops_df["lap"].astype(str))
pit_stops_df = pit_stops_df.set_index("pit_stops_id")

lap_times_df.info()
print(lap_times_df.head())




#write sql
races_df.to_sql("races",con,if_exists="replace")
circuits_df.to_sql("circuits",con,if_exists="replace")
constructor_results_df.to_sql("constructor_results",con,if_exists="replace")
constructor_standings_df.to_sql("constructor_standings",con,if_exists="replace")
constructors_df.to_sql("constructors",con,if_exists="replace")
driver_standings_df.to_sql("driver_standings",con,if_exists="replace")
drivers_df.to_sql("drivers",con,if_exists="replace")
lap_times_df.to_sql("lap_times",con,if_exists="replace")
pit_stops_df.to_sql("pit_stops",con,if_exists="replace")
qualifying_df.to_sql("qualifying",con,if_exists="replace")
results_df.to_sql("results",con,if_exists="replace")
seasons_df.to_sql("seasons",con,if_exists="replace")
sprint_results_df.to_sql("sprint_results",con,if_exists="replace")
status_df.to_sql("status_results",con,if_exists="replace")



#Closing DB
con.close()
