import numpy 
import matplotlib.pyplot as plt # import matplotlib library
import serial
import time
import os
import csv
#import drawnow
#from drawnow import *


data_raw= []

cnt=0
plt.ion() #Tell matplotlib you want interactive mode to plot live data

ser = serial.Serial('/dev/ttyACM1', 115200);
print('initializing')
time.sleep(3)

def plotValues():
        plt.title('Force Sensor Demonstration', fontsize = "16")
        plt.grid(True)
        plt.xlabel("Time [s]", fontsize = "14")
        plt.ylabel("Force [N]", fontsize = "14")
        plt.plot(values, 'rx-', label='values')
        plt.legend(loc='upper left')

#pre-load dummy datAa
##def makeFig(): #Function to create plot
##plt.plot(data_raw)

while True:
    data_raw = ser.readline().decode().strip("\n")
    print(data_raw)
    #data_raw = data_raw.strip('\n')
    #print(data_raw) 
    tmp = data_raw.split(",")
    timestamp = tmp[0]
    f1 = tmp[1]
    f2 = tmp[2]
    f3 = tmp[3]
    timestamp = float(timestamp)
    f1 = float(f1)
    f2 = float(f2)
    f3 = float(f3)
    print('values interpereted: ',timestamp,f1,f2,f3)
##    print(f1)
##    print(f2)
##    print(f3)

    plt.scatter(timestamp,f1,color="red")
    plt.scatter(timestamp,f2,color="blue")
    plt.scatter(timestamp,f3,color="green")
  #  plt.pause(0.008)
    time.sleep(0.01)
    #thyme = time + 0.5

##    with open('/FSG_Matplotlib_Experiment/tmp.csv', 'w') as f:
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
