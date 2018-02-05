import numpy as np
import matplotlib.pyplot as plt

#def Traj_gen(ui, ui_dot, ui_ddot, uf, uf_dot, uf_ddot, t0, tf, step):
t0 = 1
tf = 3
M = np.matrix([[1,t0,t0**2,t0**3,t0**4,t0**5],[0,1,2*t0,3*t0**2,4*t0**3,5*t0**4],[0,0,2,6*t0,12*t0**2,20*t0**3],[1,tf,tf**2,tf**3,tf**4,tf**5],[0,1,2*tf,3*tf**2,4*tf**3,5*tf**4],[0,0,2,6*tf,12*tf**2,20*tf**3]])
print M
a = []
ui = 1
ui_dot = 0
ui_ddot = 0.1
uf = 5
uf_dot = 0
uf_ddot = 0
b = [ui, ui_dot, ui_ddot, uf, uf_dot, uf_ddot]
print b
M_inv = np.linalg.inv(M)	
a = np.matmul(M_inv, b)
print a
# print a.shape
t = np.linspace(t0, tf, 50)
X = np.zeros(len(t))
print a
# for j in range(50):
#     X[j] = a[0] + a[1]*t[i] + a[2]*(t[i]**2) + a[3]*(t[i]**3) + a[4]*(t[i]**4) + a[5]*(t[i]**5)
# print X
#plt.plot(time_x, x, 'o', time_x_new, new_x, time_x_new, new_x_dot, 'x')
# plt.xlim([time_x[0]-1, time_x[-1] + 1 ])
# plt.ylim([0, 15 ])
plt.show()
