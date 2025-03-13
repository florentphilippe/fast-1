# Fast-1

A data science project about Formula 1, from racing statistics to overall season results. This app is like a "Static Data Generator" (SDG) to produce data oriented files ready for datavisualisation in a separate service. No API for smoother workflow, everything is static here !

## Data source

### Historic racing data 
Historic race results and data is originated from [jolpica / ergast API](https://github.com/jolpica/jolpica-f1). 

### Grands-prix tracks
The geojson files describing the grand-prix tracks are distributed (unofficial) on @bacinger repo : [f1-circuits](https://github.com/bacinger/f1-circuits).



## Output

An output folder is built (`/output`) where all the data is ready and optimised for dataviz.  
Thus this is where we can find the main databse, `fast1.db`, a SQLite DB for the main data structure. 
However, the data ready files are located in the `/outout/data` folder. 

### Data compression

Data compression is paramount here given the dataviz target. Thus we use `messagepack` framework to get compressed binary JSON files, useful for a later usage with `d3` / `js` fameworks. 

