#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 08:43:17 2020

@author: u7075106
"""
import robot

def make_tower():
    count = 0
    while robot.sense_color() != "":
        count = count + 1
        robot.drive_right()
        robot.drive_right()
    boxes = count
    
    while boxes > 0:
        robot.drive_left()
        robot.drive_left()
        boxes = boxes - 1
        
    robot.lift_up()
    robot.gripper_to_open()
    robot.drive_right()
    robot.lift_down()
    robot.gripper_to_closed()
    
    while boxes < (count - 1):
        boxes = boxes + 1
        robot.lift_up()
        robot.drive_right()
        robot.drive_right()
        robot.gripper_to_open()
        robot.lift_down()
        if boxes != count-1 :
            robot.gripper_to_closed()
        
def find(color):
    index = 0
    while (robot.sense_color() != color) and (robot.sense_color() != ""):
        index = index + 1
        print(index)
        if(robot.sense_color != ""):
            robot.lift_up()
    if robot.sense_color() == color:
        return index + 1
    else:
        return -1



    
        
        
    
        
        
        
        
        