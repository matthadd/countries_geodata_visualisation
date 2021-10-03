Visualisation of countries geodata using fastapi server and jupyter client

/all_geometries: GET : retrieve all the contents of the countries.geojson file in one go

/iso_code : POST :  takes as input one or multiple country names and returns the ISO3 country codes and return the associated geographical data when the optional parameter ‘details’ is True