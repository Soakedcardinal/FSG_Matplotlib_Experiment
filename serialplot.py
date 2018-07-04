import numpy 
import matplotlib.pyplot as plt # import matplotlib library
import serial
from drawnow import *
fig, ax = plt.subplots()
line, = ax.plot(np.random.rand(10))
ax.set_ylim(0, 150)
xdata, ydata = [0]*100, [0]*100
ser = serial.Serial("/dev/ttyACM0",115200)

while True: # While loop that loops forever
	while (ser.inWaiting()==0): #Wait here until there is data
		pass #do nothing
	data_str = ser.readline()
	print data_str

