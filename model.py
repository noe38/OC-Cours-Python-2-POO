import json
import math

class Agent:

    #def say_hello(self, first_name):
    #    return "Bien le bonjour " + first_name + " !"

    def __init__(self, position, **agent_attributes):
        self.position = position
        for attr_name, attr_value in agent_attributes.items():
            setattr(self, attr_name, attr_value)

class Position:
    def __init__(self, latitude_degrees, longitude_degrees):
        self.latitude_degrees = latitude_degrees
        self.longitude_degrees = longitude_degrees

    @property
    def latitude(self):
        # latitude in radians
        return self.latitude_degrees * math.pi / 180

    @property
    def longitude(self):
        # longitude in radians
        return self.longitude_degrees * math.pi / 180

class Zone:

    ZONES = []
    MIN_LONGITUDE_DEGREES = -180
    MAX_LONGITUDE_DEGREES = 180
    MIN_LATITUDE_DEGREES = -90
    MAX_LATITUDE_DEGREES = 90
    WIDTH_DEGREES = 1
    HEIGHT_DEGREES = 1

    def __init__(self, corner1, corner2):
        self.corner1 = corner1
        self.corner2 = corner2
        self.inhabitants = 0

    def initialize_zones(self):
        for latitude in range(self.MIN_LATITUDE_DEGREES, self.MAX_LATITUDE_DEGREES, self.WIDTH_DEGREES)
            for longitude in range(self.MIN_LONGITUDE_DEGREES, self.MAX_LONGITUDE_DEGREES, self.WIDTH_DEGREES)
                bottom_left_corner = Position(longitude, latitude)
                top_right_corner = Position(longitude + self.WIDTH_DEGREES, latitude + self.HEIGHT_DEGREES)

def main():
    for agent_attributes in json.load(open("agents-100k.json")):
        latitude = agent_attributes.pop("latitude")
        longitude = agent_attributes.pop("longitude")
        position = Position(latitude, longitude)
        agent = Agent(position, **agent_attributes)
        print(Zone.MIN_LONGITUDE_DEGREES)
        

main()