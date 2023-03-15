#! /usr/bin/env python
''' 
This file aim to connect to the rosservice which connect to the UR IO 

    int8 FUN_SET_DIGITAL_OUT=1
    int8 FUN_SET_FLAG=2
    int8 FUN_SET_ANALOG_OUT=3
    int8 FUN_SET_TOOL_VOLTAGE=4
    int8 STATE_OFF=0
    int8 STATE_ON=1
    int8 STATE_TOOL_VOLTAGE_0V=0
    int8 STATE_TOOL_VOLTAGE_12V=12
    int8 STATE_TOOL_VOLTAGE_24V=24

    int8 fun
    int8 pin
    float32 state
    ---
    bool success
'''
import rospy
# ros set io is a service
from ur_msgs.srv import SetIO, SetIORequest
from std_msgs.msg import String
import time

from Robot_name import Robot
class Digital_IO:
    def __init__(self, robot_name):
        '''The service name can eitherbe 'p' or 'd', representing pick and palce robot and dispense robot service name'''
        robot = Robot()
        service_action_name = 'set_io'
        self.service_name = robot.name(robot_name, service_action_name)
        rospy.wait_for_service(self.service_name,  timeout=3)
        self.client = rospy.ServiceProxy(self.service_name, SetIO)
        self.request = SetIORequest()
        self.request.fun = 1
    def digital_on(self, pin_num):
        self.request.pin = pin_num
        self.request.state = 1
        result = self.client(self.request)
        return result
    def digital_off(self, pin_num):
        self.request.pin = pin_num
        self.request.state = 0
        result = self.client(self.request)
        return result

# io_control = Digital_IO()
# io_control.digital_on(2)
# time.sleep(2)
# io_control.digital_off(1)
#
# rospy.sleep(1)
# request(fun = 1, pin = 3, state = 24)
# rospy.sleep(1)
# request(fun = 1, pin = 3, state = 0)
# result = client(request)

# 

# ORRRR 
#  rostopic pub /ur_hardware_interface/script_command std_msgs/String "data: 'set_digital_out(2,True)'

# turn it off
# rosservice call /ur_hardware_interface/set_io "fun: 1
# pin: 2
# state: 0.0" 
# success: True

# turn it on
# rosservice call /ur_hardware_interface/set_io "fun: 1
# pin: 2
# state: 1.0" 
# 

# print(result.state)
