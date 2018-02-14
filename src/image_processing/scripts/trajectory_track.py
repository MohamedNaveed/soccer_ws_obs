#!/usr/bin/env python
import robot
import time
import rospy
import math
import numpy as np
import pathPlanning
from image_processing.msg import route


path_x = np.array(50, dtype=np.uint64)
path_y = np.array(50, dtype=np.uint64)

def traj_gen(path_x,path_y):
    #print "at path"
    time, x, y, x_dot, y_dot = pathPlanning.curve_fit((np.asarray(path_x)),(np.asarray(path_y)))
    #print "traj received"
    time_period = time[1]-time[0]
    rate = rospy.Rate(1/time_period)
    for i in range(len(time)):
        bot3.kinematic_model(y_dot[i], x_dot[i])
        print "x_dot:", x_dot[i], "y_dot:", y_dot[i]
        rate.sleep()

def callback_points(msg):

    path_x = msg.x
    path_y = msg.y
    print "at callback"
    traj_gen(path_x, path_y)

if __name__ =="__main__":
    global flag
    flag=0
    try:
        bot3=robot.robot()
        rospy.init_node('trajectory_track',anonymous=True)
        rospy.Subscriber('path',route,callback_points)

        print "Waiting for path..."
        while not rospy.is_shutdown():
            flag = 1


        #pathPlanning.curve_fit(np.asarray(route_path))
        #rospy.spin()
    except rospy.ROSInterruptException:
        pass
