#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 08:27:30 2020

@author: guest-lttoih
"""

import robot

robot.init()

def move_2steps_right() :
    robot.drive_right()
    robot.drive_right()
    
def move_2steps_left() :
    robot.drive_left()
    robot.drive_left()
    
def open_down_and_close_up() :
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_closed()
    robot.lift_up()
    
def pickup_and_replace() :
    robot.lift_up()
    open_down_and_close_up()
    move_2steps_right()
    open_down_and_close_up()
    move_2steps_left()
    robot.lift_down()
    robot.gripper_to_open()
    robot.lift_up()
    robot.gripper_to_closed()
    move_2steps_right()
    robot.lift_down()
    
def swap_left_and_middle() :
    robot.drive_right()
    pickup_and_replace()
    
def swap_middle_and_right() :
    robot.lift_up()
    move_2steps_right()
    open_down_and_close_up()
    move_2steps_left()
    robot.lift_down()
    robot.gripper_to_open()
    robot.lift_up()
    robot.gripper_to_closed()
    move_2steps_right()
    robot.lift_down()
    
def swap_left_and_right() :
    robot.lift_up()
    move_2steps_left()
    move_2steps_left()
    open_down_and_close_up()
    move_2steps_right()
    move_2steps_right()
    robot.lift_down()
    robot.gripper_to_open()
    robot.lift_up()
    robot.gripper_to_closed()
    move_2steps_left()
    move_2steps_left()
    robot.lift_down()
    robot.gripper_to_open()
    
    
    
    
    
    
    
    
    
    
    