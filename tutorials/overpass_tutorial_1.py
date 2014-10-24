import geocoder
import requests

# Geocode Address from the OSM server
# Website: https://github.com/DenisCarriere/geocoder
g = geocoder.osm("Westboro, Ottawa ON")

# Define Bounding Box query for Overpass
bbox = '<bbox-query s="{south}" w="{west}" n="{north}" e="{east}"/>'.format(south=g.south, west=g.west, north=g.north, east=g.east)

# Define which keys & values you want to extract with your Overpass request
# Website: http://overpass-turbo.eu/
has_kv = """
<has-kv k="amenity" v="cafe"/>
<has-kv k="cuisine" v="coffee_shop"/>
"""

# Standard XML format for the Overpass query
data = """
<osm-script output="json" timeout="25">
  <union>
    <query type="node">
      {has_kv}
      {bbox}
    </query>
    <query type="way">
      {has_kv}
      {bbox}
    </query>
  </union>
  <print mode="body"/>
</osm-script>
""".format(has_kv=has_kv, bbox=bbox)

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

    # Geometry
    lat = element.get('lat')
    lng = element.get('lng')

    # Address
    name = tags.get('name')
    housenumber = tags.get('addr:housenumber')
    street = tags.get('addr:street')
    address = '%s %s' % (housenumber,street)

    # Print Pretty information:)
    if bool(housenumber and street):
        print '[%s] %s, %s' % (osm_id, name, address)
