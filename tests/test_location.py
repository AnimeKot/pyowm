#!/usr/bin/env python

"""
Test case for location.py module
"""

import unittest
from pyowm import Location


class Test(unittest.TestCase):
    
    __test_name = u'London'
    __test_lon = 12.3
    __test_lat = 43.7
    __test_ID = 1234

    def test_init_fails_when_coordinates_are_out_of_bounds(self):
        """
        Test failure when providing: lon < -180, lon > 180, lat < -90, lat > 90
        """
        self.assertRaises(ValueError, Location, u'London', -200.0, 43.7, 1234)
        self.assertRaises(ValueError, Location, u'London', 200.0, 43.7, 1234)
        self.assertRaises(ValueError, Location, u'London', 12.3, -100.0, 1234)
        self.assertRaises(ValueError, Location, u'London', 12.3, 100.0, 1234)
        
    def test_getters_return_expected_data(self):
        instance = Location(self.__test_name, self.__test_lon, self.__test_lat, self.__test_ID)
        self.assertEqual(instance.get_name(), self.__test_name, "")
        self.assertEqual(instance.get_lon(), self.__test_lon, "")
        self.assertEqual(instance.get_lat(), self.__test_lat, "")
        self.assertEqual(instance.get_ID(), self.__test_ID, "")

    def test_XML_dump(self):
        """
        Test correct object data dump to an XML string
        """
        expectedOutput = """<Location><name>%s</name><coordinates><lon>%s</lon><lat>%s</lat></coordinates><ID>%s</ID></Location>""" % (self.__test_name,
                                                                    self.__test_lon,
                                                                    self.__test_lat,
                                                                    self.__test_ID)
        instance = Location(self.__test_name, self.__test_lon, self.__test_lat, self.__test_ID)
        self.assertEqual(instance.to_XML(), expectedOutput, "")
        
    def test_JSON_dump(self):
        """
        Test correct object data dump to a JSON string
        """
        expectedOutput = """{"name": "%s", "coordinates": {"lat": %s, "lon": %s}, "ID": %s}""" %  (self.__test_name, 
           self.__test_lat, self.__test_lon, self.__test_ID)
        instance = Location(self.__test_name, self.__test_lon, self.__test_lat, self.__test_ID)
        self.assertEqual(instance.to_JSON(), expectedOutput, "")
        

if __name__ == "__main__":
    unittest.main()