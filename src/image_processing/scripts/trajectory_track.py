#!/usr/bin/env python
import robot
import time
import rospy
import math
import numpy as np
import pathPlanning
from image_processing.msg import route
from image_processing.msg import bot_state
import matplotlib.pyplot as plt

path_x = np.array(50, dtype=np.uint64)
path_y = np.array(50, dtype=np.uint64)

end_x = 1100/18
end_y = 620/12
call = 0
def traj_gen(path_x,path_y):
    print "at path"
    print "path_x : ",path_x, "path_y : ", path_y
    # kp_x = 1.1;     kp_y = 1 ;     kp_theta = 0.0  #kp_x = 1.0;     kp_y = 1.7;     kp_theta = 0.30 ||| kp_x = 0.04 kp_y = 0.05
    # kd_x = 1.5;   kd_y = 1.5;     kd_theta = 0
    # ki_x = 0.002; ki_y = 0.002; ki_theta = 0.0 #ki_x = 0.00020 ki_y = 0.00020
    kp_x = 0.016;     kp_y = 0.015;     kp_theta = 0.0  #kp_x = 1.0;     kp_y = 1.7;     kp_theta = 0.30 ||| kp_x = 0.04 kp_y = 0.05
    kd_x = 0.0;   kd_y = 0.0;     kd_theta = 0.
    ki_x = 0.00; ki_y = 0.00; ki_theta = 0.0 #ki_x = 0.00020 ki_y = 0.00020
    old_error_x = 0.0;    old_error_y = 0.0;    old_error_theta = 0.0;
    sum_x = 0.0;          sum_y = 0.0;          sum_theta = 0.0;

    if (call == 0):
        global call
        call = 1
        print "call:", call
        time, x, y, x_dot, y_dot = pathPlanning.curve_fit((np.asarray(path_x)),(np.asarray(path_y)))
        #print "traj received"
        x_actual = np.zeros(len(x))
        y_actual = np.zeros(len(y))

        time_period = 4*(time[1]-time[0])  # multiplied a factor 2, to increase the frequency to be maintained by rate.sleep
        rate = rospy.Rate(1/time_period)     # .. otherwise bot stops in between

        # x_dot = np.zeros(100)
        # y_dot = np.linspace(20,10,100)

# x_dot > 0 , then direction = down
# y_dot > 0, then direction =  right
        #start = time.time()
        for i in range(len(x_dot)):

            x_actual[i] = bot3.state[0]
            y_actual[i] = bot3.state[1]
            error_x = float(y[i]*end_x - bot3.state[0])#end_x and end_y are multiplied to find the coordinate wrt the image. x,y give the grid coordinates
            error_y = float(x[i]*end_y - bot3.state[1])
            #print "x", y[i]*end_x, "bot_x:", bot3.state[0], "y:", x[i]*end_y, "bot_y:", bot3.state[1]
            print "error_x:", error_x, "error_y:", error_y
            #error_theta = math.atan2(math.sin(math.pi*(destination[2]-bot3.state[2])/180),math.cos(math.pi*(destination[2]-bot3.state[2])/180))
            error_theta = 0
            print "x_dot:", x_dot[i], "y_dot:", y_dot[i]
            y_dot[i] = y_dot[i] + kp_x*error_x + kd_x*(error_x-old_error_x) + ki_x*sum_x
            x_dot[i] = x_dot[i] + kp_y*error_y + kd_y*(error_y-old_error_y) + ki_y*sum_y

            bot3.kinematic_model(x_dot[i], y_dot[i])
            # if x_dot[i] >= 3:
            #     x_dot[i] = 3
            # if y_dot[i] >= 3:
            #     y_dot[i] = 3
            # if x_dot[i] <= -3:
            #     x_dot[i] = -3
            # if y_dot[i] <= -3:
            #     y_dot[i] = -3
            sum_x = sum_x + error_x
            sum_y = sum_y + error_y

            old_error_x = error_x
            old_error_y = error_y

            print "x_dot_p:", x_dot[i], "y_dot_p:", y_dot[i]
            rate.sleep()
        # end = time.time()
        # time_t = end - start
        # print "total points = {0}".format(len(x_dot))
        # print "total time = {0}".format(time_t)

        bot3.kinematic_model(0, 0)

        plt.figure(1)
        plt.subplot(311)
        plt.plot(time,x*end_y, 'o', time, y_actual,'x')
        plt.subplot(312)
        plt.plot(time,y*end_x, 'o', time, x_actual,'x')
        plt.subplot(313)
        plt.plot(y_actual,x_actual,'x',x*end_y,y*end_x,'o')
        plt.show()
def callback_points(msg):

    path_x = msg.x
    path_y = msg.y
    print "at callback:", path_x, ":", path_y
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
