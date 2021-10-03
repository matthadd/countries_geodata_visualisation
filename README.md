Visualisation of countries geodata using fastapi server and jupyter client

+ server : contains the pydantic models (models.py), the fastapi endpoints (main.py), and the bash script to start the server (start.sh). Three APIs have been implemented:
    		- GET / : details the differents endpoints with associate methods.
		- POST /iso_code (with Offset Pagination) : takes as input one or multiple country names and returns the ISO3 country codes and return geographical data when 'details' parameter is true.
		- GET /all_geometries : retrieve all the contents of the countries.geojson file in one go.
    
    + client : contains a jupyter notebook which allows to make requests to the server (visualisation.ipynb). The display of the results is done by the matplotlib library.
    
    The details of the different versions for the server and the client are summarized in the requirements.txt of the respective folders.

Matthis Haddouche
