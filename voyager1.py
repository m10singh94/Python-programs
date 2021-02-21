#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 09:00:20 2020

@author: u7075106
"""

distance_at_start = 21906219000
velocity = 16.9995
speed_of_light = 299792.458
time = (2*distance_at_start)/speed_of_light
print(time)
def round_trip_communication_time(x):
    distance = distance_at_start + (velocity*x*24*3600)
    roundtrip_communication_time = (2*distance)/speed_of_light
    return roundtrip_communication_time

print(round_trip_communication_time(365))
print(round_trip_communication_time(3*365))
print(round_trip_communication_time(10*365))
print(round_trip_communication_time(100*365))
print(round_trip_communication_time(300*365))