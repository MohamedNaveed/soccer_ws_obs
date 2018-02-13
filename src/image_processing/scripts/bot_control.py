#!/usr/bin/env python
import robot
import time
import rospy
import math
from image_processing.msg import ball
from image_processing.msg import bot_state
from image_processing.msg import ball_predict

def callback_bot(msg):
    if msg.num_circles == 3:
        print "x:", msg.pose.x, "y:", msg.pose.y, "theta:", msg.pose.theta
        bot3.update_state((msg.pose.x,msg.pose.y,msg.pose.theta))


if __name__=="__main__":
    try:
        bot3=robot.robot()
        rospy.init_node('track_bot',anonymous=True)
        rospy.Subscriber('bot_states',bot_state,callback_bot)
        print "Waiting..."

        while not rospy.is_shutdown():
            print "inside while"
            bot3.go_to_goal(0, 20, 0) #x_dot, y_dot, w
            #rospy.spin()

    except rospy.ROSInterruptException:
        pass
