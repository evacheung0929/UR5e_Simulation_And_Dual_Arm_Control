#!/usr/bin/env python
'''As the ros service for the dashboard is already avaliable to be called, only a client is required to call the service

    "rosservice call /ur_hardware_interface/dashboard/power_on"

    --------------------------------
    "rosservice info /ur_hardware_interface/dashboard/power_on" returns:

    Node: /ur_hardware_interface
    URI: rosrpc://cheungy-VirtualBox:58643
    Type: std_srvs/Trigger
    Args: 

    from which we know that Trigger from std_srvs is used for power on, same process of confirmation was being done for the remaining commands
    --------------------------------

    Author: Eva Cheung
    Date: 24/02/2023


    code explaination
    
    # Trigger (This service uses exsiting .srv from package std_srvs/Trigger)
    def power_on(self):
        service_name = self.service_general_name+'power_on'
        # initialise a ROS node and wait for the service '/ur_hardware_interface/dashboard/power_on' to be running
        rospy.init_node('Dashboard_power_on')
        rospy.wait_for_service(service_name)
        
        # create a connection to the service
        client= rospy.ServiceProxy(service_name, Trigger)

        # create an object to the service, REQUEST the trigger
        request = TriggerRequest()

        # Result of that Trigger
        result = client(request)
'''

import rospy
from ur_dashboard_msgs.srv import RawRequestRequest, RawRequestResponse
from ur_dashboard_msgs.srv import Load, LoadRequest, Popup, PopupRequest, IsInRemoteControl,IsInRemoteControlRequest
from std_srvs.srv import Trigger, TriggerRequest
from std_srvs.srv import Empty
# dashboard_request = RawRequestRequest()
# a = dashboard_request.query()

class Dashboard_Client():
    def __init__(self):
        ''' comment out this init_node when using in script test_move, as only 1 ini_node is allowed for performance.
          e.g. subscriber can have a node, listener can have a node, but cannot be on the same node'''
        # rospy.init_node('Dashboard')
        self.service_general_name = '/ur_hardware_interface/dashboard/' 
    # def callback(self, msg):
    #     rospy.loginfo("The current robot mode is{}".format(msg))
    
    # ur_dashboard_msgs/IsInRemoteControl
    def is_in_remote(self):
        service_name = self.service_general_name+'is_in_remote_control'
        # rospy.init_node('remote_check')
        rospy.wait_for_service(service_name)
        client =rospy.ServiceProxy(service_name, IsInRemoteControl)
        request = IsInRemoteControlRequest()
        result = client(request)
    
    # Trigger
    def connect(self):
        service_name = self.service_general_name+'connect'
        # rospy.init_node('Dashboard_connection_check')
        rospy.wait_for_service(service_name)
        client =rospy.ServiceProxy(service_name, Trigger)
        request = TriggerRequest()
        result = client(request)

    # Trigger
    def power_on(self):
        service_name = self.service_general_name+'power_on'
        # initialise a ROS node and wait for the service '/ur_hardware_interface/dashboard/power_on' to be running
        # rospy.init_node('Dashboard_power_on')
        rospy.wait_for_service(service_name)
        
        # create a connection to the service
        client= rospy.ServiceProxy(service_name, Trigger)

        # create an object to the service, REQUEST the trigger
        request = TriggerRequest()

        # Result of that Trigger
        result = client(request)

    # Trigger
    def brake_release(self):
        service_name = self.service_general_name+'brake_release'
        # rospy.init_node('Dashboard_brake_release')
        rospy.wait_for_service(service_name)
        client =rospy.ServiceProxy(service_name, Trigger)
        request = TriggerRequest()
        result = client(request)

    # Trigger
    def play(self):
        service_name = self.service_general_name+'play'
        # rospy.init_node('Dashboard_play')
        rospy.wait_for_service(service_name)
        client =rospy.ServiceProxy(service_name, Trigger)
        request = TriggerRequest()
        result = client(request)
    
    # Trigger
    def pause(self):
        service_name = self.service_general_name+'pause'
        # rospy.init_node('Dashboard_pause')
        rospy.wait_for_service(service_name)
        client =rospy.ServiceProxy(service_name, Trigger)
        request = TriggerRequest()
        result = client(request)

    # ur_dashboard_msg/Load, load program file
    def load_program(self,filename):
        service_name = self.service_general_name+'load_program'
        # rospy.init_node('Dashboard_load_program')
        rospy.wait_for_service(service_name)
        client =rospy.ServiceProxy(service_name, Load)
        request = LoadRequest()
        request.filename = filename+'.urp'
        result = client(request)

    # ur_dashboard_msgs/Popup, show a message popup
    def pop_up(self, popup_msg):
        service_name = self.service_general_name+'popup'
        # rospy.init_node('Dashboard_popup')
        rospy.wait_for_service(service_name)
        client =rospy.ServiceProxy(service_name, Popup)
        request = PopupRequest()
        request.message = popup_msg
        result = client(request)

# uncomment the code below, after launching the ur5e robot bring up, test out if the this client is working expectedly
# make sure the initialise a node when testing without 'test_move'
# dashboard = Dashboard_Client()
# # Enter the program that you would like to upload
# # program variable: program name that is stored in the pendant
# program_name = {'external':'external', 'pcb_pick_and_place':'pcb', 'test':'testing'}
# dashboard.is_in_remote()
# dashboard.connect()
# dashboard.power_on()
# dashboard.brake_release()
# dashboard.load_program(program_name['test'])
# dashboard.play()