import json
import requests
import os


file_counter = 0
offset_counter = 1
token = os.environ.get('token')

while file_counter <= 39:
    name = ("location_" + str(file_counter))
    url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit=1000&offset=' + str(offset_counter)
    header = {"Token": token, 'Content-Type': 'application/json'}
    r = requests.get(url=url, headers=header)
    data = r.json()

    with open('/Users/nli/dev/PythonFundamentals.Labs.DataAcqusitionLab/location_json/' + \
              (name + ".json"), 'w') as outfile:
        json.dump(data, outfile)
    file_counter += 1
    offset_counter += 1000

