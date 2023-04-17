#! /usr/bin/env python
from simplified_dual_move_p import Dual_Move
import rospy
'''run_first_pp_program = 
pp_load + 
pp.play +
listen to DOut[3] on pp

run_pp_program is listening to the digital output [3] in the pp robot 

'''
pick_and_place_robot = Dual_Move()
prog_name = 'change this!!'
round = 0
while not rospy.is_shutdown():
    if round==0:
        pick_and_place_robot.run_first_pp_program()
        round = 1
    else:
        pick_and_place_robot.run_pp_program(prog_name)
# In a different file
dispense = Dual_Move()
while not rospy.is_shutdown():
    # wait for the signal from    
    dispense.run_d_program()
    