# ----
# Data loader and connection to db 
# ----

import sqlite3
import pandas as pd



# DB connection
con = sqlite3.connect("../../data/sql/fast1.db")
cur = con.cursor()

#Read csv
races_df = pd.read_csv("../../data/csv/races.csv", sep=',', na_values=["\\N"], index_col="raceId")
circuits_df = pd.read_csv("../../data/csv/circuits.csv", sep=',', na_values=["\\N"], index_col=0)
constructor_results_df = pd.read_csv("../../data/csv/constructor_results.csv", sep=',', na_values=["\\N"], index_col=0)
constructor_standings_df = pd.read_csv("../../data/csv/constructor_standings.csv", sep=',', na_values=["\\N"], index_col=0)
constructors_df = pd.read_csv("../../data/csv/constructors.csv", sep=',', na_values=["\\N"], index_col=0)
driver_standings_df = pd.read_csv("../../data/csv/driver_standings.csv", sep=',', na_values=["\\N"], index_col=0)
drivers_df = pd.read_csv("../../data/csv/drivers.csv", sep=',', na_values=["\\N"], index_col=0)
lap_times_df = pd.read_csv("../../data/csv/lap_times.csv", sep=',', na_values=["\\N"])
pit_stops_df = pd.read_csv("../../data/csv/pit_stops.csv", sep=',', na_values=["\\N"], index_col=0)
qualifying_df = pd.read_csv("../../data/csv/qualifying.csv", sep=',', na_values=["\\N"], index_col=0)
results_df = pd.read_csv("../../data/csv/results.csv", sep=',', na_values=["\\N"], index_col=0)
seasons_df = pd.read_csv("../../data/csv/seasons.csv", sep=',', na_values=["\\N"], index_col=0)
sprint_results_df = pd.read_csv("../../data/csv/sprint_results.csv", sep=',', na_values=["\\N"], index_col=0)
status_df = pd.read_csv("../../data/csv/status.csv", sep=',', na_values=["\\N"], index_col=0)

lap_times_df.info()
print(lap_times_df.head())

lap_times_df.insert(0,"lap_times_id", lap_times_df.index.astype(str) + "-" + lap_times_df["driverId"].astype(str) + "-" + lap_times_df["lap"].astype(str))
lap_times_df.set_index("lap_times_id")





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
