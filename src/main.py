"""
    @file                    main.py
    @brief                   This file allows us to call an interrupt function 
    @details                 This file will run, wait for an input, and then print 
                             the ADC readings from our RC circuit. The printed data
                             will be collected in portreaderLab4.py and then a plot
                             will be generated and exported as a .png file. 
    @author                  Daniel Gonzalez
    @author                  Nolan Clapp
    @author                  Caleb Kephart
    @date                    Feburary 14, 2022
"""
import task_share
import pyb
import micropython
from pyb import ADC
import time


micropython.alloc_emergency_exception_buf(100)

##  @brief Variable for Queue
#   @details This variable sets up a shared queue that is 1000 long and takes in 16-bit integers
q0 = task_share.Queue ('L', 1000, thread_protect = False, overwrite = False, name = "Queue 0")


##  @brief Variable for the output pin
#   @details Sets up variable for the output pin using pin C1 on the Nucleo
pinC1=pyb.Pin(pyb.Pin.cpu.C1, pyb.Pin.OUT_PP)

##  @brief Variable for the ADC pin
#   @details Sets up variable for the ADC pin we will read from using pin C0 on the Nucleo
pinC0=pyb.Pin(pyb.Pin.cpu.C0)

##  @brief Variable to take ADC readings
#   @details Sets up variable to take ADC readings from pinC0
myadc=pyb.ADC(pinC0)
pinC1.low()
time.sleep(1)
##  @brief Sets up timer 1
#   @details sets up timer as timer 1 on the nucleo using pyb.Timer and then determining the frequency
tim1=pyb.Timer(1)
tim1.init(freq=3000)

def interruptfunc(tim1):
    '''
        Creates an interrupt function that will add the current ADC reading
        to shared variable q0. 
        @param tim1 Varaible for the timer object we are passing in
    '''
    q0.put(myadc.read(),in_ISR=True)


## @brief Variable to wait for input to allow us to run portreader file
x=int(input())
tim1.callback(interruptfunc)
time.sleep_ms(100)
pinC1.high()
#time.sleep(2)


while x<=10:
    try: 
        print(q0.get())
        time.sleep_ms(5)
    except KeyboardInterrupt: 
        print("Stop Data")
        tim1.callback(None)
