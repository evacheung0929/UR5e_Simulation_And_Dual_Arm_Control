#! usr/bin/env python

''' 
    THIS IS FOR PICK AND PLACE ROBOT

    This script test out
    1. Dispensing pad retouch
    2. Load and run sequential program 

    by using dashboard server to call and play pre-writtened program on the UR5 pendant

    It is intend to be integrated with GUI

    Note, if the position between different programs are too too far away, it may fail to execute 'play' 

 '''

from dashboard_dual_service import Dashboard_Client
from ur_dashboard_msgs.srv import Load, LoadRequest, RawRequest,RawRequestRequest,Popup, PopupRequest, IsInRemoteControl,IsInRemoteControlRequest, GetRobotMode, GetRobotModeRequest, IsProgramRunning, IsProgramRunningRequest
from std_srvs.srv import Trigger, TriggerRequest
import time



# To be completed
# class Pick_and_Place_Program:
#     ''' To be completed '''
#     def __init__(self):
#         pass

#     def start(self):
#         total_sub_prog = ['reach_PCB', 'move_to_break_off', 'hold_PCB']
#         Program_Communication.check_prog_fail(total_sub_prog)
#         pass

#     def mid(self):
#         # check the status of the previous program, whether that is running or not

#         # How many programs we have
#         total_sub_prog = ['reach_PCB', 'move_to_break_off', 'hold_PCB']
#         Program_Communication.check_prog_fail(total_sub_prog)

#     def end(self):
#         # check the status of the previous program, whether that is running or not        
#         # How many programs we have
#         total_sub_prog = ['reach_PCB', 'move_to_break_off', 'hold_PCB']
#         Program_Communication.check_prog_fail(total_sub_prog)

#         pass