#!/usr/bin/env python
'''This program is used to connect to the Dsashboard services fro provided message type, either from the std_srvs.srv (Trigger) or from the ur_dashboard_msgs.srv (UR Dashboard)

The dahsbaord commands are on the ROS service and can be activated through connecting to its corresponding service name
-  an example of service name for individual robot: '/ur_hardware_interface/dashboard'

When in dual-robot mode, each robot will be instantiated under different namespace
- an example of service name for multi-robots: '/<namespace>/ur_hardware_interface/dashboard'
- to test out if a rosservice is valid, use the command line >> rosservice call /<namespace>/ur_hardware_interface/dashboard/power_on
    - Need to ensure the robot is in remote control first

For more details of which service was being used here: https://github.com/UniversalRobots/Universal_Robots_ROS_Driver/blob/master/ur_robot_driver/doc/ROS_INTERFACE.md

MSg_name exmaples: Load, Popup, IsInRemoteControl, Trigger

Perform timeout check from the Timer.py to identify whether the client is successfully connected to the serivce
- if the time out has reached and service is not connected, output the result. The std_srv.srvs returns 2 output (http://docs.ros.org/api/std_srvs/html/srv/Trigger.html)
this can be directly accessed through the request result

client = rospy.ServiceProxy('power on', Trigger)
request = TriggerRequest()
result = client(request)

print(result.answer)
print(result.success)

service_name is the pre-defined service name that is called upon the instantiation of the program
http://docs.ros.org/api/std_srvs/html/srv/Trigger.html 
https://github.com/UniversalRobots/Universal_Robots_ROS_Driver/blob/master/ur_robot_driver/doc/ROS_INTERFACE.md
https://github.com/UniversalRobots/Universal_Robots_ROS_Driver/tree/98e0d87234cdbd75736c0a30b817cd4ec34bc469/ur_dashboard_msgs 

'''
# import all the relavent libraries and service messages that is relevant in obtaining the dahsboard result
import rospy
from ur_dashboard_msgs.srv import Load, LoadRequest, Popup, PopupRequest, IsInRemoteControl,IsInRemoteControlRequest, GetRobotMode, GetRobotModeRequest
from std_srvs.srv import Trigger, TriggerRequest
import time
from Timer import Time_Out_Check
from Robot_name import Robot

class Dashboard_Client:
    def __init__(self, service_str_name,  Msg_Name, Msg_Request, robot_name):
        '''
        service_str_name = 'power on' 
        Msg_Name = the message type, e.g. Trigger, Load ...
        use the "self.robot" to determine which robot will be called
        '''
        self.robot = Robot()
        self.service_name = self.robot.name(robot_name,service_str_name)
        self.time_out_check = Time_Out_Check()
        self.Msg_Name = Msg_Name
        self.Msg_Request = Msg_Request
        self.service_str_name = service_str_name

        # indicate the service name corresponding to the robot name
        print(self.service_name)
    def tout(self, result):
        return self.time_out_check.time_out(result, Msg_Request_Name=self.Msg_Request)

    def connect(self):
        ''' Connecting to the service & check if the service is connected, using its message type
        e.g. client =rospy.ServiceProxy(self.service_name, Load)'''
        rospy.wait_for_service(self.service_name)
        self.client = rospy.ServiceProxy(self.service_name, self.Msg_Name)
        self.request = self.Msg_Request

    def return_result(self):
        result  = self.client(self.request)  
        print(result)
        self.time_out_check.time_out(result, self.Msg_Request)
        return result

    def call_service(self):
        self.connect()
        self.return_result()
    def load(self, file_name):
        self.connect()
        self.request.filename = file_name+'.urp'
        print('loading program:',self.request.filename)
        self.return_result()

    # serv_robot_mode = 'get_robot_mode'
    # ur_dashboard_msgs.msg.RobotMode()
    def robot_mode(self):
        '''This function specifically return the robot mode of the selected robot, based on which robot is selected 
        1. robot name of 'pick' or p is selected, service name = /pickAndPlace_robot/ur_hardware_interface/dashboard/get_robot_mode
        2. robot name 'dispense' or d is selected, service name = /dispense_robot//ur_hardware_interface/dashboard/get_robot_mode

        As this fucntion is used solely to check if 'play' can be executed, the message name and type doesn't need to be called using class
        '''
        robot_serv_name = 'get_robot_mode'
        if self.robot.dispense_robot_on:
            print('dispense activated')
            srv_action = 'get_robot_mode'
            serv_name = self.robot.name('d', srv_action)
        elif self.robot.pick_robot_on:
            print('pick activated')
            serv_name = self.robot.name('p', srv_action)

        mode_client = rospy.ServiceProxy(robot_serv_name,GetRobotMode)
        request = GetRobotModeRequest()
        mode_result = mode_client(request)
        # self.tout(result)
        print('==========')
        print(mode_result)
        return mode_result.answer
    
    def play(self):
        '''Check if the robot mode is in the "Running" mode or not, if it is ready, then start playing'''
        status = {
        'OFF'    :'Robotmode: POWER_OFF',
        'ON'     :'Robotmode: POWER_ON',
        'RUNNING':'Robotmode: RUNNING'
        }
        robot_status_check = self.robot_mode()
        print('===========')
        # print(status['RUNNING'])
        while robot_status_check != status['RUNNING']:
            robot_status_check = self.robot_mode()
            time.sleep(1)
            print('The current mode is in: {}'.format(robot_status_check))
        rospy.loginfo('Starting program!')
        print('starting program!!')
        self.connect()
        self.return_result()


is_remote_check = Dashboard_Client('is_in_remote_control', IsInRemoteControl, IsInRemoteControlRequest(), 'd')
is_remote_check.call_service()

power_on =Dashboard_Client('power_on', Trigger, TriggerRequest(),'p')
power_on.call_service()
# brake_release =Dashboard_Client('brake_release', Trigger, TriggerRequest())
# brake_release.connect()


# program_name = {'external':'external_control', 'pcb_pick_and_place':'pcb', 'test':'testing'}
# load_program = Dashboard_Client('load_program', Load, LoadRequest())
# load_program.load(file_name = program_name['external'])

# play = Dashboard_Client('play', Trigger, TriggerRequest())
# play.play()
# # play.connect()


# time.sleep(5)       
# spause = Dashboard_Client('pause', Trigger, TriggerRequest())  

# # pause.connect()

# stop =Dashboard_Client('stop', Trigger, TriggerRequest())
# stop.connect()
