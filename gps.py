# gps.py
# Christopher Mulkey
# 10/15/2012
# Ch. 11 Final Exercise


import random

class Waypoint(object):                                 # Create a waypoint
    def __init__(self, latitue, longitude, name=''):    
        self.latitude = latitude
        self.longitude = longitude
        self.name = name

class Path(object):                                     # Creates Path
    def __init__(self, name=''):                        
        self.waypoints = []
        self.name = name
    def add_waypoint(self, waypoint):                   # Adds waypoints to list for path
        self.waypoints.append(waypoint)

def gpsGetLongLat():                                    # Generates random Long/Lat for waypoints
    longitude = (random.random()*180)-180
    latitude =  (random.random()*180)-90

gpsGetLongLat(print)
