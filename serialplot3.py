import numpy as np
import serial
import time
import matplotlib.pyplot as plt # import matplotlib library
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax = plt.axes(xlim=(0, 360, ), ylim=(-1, 100))
line, = ax.plot([], [], 'ro', animated=True, lw=2)
print('init vars')
t, f1, f2, f3 , force = [], [], [], [], [[], [], []]
force 

def plotValues():
        plt.title('Force Sensor Demonstration', fontsize = "16")
        plt.grid(True)
        plt.xlabel("Timestamp [s]", fontsize = "14")
        plt.ylabel("Force [N]", fontsize = "14")
        plt.plot(values, 'rx-', label='values')
        plt.legend(loc='upper left')

ser = serial.Serial('/dev/ttyACM0', 115200);
print('Serial initialization attempt');

def init():
    print('init function enter')
    line.set_data([], [])
    return line,

def update(frame):
    print('UPDATING:-------------------SERIAL DATA      -------------------')
    data_raw = ser.readline().decode().strip("\n");
    print(data_raw)
    tmp = data_raw.split(",")
    print(tmp)
    t = float(tmp[0]); print('t')
    f1 = float(tmp[1]); f2 = float(tmp[2]); f3 = float(tmp[3])
    force = [[f1], [f2], [f3]]
    print(force)
    print('force:::');print(f1);print(f2);print(f3);
    print('UPDATING:-------------------            FRAME----------------------')
    xdata.append(frame)
    ydata.append(frame)
    ln.set_data(t, force)
    return ln,

#class matplotlib.animation.FuncAnimation(fig, func, timestamp=None, init_func=None, fargs=None, save_count=None, **kwargs)[source]
ani = FuncAnimation(fig, update, init_func=init, interval=20, blit=True)

plt.show()
