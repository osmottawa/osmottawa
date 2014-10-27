import geocoder
import requests

"""
Tutorial 2
==========
Extract from Polygon using Python
"""

# Define Polygon query for Overpass
polygon = '(poly:"50.7 7.1 50.7 7.12 50.71 7.11");'

# Standard Overpass QL (Query Language)
data = """
[out:json];
(
    way
    ["addr:housenumber"]
    {polygon}
    <;
);
out meta;
""".format(polygon=polygon)

# Using the Request module, connect to the Overpass REST API
# Refence website: http://docs.python-requests.org/en/latest/
r = requests.get('http://overpass-api.de/api/interpreter', params={'data': data})

# Retrieve and see your data into a JSON format
elements = r.json().get('elements')
for element in elements:
    # OSM related tags
    osm_type = element.get('type')
    osm_id = element.get('id')
    tags = element.get('tags')
    print tags