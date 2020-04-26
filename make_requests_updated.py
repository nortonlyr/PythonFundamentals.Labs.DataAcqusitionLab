import json
import requests
import os
from dotenv import load_dotenv

def connect_url(url_base, offset_counter):
    url =url_base + str(offset_counter)
    return url

def create_file_name(file_counter):
    f = ('location_' + str(file_counter))
    return f

file_counter = 0
offset_counter = 1
token1 = os.environ.get('noaa_token1')
dotenv_local_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_local_path, verbose=True)

while file_counter <= 39:
    name = ('location_' + str(file_counter))
    url_base = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit=1000&offset=' + str(offset_counter)
    header = {"Token": token1, 'Content-Type': 'application/json'}
    r = requests.get(url=url_base, headers=header)
    data = r.json()
    file_path = './location_json/' + name + '.json'

    with open(file_path, 'w') as outfile:
        json.dump(data, outfile)
    file_counter += 1
    offset_counter += 1000