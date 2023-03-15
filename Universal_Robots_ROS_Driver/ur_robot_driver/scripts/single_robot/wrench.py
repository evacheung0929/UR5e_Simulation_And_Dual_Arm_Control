#!/usr/bin/env/ python
'''This is unfinished'''
import rospy
from geometry_msgs.msg import Wrench

def callback(data):
    rospy.loginfo("Here is the result of using Wrench topic")
    rospy.loginfo("================================")
    rospy.loginfo("================================")
    rospy.loginfo("================================")
    rospy.loginfo("Force z:{}".format(msg.force.x))
    rospy.loginfo("Force z:{}".format(msg.force.y))
    rospy.loginfo("Force z:{}".format(msg.force.z))
    rospy.loginfo("================================")
    rospy.loginfo("================================")
    rospy.loginfo("================================")
    rospy.loginfo("Torque z:{}".format(msg.torque.X))
    rospy.loginfo("Torque z:{}".format(msg.torque.Y))
    rospy.loginfo("Torque z:{}".format(msg.torque.z))

def listener():
    rospy.init_node('/ft_wrench')
    rospy.Subscriber('/wrench',Wrench, callback)
    w = Wrench()
    # rospy.Publisher('/wrench',)
    rospy.Rate(1)
    rospy.sleep()
    rospy.spin()

# # Obtain torque used by screwdriver (rotation motion), torque = r x F
# w = Wrench()
# # distance meausred in meter, torque is measured in N/m
# distance = 0.5
# threshold = 0.7
# torque  = (w.force.x)*distance
# # once reached the waypoint, zero the ft sensor?
# if torque>threshold:


# if __name__ == '__main__':
#     listener()