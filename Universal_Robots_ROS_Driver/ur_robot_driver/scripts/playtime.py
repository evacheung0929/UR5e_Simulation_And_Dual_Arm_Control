#! /usr/bin/env python
'''This determines how long you would like to program to run for'''
import timeit
import rospy#
from dashboard_client import Dashboard_Client 
class Run_Time:
    def __init__(self):
        self.t_start = timeit.default_timer()
        self.t_duration = timeit.default_timer()
        self.on = True
        self.dashboard = Dashboard_Client()

    def set_timer(self, timesup):
        count = 0
        while self.on:
            if (self.t_duration - self.t_start) < timesup:
                self.dashboard.play()
                if count == 0:
                    rospy.loginfo("Robot starting to move, running program")  
                    print('hey')
                    count = 1  
                    self.t_duration = timeit.default_timer()       
                self.t_duration = timeit.default_timer()
            else:
                self.dashboard.pause()
                rospy.loginfo("Time is up, the current program has been paused")
                print('stop')
                self.on = False

# run = Run_Time()
# run.set_timer(5)