from typing import List, Union
from pydantic import BaseModel

# all models used by main.py


# generate with datamodel-code-generator : countries.geojson data model
class Properties(BaseModel):
    name: str = None
class Geometry(BaseModel):
    type: str = None
    coordinates: List[List[List[Union[float, List[float]]]]] = None
class Feature(BaseModel):
    type: str = None
    id: str = None
    properties: Properties = None
    geometry: Geometry = None
class Countries(BaseModel):
    type: str = None
    features: List[Feature] = []


# IsoCodeRequest data model
class IsoCodeRequest(BaseModel):
    countries: List[str]
    details: bool = False
    limit: int = 5
    offset: int = 0


# IsoCodeResponse data model
class CountriesCodeDetails(BaseModel):
    code: str = None
    geometry: Geometry = None
class IsoCodeResponse(BaseModel):
    data: List[CountriesCodeDetails] = []
