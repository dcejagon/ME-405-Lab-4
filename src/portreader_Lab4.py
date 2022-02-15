"""
    @file                    EncoderDriver.py
    @author                  Daniel Gonzalez
    @author                  Nolan Clapp
    @author                  Caleb Kephart
    @date                    January 31, 2022
"""

import time
import serial 
from matplotlib import pyplot as plt


with serial.Serial ('COM26', 115200) as ser_port:
    
    ser_port.write (b'0\r\n')
    time.sleep(5)
    ser_port.write(b'\x03')
    data_results=[]
    while True :
        try:
            line = ser_port.readline().strip().decode()
            print (line)
            data_results.append(line)
            if line == 'Stop Data':

                raise KeyboardInterrupt    
        except KeyboardInterrupt:
            break
        
data_results = ','.join(data_results).split(',')
print(data_results)   

data_results.pop(len(data_results)-1)
data_results.pop(0)

for i in range(0, len(data_results)):
   data_results[i] = int(data_results[i])

Time = range(0,len(data_results))


plt.scatter(Time,data_results)
plt.plot(Time,data_results)

# Axis Labeling
plt.xlabel('Time (ms)') 
plt.ylabel('ADC Step Response (ticks)') 
    
# Graph Title
plt.title('Lab 4 Plots') 
plt.savefig('RC_Circuit_Responce2.png')
plt.show()

