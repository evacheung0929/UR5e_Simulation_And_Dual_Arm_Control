#! /usr/bin/env python

import rospy
from ur_msgs.msg import IOStates
from Io_State_Check import IO_Status

class IO_Pub:
    def __init(self):
        rospy.init_node('pickAndPlace_io_results')
        self.rate = rospy.Rate(10)

        self.p_io_state = IO_Status(3)
        self.p_io_state.listening()

    def p_io_publish(self):
        pub = rospy.Publisher("testingggggggggggpafkldsajfldfa", IOStates, queue_size= 5)
        while not rospy.is_shutdown():
            rospy.loginfo('suoooo')
            pub.publish(self.p_io_state.call_back)
            self.rate.sleep()

io_pub = IO_Pub()
io_pub.p_io_publish()