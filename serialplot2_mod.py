import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import serial
import os
import csv
##import drawnow
##from drawnow import *

##fig, ax = plt.subplots()
##line, = ax.plot(timestamp, f1, f2, f3)
ser = serial.Serial('/dev/ttyACM1', 115200);
print('initialized');
cnt=0;
dt = 1./30 # 30 fps
fig, ax = plt.subplots()
ax = plt.axes(xlim=(0, 500, ), ylim=(-1, 100))
line, = ax.plot([], [], 'r-', animated=True, lw=2)
plt.ion() #Tell matplotlib you want interactive mode to plot live data

def init():  # only required for blitting to give a clean slate.
   # line.set_ydata([np.nan] * len(x))
    time_text.set_text('')
    energy_text.set_text('')
    line.set_data([], [])
    return line, time_text, energy_text

def plotValues():
        plt.title('Force Sensor Demonstration', fontsize = "16")
        plt.grid(True)
        plt.xlabel("Time [s]", fontsize = "14")
        plt.ylabel("Force [N]", fontsize = "14")
        plt.plot([],[],[],[])
        plt.legend(loc='upper left')
    
    
def animate(i):
    print('UPDATING:-------------------SERIAL DATA      -------------------')
    data_raw = ser.readline().decode().strip("\n")
    tmp = data_raw.split(",")
    t = float(tmp[0])
    f1 = float(tmp[1])
    f2 = float(tmp[2])
    f3 = float(tmp[3])
    print('values interpereted: ',t,f1,f2,f3)
    line.set_data(t, f1)
    return line,
##    plt.scatter(t,f1,color="red")
##    plt.scatter(t,f2,color="blue")
##    plt.scatter(t,f3,color="green")
    #plt.pause(0.01)

from time import time
t0 = time()
animate(0)
t1 = time()
interval = 1000 * dt - (t1 - t0)
    
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=interval, blit=True)
    
    

    #blit
   # time.sleep(0.05)
    #thyme = time + 0.5

##    with open('/FSG_Matplotlib_Experiment/log.csv', 'w') as f:
##        writer = csv.writer(f)
##    for t, f1, f2, f3 in zip(array_data[0], array_data[2], array_data[3], array_data[4]):
##            writer.writerow([t,f1, f2, f3])
            
##while (ser.inWaiting()==0): 
##        pass #do nothing
##    sec = str(data_raw[0])
##    f1 = str(data_raw[1])
    
#print(data_raw)
#print(sec)   #
#println(f1)
##print(connection.readline)
##print(serial.Serial.readline)
##try:
##    ser.isOpen()
##    print("Serial port is open")
##except:
##    print("Error")
##    exit()
##
##if(ser.isOpen()):
##    try:
##        while(1):
##            #t=data[0]
##            #f1=data[1]
##            print(ser.read())
##    except Exception:
##        print("error")
##else:
##    print("cannot open serial port")
##
