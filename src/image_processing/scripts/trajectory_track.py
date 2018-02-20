#!/usr/bin/env python
import robot
import time
import rospy
import math
import numpy as np
import pathPlanning
from image_processing.msg import route
from image_processing.msg import bot_state

path_x = np.array(50, dtype=np.uint64)
path_y = np.array(50, dtype=np.uint64)

call = 0
def traj_gen(path_x,path_y):
    print "at path"
    if (call == 0):
        global call
        call = 1
        print "call:", call
        time, x, y, x_dot, y_dot = pathPlanning.curve_fit((np.asarray(path_x)),(np.asarray(path_y)))
        #print "traj received"
        time_period = time[1]-time[0]
        rate = rospy.Rate(1/time_period)

        # x_dot = np.zeros(100)
        # y_dot = np.linspace(20,10,100)

# x_dot > 0 , then direction = LEFT
# y_dot > 0, then direction =  DOWN
        for i in range(len(time)):
            bot3.kinematic_model(y_dot[i]*8, x_dot[i]*8)
            print "x_dot:", x_dot[i], "y_dot:", y_dot[i]
            rate.sleep()


        bot3.kinematic_model(0, 0)

def callback_points(msg):

    path_x = msg.x
    path_y = msg.y
    #print "at callback:", path_x, ":", path_y
    traj_gen(path_x, path_y)

def callback_bot(msg):
    if msg.num_circles == 3:
        #print "x:", msg.pose.x, "y:", msg.pose.y, "theta:", msg.pose.theta
        bot3.update_state((msg.pose.x,msg.pose.y,msg.pose.theta))


if __name__ =="__main__":
    flag = 0
    try:
        bot3=robot.robot()
        rospy.init_node('trajectory_track',anonymous=True)
        rospy.Subscriber('path',route,callback_points)
        rospy.Subscriber('bot_states',bot_state,callback_bot)

        print "Waiting for path..."
        while not rospy.is_shutdown():
            flag = 1



        #pathPlanning.curve_fit(np.asarray(route_path))
        #rospy.spin()
    except rospy.ROSInterruptException:
        pass
