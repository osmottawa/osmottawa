## Install

```bash
$ sudo apt-get install osm2pgsql
```

## Connect all users to PostgreSQL

```bash
$ cd /etc/postgresql/9.3/main
$ sudo nano pg_hba.conf
```
change the last row to open to the internet.

```bash
TYPE    DATABASE    USER    ADDRESS         METHOD
host    all         all     0.0.0.0/0       md5
```

Restart the server afterwards

```bash
$ sudo service postgresql restart
```

## Using osm2pgsql

### Create PostgreSQL DB

Using PgAdmin3 you will create a new Database `gisdb` with postgres as the user and create the PostGIS extension.

Documentation can be found on [LearnOSM](http://learnosm.org/en/osm-data/setting-up-postgresql/)

### Download Data

Using the [HOT Export](http://export.hotosm.org/) you can download a large area directly from the latest OSM server.
If you need a larger area try downloading the OSM.PBF from [GeoFabrik](http://download.geofabrik.de/), they upload new datasets every day.

```bash
wget -O iraq.osm.pbf http://export.hotosm.org/download/022356/rawdata.osm.pbf
```

```bash
$ osm2pgsql -c -d gisdb -U postgres -H localhost iraq.osm.pbf  -l -W -x -s
```
Opitional values ``-l`` imports data into latlng (WGS84), ``-W`` forces password prompt, use this on the Ubuntu Server.

Slim mode can be enable if you are receiving some errors `-s`

Extra Attributes to retrieve OSM User name & ID `-x` if you add the attributes in the default.style

### Changing Style

```bash
$ cd /usr/share/osm2pgsql
$ sudo nano default.style
```

Applying style to osm2pgsql import

```bash
$ osm2pgsql -c -d gisdb -U postgres -H localhost -S /usr/share/osm2pgsql/roads.style iraq-latest.osm.pbf
```

Optional parameters are ``-a`` Append Data, instead of ``-c`` which will overwrite the existing data. 

### Style File

A good Style file

```text
node        capital     text
node        population  text
node,way    name:en     text
node,way    name        text
node,way    admin_level text
way         highway     text    linear
way         railway     text
way         landuse     text    polygon
way         barrier     text
way         waterway    text
way         natural     text
way         power       text
way         place       text
way         wood        text
way         water       text
```
