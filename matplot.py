#!/usr/bin/python
import serial
import time
from time import sleep
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#import csv
import sys
from matplotlib import style
#csvfile = "Vouts.csv"


style.use('fivethirtyeight')
fig1 = plt.figure()

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1, xonxoff=False, rtscts=False, dsrdtr=False)
plt.ion()
ser.flushInput()
ser.flushOutput()

def animate(i):
	ser.reset_input_buffer()
	data = ser.readline().split(',')


t = [] 
vo1 = []
vo2 = []
vo3 = []
for line in lines:
 	if len(line) > 1:
    		x, y = line.split(',')
       		xs.append(x)
       		ys.append(y)
 		ax1.clear()
 		ax1.plot(xs, ys)
ani = animation.FuncAnimation(fig, animate, interval=25)
