#!/usr/bin/env python

import sys
import math
import rospy
from ur_msgs.msg import IOStates
from ur_dashboard_msgs.srv import Load, LoadRequest, Popup, PopupRequest, IsInRemoteControl,IsInRemoteControlRequest, GetRobotMode, GetRobotModeRequest
from std_msgs.msg import Bool
from std_srvs.srv import Trigger, TriggerRequest
import rospy

from dashboard_dual_service import Dashboard_Client
from dual_IO import Digital_IO
# Exisitng programs on the teach pendant, key = reference, val = program name within the pendant
# program_names = {'start_paste':'initial_paste', 'empty_dry_paste':'empty_paste'}

class IO_Status:
    def __init__(self,pin_num):
        # rospy.init_node('pickAndPlace_digital_out')
        self.num = pin_num
        self.count=0
        self.d_count = 0
        self.dispense_program_name = {'empty_paste':'empty_dry_paste', 'start_pasting':'inital_test', 
                                      'test':'test', 'move_away':'move_away_test'}
        
        self.pp_program_names = {'external':'external_control', 'pcb_pick_and_place':'pcb', 'test':'external_test', 'test2':'external_test_2'}

        self.disp_IO_control = Digital_IO('d')
        self.pick_IO_control = Digital_IO('p')
        self.d_io_state = '/dispense_robot/ur_hardware_interface/io_states'
        self.p_io_state = '/pickAndPlace_robot/ur_hardware_interface/io_states'

# -----------------------------------------------------------------------------------------------------------------------------------Dashboard commands ------------------------------------------------------------------------------------------------------------------------
        # self.dispense_connect = Dashboard_Client('connect', Trigger, TriggerRequest(),'d')  
        # self.dispense_connect.call_service()
        self.dispense_load_program = Dashboard_Client('load_program', Load, LoadRequest(),'d')
        # self.dispense_load_program.load(file_name = self.dispense_program_name['test'])

        self.dispense_start_program = Dashboard_Client('play', Trigger, TriggerRequest(),'d')
        self.dispense_stop_program =Dashboard_Client('stop', Trigger, TriggerRequest(),'d')
        self.dispense_power_on_robot = Dashboard_Client('power_on', Trigger, TriggerRequest(),'d')
        self.dispense_brake_release =Dashboard_Client('brake_release', Trigger, TriggerRequest(),'d')
        self.dispense_pause_robot = Dashboard_Client('pause', Trigger, TriggerRequest(),'d') 
        self.dispense_stop_robot = Dashboard_Client('stop', Trigger, TriggerRequest(),'d')  

        self.pickAndPlace_load_program = Dashboard_Client('load_program', Load, LoadRequest(),'p')
        self.pickAndPlace_start_program = Dashboard_Client('play', Trigger, TriggerRequest(),'p')
        self.pickAndPlace_stop_program =Dashboard_Client('stop', Trigger, TriggerRequest(),'p')
        self.pickAndPlace_power_on_robot = Dashboard_Client('power_on', Trigger, TriggerRequest(),'p')
        self.pickAndPlace_brake_release =Dashboard_Client('brake_release', Trigger, TriggerRequest(),'p')
        self.pickAndPlace_pause_robot = Dashboard_Client('pause', Trigger, TriggerRequest(),'p')  

        # d_connect = Dashboard_Client('quit', Trigger, TriggerRequest(), 'd')
        # call = d_connect.call_service()

    def pp_load(self, program_n):
        self.pickAndPlace_load_program.load(file_name = self.pp_program_names[program_n])
    
    def d_load(self, program_n):
        self.dispense_load_program.load(file_name = self.dispense_program_name[program_n])
 
    def p_call_back(self,msg):
        '''         START DISPENSING
        Return the IO status of the pick and place robot
        Indicate whether the pp had moved away
        Start dispense robot when the data of the provided pin number return true
        '''
        rate = rospy.Rate(1)
        # access the digital output state
        data = msg.digital_out_states[self.num].state
        # print(self.listening_to_d_io())
        if data == True and self.count ==0:
            print('Pick and place robot had moved away, start pasting now')
            '''The Pick and Place robot had moved away, now start pasting!
                The program is called only once when initiated.
                Turn off the digital output immediately to avoid future clash
            '''
            self.disp_IO_control.digital_on(7)
            self.d_load('test')
            self.dispense_start_program.call_service()
            # self.pick_IO_control.digital_off(self.num)
            self.count = 1
        elif data ==False:
            '''Pick and Place robot not ready yet'''
            print('Waiting on the Pick and Place robot')
            self.count = 0
            # self.dispense_stop_robot.call_service()
        rate.sleep()
        self.p_publishing(data)

    def d_call_back(self,msg):
        '''             Continue pick and place robot function !!
        Return the IO status of the dispense robot
        can indicate whether or not the pasting had finished
        '''
        rate = rospy.Rate(1)

        # wait 4 paste in the first round of assembly
        # pp_wait_4_paste = True
        # access the digital output state
        data = msg.digital_out_states[self.num].state
        # When the incoming pin state is true
        if data == True and self.d_count ==0:
            '''Call action'''
            print('The dispense had finished! Pick it up')
            # pick up
            self.pp_load('test2')
            self.pickAndPlace_start_program.call_service()
            # self.disp_IO_control.digital_off(self.num)
            # place another enclosure to dispensing area
            self.pp_load('test')
            self.d_count =1
            # self.dispense_pause_robot.call_service()
            # self.dispense_load_program.load(file_name = self.dispense_program_name['move_away'])
            # self.dispense_start_program.call_service()
            # rospy.is_shutdown(True)
            pp_wait_4_paste = False
        # elif data == True and self.d_count ==0 and pp_wait_4_paste == False:
        #     print('place a')
        elif data ==False:
            print('I am still pasting bro! You gotta be patient!!!')
            self.d_count = 0
        rate.sleep()
        self.d_publishing(data)
    '''------------------------------------Subscriber------------------------------------'''
    def listening_to_p_io(self):
        rospy.Subscriber(self.p_io_state, IOStates ,self.p_call_back, queue_size=1)
        rospy.spin()

    def listening_to_d_io(self):
        rospy.Subscriber(self.d_io_state, IOStates ,self.d_call_back, queue_size=1)
        rospy.spin()

    '''------------------------------------Publisher------------------------------------'''
    def p_publishing(self, info):
        '''convert the io_state data of a selected pin from self.p_io_state to bool, then publish it as io topic
            /pickAndPlace_io_results for future use
        '''
        pub = rospy.Publisher('/pickAndPlace_IO_results', Bool, queue_size=1)
        pub.publish(info)

    def d_publishing(self, info):
        '''convert the io_state data of a selected pin from self.p_io_state to bool, then publish it as io topic
            /pickAndPlace_io_results for future use
        '''
        pub = rospy.Publisher('/dispense_IO_results', Bool, queue_size=1)
        pub.publish(info)


# # monitoring pin number 3 in pickAndPlace
# p_io_state = IO_Status(3)
# p_io_state.listening_to_p_io()

# d_io_state = IO_Status(0)
# d_io_state.listening_to_d_io()
