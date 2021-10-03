from fastapi import FastAPI
import json
from models import *

app = FastAPI()


def fill_countries_datamodel():
    # read and convert json data from countries.geojson to data model Countries
    data = open("countries.geojson", "r").read()
    countries_geojson_data = json.loads(data)
    countries = Countries()

    # we fill each models to create a feature wich is append to the Countries model
    for i in range(len(countries_geojson_data['features'])):
        properties = Properties()
        properties.name = countries_geojson_data['features'][i]['properties']['name']
        geometry = Geometry()
        geometry.type = countries_geojson_data['features'][i]['geometry']['type']
        geometry.coordinates = countries_geojson_data['features'][i]['geometry']['coordinates']
        feature = Feature()
        feature.type = countries_geojson_data['features'][i]['type']
        feature.id = countries_geojson_data['features'][i]['id']
        feature.properties = properties
        feature.geometry = geometry
        countries.type = countries_geojson_data['type']
        countries.features.append(feature)
    return countries


@app.get("/")
async def root():
    return {'message': 'Welcome to countries geodata visualisation',
            'endpoints': ['/iso_code', '/all_geometries']}


@app.post("/iso_code")
# takes as input one or multiple country names and returns the ISO3 country codes
# and return the associated geographical data when the optional parameter ‘details’ is True
async def iso_code(iso_code_request: IsoCodeRequest):
    iso_code_response = IsoCodeResponse()
    # offset pagination
    iso_code_request.countries = iso_code_request.countries[iso_code_request.offset:iso_code_request.offset + iso_code_request.limit]
    countries = fill_countries_datamodel()

    name_to_code = {}
    name_to_geometry = {}
    for i in range(len(countries.features)):
        name_to_code[countries.features[i].properties.name] = countries.features[i].id
    # we check if the client want the geometry data to avoid unnecessary computations
    if iso_code_request.details:
        for i in range(len(countries.features)):
            name_to_geometry[countries.features[i].properties.name] = countries.features[i].geometry

    # again we check if the client want the geometry data to avoid unnecessary computations
    if iso_code_request.details:
        for country_name in iso_code_request.countries:
            countries_code_details = CountriesCodeDetails()
            countries_code_details.code = name_to_code[country_name]
            countries_code_details.geometry = name_to_geometry[country_name]
            iso_code_response.data.append(countries_code_details)
    else:
        for country_name in iso_code_request.countries:
            countries_code_details = CountriesCodeDetails()
            countries_code_details.code = name_to_code[country_name]
            iso_code_response.data.append(countries_code_details)

    return iso_code_response


@app.get("/all_geometries")
# retrieve all the contents of the countries.geojson file in one go
async def all_geometries():
    return fill_countries_datamodel()
