#!/usr/bin/env python

# \author  Eva Cheung evacheung0929.2@gmail.com
# \date    2021-08-05

import sys
import math
from datetime import datetime
# ---------------------------------------------------------------------
from xml_testing import XML_FILES_2
from dashboard_dual_service import Dashboard_Client
from dual_IO import Digital_IO
from Io_State_Check import IO_Status

import rospy
from ur_dashboard_msgs.srv import Load, LoadRequest, Popup, PopupRequest, IsInRemoteControl,IsInRemoteControlRequest, GetRobotMode, GetRobotModeRequest
from std_srvs.srv import Trigger, TriggerRequest
import time


# Compatibility for python2 and python3
if sys.version_info[0] < 3:
    input = raw_input
# Exisitng programs on the teach pendant, key = reference, val = program name within the pendant
pp_program_names = {'external':'external_control', 'pcb_pick_and_place':'pcb', 'test':'external_test'}
dispense_program_name = {'empty_paste':'empty_dry_paste', 'start_pasting':'inital_test', 
                                      'test':'test', 'move_away':'move_away_test'}

class Dual_Move:
    def __init__(self):
        rospy.init_node("test_move")
        # io contorl for piack and place + dispense robot
        # turnon = pick_IO_control.digital_on(3)
        # can stream pin state via subscribing to the namespace/iostate
        # the call back msg can be used to identify msg.digital_out_state[?].state
        self.disp_IO_control = Digital_IO('d')
        self.pick_IO_control = Digital_IO('p')

        # dashboard communication
        self.dispense_load_program = Dashboard_Client('load_program', Load, LoadRequest(),'d')
        self.dispense_start_program = Dashboard_Client('play', Trigger, TriggerRequest(),'d')
        self.dispense_stop_program =Dashboard_Client('stop', Trigger, TriggerRequest(),'d')
        self.dispense_power_on_robot = Dashboard_Client('power_on', Trigger, TriggerRequest(),'d')
        self.dispense_brake_release =Dashboard_Client('brake_release', Trigger, TriggerRequest(),'d')
        self.dispense_pause_robot = Dashboard_Client('pause', Trigger, TriggerRequest(),'d')  

        self.pickAndPlace_load_program = Dashboard_Client('load_program', Load, LoadRequest(),'p')
        self.pickAndPlace_start_program = Dashboard_Client('play', Trigger, TriggerRequest(),'p')
        self.pickAndPlace_stop_program =Dashboard_Client('stop', Trigger, TriggerRequest(),'p')
        self.pickAndPlace_power_on_robot = Dashboard_Client('power_on', Trigger, TriggerRequest(),'p')
        self.pickAndPlace_brake_release =Dashboard_Client('brake_release', Trigger, TriggerRequest(),'p')
        self.pickAndPlace_pause_robot = Dashboard_Client('pause', Trigger, TriggerRequest(),'p')  

    def pp_load(self, program_n):
        self.pickAndPlace_load_program.load(file_name = pp_program_names[program_n])
    def pp_play(self):
        self.pickAndPlace_start_program.play()
        # to pause after the play command being sent, as the controllers may not be ready just yet?
        time.sleep(5)
    def d_load(self, program_n):
        self.dispense_load_program.load(file_name = dispense_program_name[program_n])
    def d_play(self):
        self.pickAndPlace_start_program.play()
        # to pause after the play command being sent, as the controllers may not be ready just yet?
        time.sleep(5)
    def run_first_pp_program(self):
        ''' Waiting for pick and place output signal to be true to start pasting
        If the io status of pin 3 on pick and place robot is true, meaning the robot had moved away 
        & ready to start pasting
        '''
        self.pp_load('test')
        # listening to pp robot pin 3
        IO_Status(3).listening_to_p_io()
    
    def run_pp_program(self, prog_name):
        ''' Waiting for pick and place output signal to be true to start pasting
        If the io status of pin 3 on pick and place robot is true, meaning the robot had moved away 
        & ready to start pasting
        '''
        self.pp_load(prog_name)
        # listening to pp robot pin 3
        IO_Status(3).listening_to_p_io()
        
    def run_d_program(self):
        self.d_load('test')
        self.d_play()
        # listening to pp robot pin 3
        IO_Status(0).listening_to_d_io()

# if __name__ == "__main__":
# dual_robot = Dual_Move()

p_power_on =Dashboard_Client('power_on', Trigger, TriggerRequest(),'p')
p_power_on.call_service()

p_brake_release =Dashboard_Client('brake_release', Trigger, TriggerRequest(),'p')
# p_brake_release.call_servi
# dual_robot.run_pp_program()

