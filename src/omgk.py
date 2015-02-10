'''
Created on Feb 2, 2015

@author: sharrin
'''
import urllib
import pprint
import requests
import json


#endpoint = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/locations/FIPS:37'
#endpoint = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&stationid=GHCND:USW00013722&datatypeid=HLY-TEMP-NORMAL&startdate=2015-01-06&enddate=2015-02-09'
endpoint = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/datatypes?datasetid=GHCND&stationid=GHCND:USW00013722&datacatergoryid=TEMP&limit=56'
#GHCND:USR0000NDUK
#lat/long is 35.9667, -79.0917
r = requests.get(endpoint, headers={'token': 'iQGlFoeXvPRnIgnzujBGSVIgLsjnDamb'})

#pprint.pprint(r.json())

results = r.json()
#json.loads(r)
pprint.pprint(results)
#print(json.dumps(results))