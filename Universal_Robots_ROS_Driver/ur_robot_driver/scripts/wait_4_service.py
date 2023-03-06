#!/usr/bin/env python
import rospy
from ur_dashboard_msgs.srv import Load, LoadRequest, Popup, PopupRequest, IsInRemoteControl,IsInRemoteControlRequest, GetRobotMode, GetRobotModeRequest
from std_srvs.srv import Trigger, TriggerRequest
import time
from Timer import Time_Out_Check
# from testService.srv import NoArguments
'''This program is used to connect to the Dsashboard services fro provided message type, either from the std_srvs.srv (Trigger) or from the ur_dashboard_msgs.srv (UR Dashboard)

For more details of which service was being used here: https://github.com/UniversalRobots/Universal_Robots_ROS_Driver/blob/master/ur_robot_driver/doc/ROS_INTERFACE.md

MSg_name exmaples: Load, Popup, IsInRemoteControl, Trigger

Perform timeout check from the Timer.py to identify whether the client is successfully connected to the serivce
- if the time out has reached and service is not connected, output the result. The std_srv.srvs returns 2 output (http://docs.ros.org/api/std_srvs/html/srv/Trigger.html)
this can be directly accessed through the request result
e.g. 

client = rospy.ServiceProxy('power on', Trigger)
request = TriggerRequest()
ressult = client(request)

print(result.answer)
print(result.success)

service_name is the pre-defined service name that is called upon the instantiation of the program
http://docs.ros.org/api/std_srvs/html/srv/Trigger.html 
https://github.com/UniversalRobots/Universal_Robots_ROS_Driver/blob/master/ur_robot_driver/doc/ROS_INTERFACE.md
https://github.com/UniversalRobots/Universal_Robots_ROS_Driver/tree/98e0d87234cdbd75736c0a30b817cd4ec34bc469/ur_dashboard_msgs 

'''
class Dashboard_Client:
    def __init__(self, service_str_name,  Msg_Name, Msg_Request):
        self.service_general_name = '/ur_hardware_interface/dashboard/'
        self.time_out_check = Time_Out_Check()
        self.Msg_Name = Msg_Name
        self.Msg_Request = Msg_Request
        self.service_str_name = service_str_name
        self.service_name = self.service_general_name+self.service_str_name
    def tout(self, result):
        return self.time_out_check.time_out(result, Msg_Request_Name=self.Msg_Request)
        
    def connect(self):
        rospy.wait_for_service(self.service_name)
        client =rospy.ServiceProxy(self.service_name, self.Msg_Name)
        # request = self.Msg_Request
        # # request = TriggerRequest()
        # result = client(request)  
        # # self.tout(result)
        # print(result)
        # self.time_out_check.time_out(result,self.Msg_Request)
        # return result

    def load(self, file_name):
        service_name = '/ur_hardware_interface/dashboard/load_program'
        # rospy.init_node('Dashboard_load_program')
        rospy.wait_for_service(service_name)
        client =rospy.ServiceProxy(service_name, Load)
        request = LoadRequest()
        request.filename = file_name+'.urp'
        print('loading program:',request.filename)
        result = client(request)
        # self.time_out_check.time_out(result, Msg_Request_Name=self.Msg_Request)
        self.tout(result)
        # print(result.success)
        return result
    
    def robot_mode(self):
        service_name  = self.service_general_name+'get_robot_mode'
        
        rospy.wait_for_service(service_name, timeout=3)
        # req = ur_dashboard_msgs.msg.RobotMode()
        # print(req.answer)
        # print(m)
        client = rospy.ServiceProxy(service_name,GetRobotMode)
        request = GetRobotModeRequest()
        result = client(request)
        # self.tout(result)
        print('==========')
        print(result)
        
        return result.answer
    
    def play(self):
        status = {#'Robotmode: ':'NO_CONTROLLER'
        # ,'Robotmode: ':'DISCONNECTED'
        # ,'Robotmode: ':'CONFIRM_SAFETY'
        # ,'Robotmode: ':'BOOTING',
        'OFF':'Robotmode: POWER_OFF',
        'ON':'Robotmode: POWER_ON',
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

        
        # print('uuuu')
        # else:
        # print('It is taking its damn time to connect to the robot, so waitttt')
        
            # raise SystemError('Check if the robot is powered on/ in remote control!')
            # self.time_out_check.time_out(result,self.Msg_Request)


            
# is_remote_check = Dashboard_Service('is_in_remote_control', IsInRemoteControl, IsInRemoteControlRequest())
# is_remote_check.load()

power_on =Dashboard_Client('power_on', Trigger, TriggerRequest())
power_on.connect()
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
