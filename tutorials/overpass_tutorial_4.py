import geocoder
import requests
import time
import os
import osmapi

"""
Tutorial 4
==========
Search for Buildings inside BBOX and update with OSM API
Remove City & Country Tags
"""

# Connect to OSM api
username = os.environ.get('OSMAPI_USR')
password = os.environ.get('OSMAPI_PWD')
api = osmapi.OsmApi(username=username, password=password)
api.ChangesetCreate({u"comment": u"Removing addr:city", u'source':'Addxy', u'created_by':'Addxy'})
save_changeset = False

# Geocode Address to retrieve Bounding Box
g = geocoder.osm('Orleans, Ottawa ON')
bbox = '{south},{west},{north},{east}'.format(south=g.south, west=g.west, north=g.north, east=g.east)

# Standard Overpass QL (Query Language)
data = """
[out:json][bbox:{bbox}];
(
    way
    ["addr:housenumber"]
    ["addr:country"]
    ["addr:city"="Orleans"];
    <;
    node
    ["addr:housenumber"]
    ["addr:country"]
    ["addr:city"="Orleans"];
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

time.sleep(1.0)

for element in elements:
    # OSM related tags
    osm_type = element.get('type')
    osm_id = element.get('id')
    tags = element.get('tags')
    osm_modified = False

    # Retrieve OSM object
    if osm_type == 'way':
        obj = api.WayGet(osm_id)
    elif osm_type == 'node':
        obj = api.NodeGet(osm_id)
    print osm_id,'- Read'

    # Delete Extra fields
    tag = obj['tag']
    if tag.get('addr:city'):
        del obj['tag']['addr:city']
        print osm_id, '- Delete City'
        osm_modified = True

    if tag.get('addr:country'):
        del obj['tag']['addr:country']
        print osm_id, '- Delete Country'
        osm_modified = True

    # Update to OSM Database
    if osm_modified:
        print osm_id,'- Update OSM'
        if osm_type == 'way':
            obj = api.WayUpdate(obj)
            save_changeset = True
        elif osm_type == 'node':
            obj = api.NodeUpdate(obj)
            save_changeset = True

# Close Changeset
if save_changeset:
    api.ChangesetClose()
