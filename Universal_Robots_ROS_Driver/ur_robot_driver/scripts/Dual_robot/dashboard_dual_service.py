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
from ur_dashboard_msgs.srv import Load, LoadRequest, RawRequestRequest, RawRequest,Popup, PopupRequest, IsInRemoteControl,IsInRemoteControlRequest, GetRobotMode, GetRobotModeRequest, IsProgramRunning, IsProgramRunningRequest
from std_srvs.srv import Trigger, TriggerRequest
import time
import timeit

class Time_Out_Check:
    def __init__(self):
        self.start_time = timeit.default_timer()
        self.duration = timeit.default_timer() - self.start_time
        self.time_out_limit = 10000

    def time_out(self, result, Msg_Request_Name):
        while (result.success == False) and (self.time_out_limit > self.duration):
            self.duration = timeit.default_timer()
            time.sleep(5)
            request = Msg_Request_Name

            # raise SystemError(result)
            print('Switch to Remote control and re-initiate the controller ')
            raise SystemError(result)

class Robot_Name:
    ''' Returns the generic service name corresponding to the provided robot name and action name,
        here action is defined as the name of the command that will be sent to the dashboard.
    
        Note, this is for dashboard service only!!! Other services will be coming up lately
    '''
    def __init__(self):
        # the name of the robot is obtained from the previously set up node name (inside package ur_robot_driver/launch/3_dual.launch)
        # this is the node name/ namespace that is corresponding to each robot
        # /pickAndPlace_robot/ur_hardware_interface/dashboard/

        self.service_general_name = '/ur_hardware_interface'
        self.pick_and_place_node = '/pickAndPlace_robot'
        self.dispense_node = '/dispense_robot'

        self.pp_dashboard = self.pick_and_place_node + self.service_general_name + '/dashboard' 
        self.disp_dashboard =  self.dispense_node + self.service_general_name +'/dashboard'
        self.dispense_robot_on = False
        self.pick_robot_on = False

    def dashboard_srv_name(self, robot_name, srv_name):
        '''The robot name is referring pickAndPlace robot node and dispense robot node
            The srv_name is the name of action in the service that we are trying to call, for example 'power_on' or 'set_IO'
            for the purpose of simplicity, the srv_name is used in dashboard_dual_service
        '''
        if robot_name.lower() == 'p':
            self.dispense_robot_on = False
            self.pick_robot_on = True
            service_name = self.pp_dashboard + srv_name
        elif robot_name.lower() == 'd':
            self.dispense_robot_on = True
            self.pick_robot_on = False
            service_name =  self.disp_dashboard + srv_name       
        elif robot_name == '':
                service_name = self.service_general_name+'/dashboard'+srv_name
        else:
            raise ValueError('The provided robot name does not exist, please enter either "p" or "d" to indcate which robot you are referring to')

        return service_name
    
    def hardware_int_srv(self, robot_name, srv_name):
        '''The robot name is referring pickAndPlace robot node and dispense robot node
            The srv_name is the name of action in the service that we are trying to call, for example 'power_on' or 'set_IO'
            for the purpose of simplicity, the srv_name is used in dashboard_dual_service
        '''
        if robot_name.lower() == 'p':
            self.dispense_robot_on = False
            self.pick_robot_on = True
            service_name = self.pick_and_place_node + self.service_general_name + srv_name
        elif robot_name.lower() == 'd':
            self.dispense_robot_on = True
            self.pick_robot_on = False
            service_name = self.dispense_node + self.service_general_name + srv_name        
        else:
            raise ValueError('The provided robot name does not exist, please enter either "p" or "d" to indcate which robot you are referring to')

        return service_name

class Dashboard_Client:
    def __init__(self, service_str_name,  Msg_Name, Msg_Request, robot_name):
        '''
        service_str_name = 'power on' 
        Msg_Name = the message type, e.g. Trigger, Load ...
        use the "self.robot" to determine which robot will be called
        '''
        self.robot = Robot_Name()
        self.service_str_name = '/' + service_str_name
        # print(self.service_str_name)
        # print(self.service_str_name)
        self.robot_name = robot_name
        self.service_name = self.robot.dashboard_srv_name(self.robot_name,self.service_str_name)
        self.time_out_check = Time_Out_Check()
        self.Msg_Name = Msg_Name
        self.Msg_Request = Msg_Request

        # indicate the service name corresponding to the robot name
        print(self.service_name)

    def tout(self, result):
        return self.time_out_check.time_out(result, Msg_Request_Name=self.Msg_Request)

    def connect(self):
        ''' Connecting to the service & check if the service is connected, using its message type
        e.g. client =rospy.ServiceProxy(self.service_name, Load)'''
        rospy.wait_for_service(self.service_name, timeout=5)
        self.client = rospy.ServiceProxy(self.service_name, self.Msg_Name)
        self.request = self.Msg_Request

    def connect_internal(self, srv_name, msg, req):
        ''' Connecting to the service & check if the service is connected, using its message type.
            It takes pre-determined msg and srv and service name

        e.g. robot mode and play'''

        rospy.wait_for_service(srv_name)
        client = rospy.ServiceProxy(srv_name, msg)
        # time.sleep(1)
        result = client(req)
        return result

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
        srv_action = '/get_robot_mode'
        serv_name = self.robot.dashboard_srv_name(self.robot_name, srv_action)
        mode_result = self.connect_internal(serv_name, GetRobotMode, GetRobotModeRequest())

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

        '''If the robot is off, then turn it on'''
        if robot_status_check == status['OFF']:
            # power on the robot & brake release
            power_on = self.robot.dashboard_srv_name(self.robot_name, '/power_on')
            self.connect_internal(power_on, Trigger, TriggerRequest()) 

            brake_release = self.robot.dashboard_srv_name(self.robot_name, '/brake_release')
            self.connect_internal(brake_release, Trigger, TriggerRequest()) 

        while robot_status_check != status['RUNNING']:
            robot_status_check = self.robot_mode()
            time.sleep(1)
            print('The current mode is in: {}'.format(robot_status_check))

        # Play the program now that the robot is running
        serv_name = self.robot.dashboard_srv_name(self.robot_name, '/play')
        r = self.connect_internal(serv_name, Trigger, TriggerRequest())
        return r

    def program_runing(self):
        '''Return True or False for whether the robot is currently running a program'''
        program_running_srv_name = '/program_running'
        serv_name = self.robot.dashboard_srv_name(self.robot_name, program_running_srv_name)
        result = self.connect_internal(serv_name, IsProgramRunning, IsProgramRunningRequest())
        return result.program_running
    
        # A different way of achieving the same thing
        # program_running_srv_name = '/raw_request'
        # serv_name = self.robot.dashboard_srv_name(self.robot_name, program_running_srv_name)
        # client = rospy.ServiceProxy(serv_name, RawRequest)
        # request = RawRequestRequest()
        # request.query = 'running'
        # result = client(request)
        # print(result.answer)

        # return result

'''Examples for testing the connection of the connection'''

# Simulation

# power_on = Dashboard_Client('power_on', Trigger, TriggerRequest(),'')
# power_on.robot_mode()
# power_on.play()
# power_on.program_runing()
# power_on.program_runing()
# power_on.call_service()


# Dispense
# d = Dashboard_Client('power_on', Trigger, TriggerRequest(),'d')
# d.call_service()
# d_load = 
# d_connect = Dashboard_Client('quit', Trigger, TriggerRequest(), 'd')
# call = d_connect.call_service()
# r = d_connect.return_result()
# print(r.success)


# d_connect = Dashboard_Client('connect', Trigger, TriggerRequest(), 'd')
# d_connect.call_service()

# is_remote_check = Dashboard_Client('is_in_remote_control', IsInRemoteControl, IsInRemoteControlRequest(), 'd')
# is_remote_check.call_service()



# brake_release =Dashboard_Client('brake_release', Trigger, TriggerRequest())
# brake_release.connect()

# simulation_connect = Dashboard_Client('connect', Trigger, TriggerRequest(), '')
# simulation_connect.call_service()

# program_name = {'external':'external_control', 'pcb_pick_and_place':'pcb', 'test':'testing'}
# load_program = Dashboard_Client('load_program', Load, LoadRequest(),'')
# load_program.load(file_name = 'new_tube_start')
# load_program.load(file_name = '1')

# play = Dashboard_Client('play', Trigger, TriggerRequest(),'')
# play.play()

# while play.program_runing():
#     print('pasting')
#     time.sleep(2)

# load_program.load(file_name = '1')
# play.play()



# time.sleep(5)       
# spause = Dashboard_Client('pause', Trigger, TriggerRequest())  

# # pause.connect()

# stop =Dashboard_Client('stop', Trigger, TriggerRequest(),'p')
# stop.call_service()
