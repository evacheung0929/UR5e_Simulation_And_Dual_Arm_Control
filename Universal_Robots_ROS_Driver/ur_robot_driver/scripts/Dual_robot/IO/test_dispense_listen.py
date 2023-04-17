#! /usr/bin/env python

'''This is a subscriber to the Digital IOnode that publishes IO output of the pick and place robot

1. Find the node name via rostopic list
2. use rosmsg show <message type> to find out the detail of the publishing data from the IOStates
3. 
ur_msgs/Digital[] digital_in_states
  uint8 pin
  bool state
ur_msgs/Digital[] digital_out_states
  uint8 pin
  bool state
ur_msgs/Digital[] flag_states
  uint8 pin
  bool state
ur_msgs/Analog[] analog_in_states
  uint8 CURRENT=0
  uint8 VOLTAGE=1
  uint8 pin
  uint8 domain
  float32 state
ur_msgs/Analog[] analog_out_states
  uint8 CURRENT=0
  uint8 VOLTAGE=1
  uint8 pin
  uint8 domain
  float32 state
'''

import rospy
import time
from ur_msgs.srv import SetIO, SetIORequest
from ur_msgs.msg import IOStates

# rospy.wait_for_service()
rospy.init_node('pp_istener')
# 50Hz or 1/10 seconds
rate = rospy.Rate(50)
'''The subscriber nodes are found in the terminal
    >> rostopic list

    To visualise the topic:
    >> rostopic echo <publisher>
'''
# if the digital pin 3 of pp robot is activation
# load program x in the teach pendant 
# set the digital output to be ...
def call_back(msg):
    # this is pin 3
    data = msg.digital_out_states[3].state
    
follow_joint_trajectory_feedback= '/pickAndPlace_robot/pos_joint_traj_controller/follow_joint_trajectory/feedback'
io_state = '/pickAndPlace_robot/ur_hardware_interface/io_states'
io_state_msg = IOStates()
rospy.Subscriber(io_state, IOStates ,call_back, queue_size=1)
rospy.spin()

# time.sleep(10)
# io_state = '/pickAndPlace_robot/ur_hardware_interface/io_states'
# a = rospy.wait_for_message(io_state, IOStates).digital_out_states[3].state
# print(type(a))




# import rospy
# import time
# from ur_msgs.srv import SetIO, SetIORequest
# from ur_msgs.msg import IOStates

# # rospy.wait_for_service()
# rospy.init_node('pp_listener')
# # 50Hz or 1/10 seconds
# rate = rospy.Rate(50)
# '''The subscriber nodes are found in the terminal
#     >> rostopic list

#     To visualise the topic:
#     >> rostopic echo <publisher>
# '''

# def call_back(msg):
#     # this is pin 3
#     data = msg.digital_out_states[3].state
    
# def publish():
#     while not rospy.is_shutdown():
#         pub.publish(io_state_msg)
#         rate.sleep()

# pub = rospy.Publisher('/pickAndPlace_robot/pin_3_io', IOStates, queue_size=1)
# io_state_msg = IOStates()
# follow_joint_trajectory_feedback= '/pickAndPlace_robot/pos_joint_traj_controller/follow_joint_trajectory/feedback'
# io_state = '/pickAndPlace_robot/ur_hardware_interface/io_states'
# # rospy.Subscriber(io_state, IOStates ,call_back, queue_size=1)
# publish()
# rospy.spin()

