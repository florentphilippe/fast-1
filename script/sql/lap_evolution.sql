SELECT races.year, races.name, races.raceId, races.date, constructors.name AS constructorName, drivers.forename, drivers.surname, results.positionText, results.points, results.time, lap_times.lap, lap_times.position
FROM races
LEFT JOIN lap_times ON races.raceId = lap_times.raceId
LEFT JOIN drivers ON lap_times.driverId = drivers.driverId
LEFT JOIN results ON races.raceId = results.raceId AND drivers.driverId = results.driverId
LEFT JOIN constructors ON results.constructorId = constructors.constructorId
WHERE year = 1995
ORDER BY races.date ASC, results.position ASC, lap_times.lap ASC