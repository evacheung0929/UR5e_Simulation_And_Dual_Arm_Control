#!/usr/bin/env python
'''


OG





'''

import sys
import math
import time
import rospy
from ur_msgs.msg import IOStates
from ur_dashboard_msgs.srv import Load, LoadRequest, Popup, PopupRequest, IsInRemoteControl,IsInRemoteControlRequest, GetRobotMode, GetRobotModeRequest
from std_msgs.msg import Bool
from std_srvs.srv import Trigger, TriggerRequest
import rospy

from dashboard_dual_service import Dashboard_Client

from dual_IO import Digital_IO
# Exisitng programs on the teach pendant, key = reference, val = program name within the pendant
pp_program_names = {'external':'external_control', 'pcb_pick_and_place':'pcb', 'place_down':'external_test', 'move_pasted':'external_test_2'}
dispense_program_name = {'empty_paste':'empty_dry_paste', 'start_pasting':'inital_test', 
                                      'test':'test', 'move_away':'move_away_test'}
class IO_Status:
    def __init__(self,pin_num):
        # rospy.init_node('pickAndPlace_digital_out')
        self.num = pin_num
        self.rate = rospy.Rate(0.5) #0.5Hz
        rospy.init_node('please_eeeeeeeeeeeeeeeeeeeeeeeeee_work')
        
        self.d_io_state = '/dispense_robot/ur_hardware_interface/io_states'
        self.p_io_state = '/pickAndPlace_robot/ur_hardware_interface/io_states'

        self.pickAndPlace_load_program = Dashboard_Client('load_program', Load, LoadRequest(),'p')
        self.pickAndPlace_start_program = Dashboard_Client('play', Trigger, TriggerRequest(),'p')
        self.pickAndPlace_stop_program =Dashboard_Client('stop', Trigger, TriggerRequest(),'p')
        self.pickAndPlace_power_on_robot = Dashboard_Client('power_on', Trigger, TriggerRequest(),'p')
        self.pickAndPlace_brake_release =Dashboard_Client('brake_release', Trigger, TriggerRequest(),'p')
        self.pickAndPlace_pause_robot = Dashboard_Client('pause', Trigger, TriggerRequest(),'p')  

    def dispense_activation(self,msg):
        p_io_signal = msg.digital_out_states[3].state
        def run():
            if p_io_signal:
                print('start dispense')
                # start dispense program
            self.rate.sleep()
        run()

    def pickup_dispensed(self,msg):
        d_io_signal = msg.digital_out_states[0].state
        def run():
            if d_io_signal:
                print('Ready to pick up the pasted stuff + WAIT + PLACE ANOTHER')
                # load program x
                # start program x
            self.rate.sleep()
        run()

    def move_dispensee(self):
        rospy.Subscriber(self.p_io_state, IOStates ,self.dispense_activation, queue_size=1)
        rospy.spin()

    def move_pick_and_place(self):
        rospy.Subscriber(self.d_io_state, IOStates ,self.pickup_dispensed, queue_size=1)
        rospy.spin()

    def p_load(self, program_n):
        self.pickAndPlace_load_program.load(file_name = pp_program_names[program_n])
      
first_enc = True
# pin 3 on pick and place robot
p_io = IO_Status(3)
p_io.p_load('test')

while True:    
    p_io.p_load('place_down')
    print('place down for pasting then move away')

    if first_enc:
        p_io.p_load('move_pasted')
        print('wait for dispense to finished')
        print('pick up enc from pasting station')

        p_io.p_load('place_down')
        print('place down for pasting then move away')
        print('=======')
        first_enc = False
    p_io.p_load('external')
    print('PCB...Screw...')
    print('pick up enc from pasting station')
    print('-------')
    time.sleep(5)

# p_io_state.listening_to_p_io()


#!/usr/bin/env python

# # Exisitng programs on the teach pendant, key = reference, val = program name within the pendant
# # program_names = {'start_paste':'initial_paste', 'empty_dry_paste':'empty_paste'}

# class IO_Status:
#     def __init__(self,pin_num):
#         # rospy.init_node('pickAndPlace_digital_out')
#         self.dispense_data = False
#         self.pick_and_place_data = False
#         self.num = pin_num
#         self.count=0
#         self.d_count = 0
#         rospy.init_node('please')
#         self.dispense_program_name = {'empty_paste':'empty_dry_paste', 'start_pasting':'inital_test', 
#                                       'test':'test', 'move_away':'move_away_test'}
        
#         self.pp_program_names = {'external':'external_control', 'pcb_pick_and_place':'pcb', 'test':'external_test', 'test2':'external_test_2'}

#         self.disp_IO_control = Digital_IO('d')
#         self.pick_IO_control = Digital_IO('p')
#         self.d_io_state = '/dispense_robot/ur_hardware_interface/io_states'
#         self.p_io_state = '/pickAndPlace_robot/ur_hardware_interface/io_states'

# # -----------------------------------------------------------------------------------------------------------------------------------Dashboard commands ------------------------------------------------------------------------------------------------------------------------
#         # self.dispense_connect = Dashboard_Client('connect', Trigger, TriggerRequest(),'d')  
#         # self.dispense_connect.call_service()
#         # self.dispense_load_program = Dashboard_Client('load_program', Load, LoadRequest(),'d')
#         # # self.dispense_load_program.load(file_name = self.dispense_program_name['test'])

#         # self.dispense_start_program = Dashboard_Client('play', Trigger, TriggerRequest(),'d')
#         # self.dispense_stop_program =Dashboard_Client('stop', Trigger, TriggerRequest(),'d')
#         # self.dispense_power_on_robot = Dashboard_Client('power_on', Trigger, TriggerRequest(),'d')
#         # self.dispense_brake_release =Dashboard_Client('brake_release', Trigger, TriggerRequest(),'d')
#         # self.dispense_pause_robot = Dashboard_Client('pause', Trigger, TriggerRequest(),'d') 
#         # self.dispense_stop_robot = Dashboard_Client('stop', Trigger, TriggerRequest(),'d')  

#         # self.pickAndPlace_load_program = Dashboard_Client('load_program', Load, LoadRequest(),'p')
#         # self.pickAndPlace_start_program = Dashboard_Client('play', Trigger, TriggerRequest(),'p')
#         # self.pickAndPlace_stop_program =Dashboard_Client('stop', Trigger, TriggerRequest(),'p')
#         # self.pickAndPlace_power_on_robot = Dashboard_Client('power_on', Trigger, TriggerRequest(),'p')
#         # self.pickAndPlace_brake_release =Dashboard_Client('brake_release', Trigger, TriggerRequest(),'p')
#         # self.pickAndPlace_pause_robot = Dashboard_Client('pause', Trigger, TriggerRequest(),'p')  

#         # d_connect = Dashboard_Client('quit', Trigger, TriggerRequest(), 'd')
#         # call = d_connect.call_service()
 

#     def d_call_back(self,msg):
#         '''call back method illustratee whether or not the dispensor roobot output is on or off
#           return true/false (state) for the slected pin '''   
#         self.dispense_data = msg.digital_out_states[self.num].state
#     def p_call_back(self,msg):
#         '''call back method illustratee whether or not the dispensor roobot output is on or off
#           return true/false (state) for the slected pin '''   
#         self.pick_and_place_data = msg.digital_out_states[self.num].state
#         rospy.loginfo(self.pick_and_place_data)
#         print(self.pick_and_place_data)
#     def run_pp(self, name):
#         '''if dispense finished, run pp
#         If the data is true, play program x, else just sleep and stop the program
#         '''
#         rate = rospy.Rate(1)
#         if self.dispense_data:
#             '''when the Dout[0] on dispense == True, meaning dispense has commpleted
#                pick up the dispensed enclosure
#             '''
#             self.d_load(name)
#             self.pickAndPlace_start_program.call_service()
#         rate.sleep()
#         self.pickAndPlace_stop_program.call_service()
# #################################################
#     def run_pp_pcb(self, name):
#         '''if dispense finished, run pp
#         If the data is true, play program x, else just sleep and stop the program
#         '''
#         rate = rospy.Rate(1)
#         if self.dispense_data:
#             '''when the Dout[0] on dispense == True, meaning dispense has commpleted
#                pick up the dispensed enclosure
#             '''
#             self.d_load(name)
#             self.pickAndPlace_start_program.call_service()
#         rate.sleep()
#         self.pickAndPlace_stop_program.call_service()
# ####################
#     # def run_dispense(self):
#     #     '''if pick and place is finished, start dispensing
#     #     If the data is true, play program x, else just sleep and stop the program
#     #     '''
#     #     count = 0
#     #     rate = rospy.Rate(1)
#     #     if self.pick_and_place_data:
#     #         '''when the Dout[0] on dispense == True, meaning dispense has commpleted
#     #            pick up the dispensed enclosure
#     #         '''
#     #         # self.d_load(name)
#     #         # self.pickAndPlace_start_program.call_service()
#     #         print('loaad and play dispensing program')
#     #         count =1
#     #     elif self.pick_and_place_data!=True and count==0:
#     #         print('stop dispensing program')
#     #         # self.pickAndPlace_stop_program.call_service()     
#     #     print('The Dout[3] on pp robot is off')
#     #     rate.sleep()                                                                                                                                                                                                                                                                                                      # self.d_publishing(data)
#     '''------------------------------------Subscriber------------------------------------'''
#     # def listening_to_p_io(self):
#     #     rospy.Subscriber(self.p_io_state, IOStates ,self.p_call_back, queue_size=1)
#     #     ######## Get the name in here!!
#     #     self.run_pp('test')

#     # def listening_to_d_io(self):
#     #     rospy.Subscriber(self.d_io_state, IOStates ,self.d_call_back, queue_size=1)
#     #     self.run_dispense('CHANGEEEEEEE THISSSSSSSS')

#     def dispense_activation(self):
#         rospy.Subscriber(self.p_io_state, IOStates ,self.p_call_back, queue_size=1)
#         # self.run_dispense(name=n)
#         # self.run_dispense()
#     # '''------------------------------------Publisher------------------------------------'''
#     # def p_publishing(self, info):
#     #     '''convert the io_state data of a selected pin from self.p_io_state to bool, then publish it as io topic
#     #         /pickAndPlace_io_results for future use
#     #     '''
#     #     pub = rospy.Publisher('/pickAndPlace_IO_results', Bool, queue_size=1)
#     #     pub.publish(info)

#     # def d_publishing(self, info):
#     #     '''convert the io_state data of a selected pin from self.p_io_state to bool, then publish it as io topic
#     #         /pickAndPlace_io_results for future use
#     #     '''
#     #     pub = rospy.Publisher('/dispense_IO_results', Bool, queue_size=1)
#     #     pub.publish(info)


# # # monitoring pin number 3 in pickAndPlace

# pp_io = IO_Status(3)
# pp_io.dispense_activation()
