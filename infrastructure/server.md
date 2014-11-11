## Overview

Wiki details the server infrastructure that the Ottawa Openstreetmap group has set up and is running.

## Servers

| Purpose | Server Type | OS | Domain Name | IP Address | Notes |
|---------|-------------|----|-------------|------------|-------|
| Task Manager | Amazon EC2 VPC. t2.medium with heavy utilization. | Ubuntu 14.04 LTS x64 | osmottawa.ca | 54.164.11.25 | Running HOT [Task Manager v2](https://github.com/hotosm/osm-tasking-manager2). 1 year term on ec2 instance. |

### Additional Notes

#### Connecting to Amazon an EC2 Instance

Setting up the Private Key

+ Download the osm_taskserver.pem and place it into a safe direction, if your using a Mac or Linux make a directory in your home root ~/.ec2/ or place it in ~/.ssh/
+ You must make the Private key not public by changing the permissions.

```
~$ chmod 400 ~/.ec2/osm_taskserver.pem
```

Finally connecting to Amazon EC2

+ Simply use your terminal and enter your private key, the username (ubuntu) which is the user on the server and the IP address of the server, if the server restarts this IP address might change.

```
~$ ssh -i ~/.ec2/osm_taskserver.pem ubuntu@54.164.11.25
```

## Task Manager Server

### Setting up the Ubuntu Instance

+ [HOT Tasking Manager V2](https://github.com/hotosm/osm-tasking-manager2)
+ [Setting up PostgreSQL + PostGIS on Ubuntu](https://help.ubuntu.com/community/PostgreSQL)

The command to install PostGIS, you will need to enter:
```
~$ sudo apt-get install postgis
# OR
~$ sudo apt-get install postgresql-9.3-postgis-2.1
```

Change password for PostgreSQL user:
```
~$ sudo -u postgres psql
postgres=# \password (username)
```

Install PostgreSQL Dev. This is a requirement for the Tasking Manager setup.py develop.
```
~$ sudo apt-get install postgresql-server-dev-9.3
```

To install Psycopg2, you must install [Python-Dev first](http://stackoverflow.com/questions/5420789/how-to-install-psycopg2-with-pip-on-python).

Ubuntu Apt-get installs or using the better apt install `aptitude`

```
sudo apt-get install git aptitude
sudo aptitude install python-pip
sudo pip install virtualenv
```

Now the hard part.. :(

Security Groups

+ After that if you are Administrator for the Amazon instance, you have to set up Security groups to unblock the incoming ports of 80 (HTTP for websites) & 5432 (PostgreSQL to connect via PgAdmin3).

Postgresql.conf & Pg_hba.conf

+ Never fun trying to figure those out, however if you have any connection problems it will be modifying those files to allow incoming connections. These files can be found at:

```
$ sudo nano /etc/postgresql/9.3/main/pg_hba.conf

local   all  postgres   md5

$ sudo nano postgresql.conf
listen_addresses = '*'

$ sudo service postgresql reload

or restart if editing the postgresql.conf

$ sudo service postgresql restart
* Restarting PostgreSQL 9.3 database server [OK]
```

## Serve HTTP

The OSM Canada server is using Nginx as HTTP server, this enables multiple applications running on a single server to be hosted. Having Nginx allows to have the hosting Tasking Manager (tasks.osmcanada.ca) on port 6432 and the port 80 pointing to the Wordpress blog.

## Running Tasking Manager in background

When you connect to the Ubuntu instance, you will want to launch the TM and close your Terminal window without closing the application, to do so you will need to add setid before deploying the app.

```
$ cd ~/osm-tasking-manager2/
$ sudo setsid ./env/bin/pserve --reload production.ini
```
