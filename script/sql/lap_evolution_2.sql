SELECT races.year, races.name, races.raceId, races.date, constructors.name AS constructorName, drivers.forename, drivers.surname, results.positionText, results.points, results.time, lap_times.lap, lap_times.position
FROM races
LEFT JOIN results ON races.raceId = results.raceId
LEFT JOIN drivers ON results.driverId = drivers.driverId
LEFT JOIN constructors ON results.constructorId = constructors.constructorId
LEFT JOIN lap_times ON results.raceId = lap_times.raceId AND results.driverId = lap_times.driverId 
WHERE year = 1996
ORDER BY races.date ASC, results.positionOrder ASC, lap_times.lap ASC