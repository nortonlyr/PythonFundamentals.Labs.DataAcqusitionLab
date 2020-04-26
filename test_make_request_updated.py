import unittest
import requests
import urllib.parse
import json
import make_requests_updated
from unittest.mock import patch


class Test_make_requests_updated(unittest.TestCase):


    def test_connect_url(self):
        self.assertEqual(make_requests_updated.connect_url(
            'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit=1000&offset=', 4000),
                        'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit=1000&offset=4000')
        self.assertEqual(make_requests_updated.connect_url(
            'https://data.cityofnewyork.us/browse?q=school+data&page=',2),
                        'https://data.cityofnewyork.us/browse?q=school+data&page=2')


    def test_create_file_name(self):
        self.assertEqual(make_requests_updated.create_file_name(10), 'location_10')
        self.assertEqual(make_requests_updated.create_file_name(1000010), 'location_1000010')


if __name__ == '__main__':
    unittest.main()
