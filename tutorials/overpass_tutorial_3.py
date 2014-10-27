import geocoder
import requests
import time

"""
Tutorial 3
==========
Search for Buildings inside BBOX
"""

# Geocode Address to retrieve Bounding Box
g = geocoder.osm('Orleans, Ottawa ON')
bbox = '{south},{west},{north},{east}'.format(south=g.south, west=g.west, north=g.north, east=g.east)

# Standard Overpass QL (Query Language)
data = """
[out:json][bbox:{bbox}];
(
    way
    ["addr:housenumber"]
    ["addr:city"="Ottawa"];
    <;
    node
    ["addr:housenumber"]
    ["addr:city"="Ottawa"];
);
out body;
""".format(bbox=bbox)

print data

# Using the Request module, connect to the Overpass REST API
# Refence website: http://docs.python-requests.org/en/latest/
r = requests.get('http://overpass-api.de/api/interpreter', params={'data': data})

# Retrieve and see your data into a JSON format
elements = r.json().get('elements')
print 'Elements:', len(elements)
print 'Content:',len(r.content)

time.sleep(3.0)

for element in elements:
    # OSM related tags
    osm_type = element.get('type')
    osm_id = element.get('id')
    tags = element.get('tags')
    
    print osm_type, osm_id