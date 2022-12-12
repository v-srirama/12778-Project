#from Button import Button
from hx711 import HX711
from machine import Pin
import time

#setting LED pin
led = Pin('LED', Pin.OUT)

#setting load cell 1 pin
pin_OUT1 = Pin(4, Pin.IN, pull=Pin.PULL_DOWN)
pin_SCK1 = Pin(2, Pin.OUT)

#setting load cell 2 pin
pin_OUT2 = Pin(3, Pin.IN, pull=Pin.PULL_DOWN)
pin_SCK2 = Pin(2, Pin.OUT)

#setting load cell 3 pin
pin_OUT3 = Pin(16, Pin.IN, pull=Pin.PULL_DOWN)
pin_SCK3 = Pin(2, Pin.OUT)

#setting load cell 4 pin
pin_OUT4 = Pin(15, Pin.IN, pull=Pin.PULL_DOWN)
pin_SCK4 = Pin(2, Pin.OUT)

#setting pins to HX711 module
hx711_1 = HX711(pin_SCK1, pin_OUT1)
hx711_2 = HX711(pin_SCK2, pin_OUT2)
hx711_3 = HX711(pin_SCK3, pin_OUT3)
hx711_4 = HX711(pin_SCK4, pin_OUT4)

#setting up button  and press counter
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
numberofpress = 0
#Calibration at 0

#calibrating values initializing
calibrate_value1 = 0
calibrate_value2 = 0
calibrate_value3 = 0
calibrate_value4 = 0

#enter number of loops for calibrating
looper = 1

weight = 0

while numberofpress == 0:
    led.toggle()
    time.sleep(0.3)
    if button.value():
        led.value(1)
        for i in range(looper):
            value1 = hx711_1.read_average(times = 10)
            value2 = hx711_2.read_average(times = 10)
            value3 = hx711_3.read_average(times = 10)
            value4 = hx711_4.read_average(times = 10)
            calibrate_value1+= value1
            calibrate_value2+= value2
            calibrate_value3+= value3
            calibrate_value4+= value4
            print('load cell 1: ',value1,'\n','load cell 2:' ,value2,'\n','load cell 3: ', value3,'\n','load cell 4: ',value4)
        calibrate_value1 = calibrate_value1/looper
        calibrate_value2 = calibrate_value2/looper
        calibrate_value3 = calibrate_value3/looper
        calibrate_value4 = calibrate_value4/looper

        print('the calibrated value load cell 1 for 0 gms :',calibrate_value1)
        print('the calibrated value load cell 2 for 0 gms :',calibrate_value2)
        print('the calibrated value load cell 3 for 0 gms :',calibrate_value3)
        print('the calibrated value load cell 4 for 0 gms :',calibrate_value4)
        numberofpress +=1

#Calibration at some weight

#calibrating values
weight1 = 50
weight2 = 502.84
weight3 = 363.23
weight4 = 26.28
calibrate_value50 = 0
calibrate_value_1_50= 0
calibrate_value_2_50= 0
calibrate_value_3_50=0
calibrate_value_4_50=0

#enter number of loops for calibrating
looper = 1


while numberofpress == 1:
    led.toggle()
    time.sleep(0.3)
    if button.value():
        led.value(1)
        for i in range(looper):
            value1 = hx711_1.read_average(times = 10)
            value2 = hx711_2.read_average(times = 10)
            value3 = hx711_3.read_average(times = 10)
            value4 = hx711_4.read_average(times = 10)
            calibrate_value_1_50+= value1
            calibrate_value_2_50+= value2
            calibrate_value_3_50+=value3
            calibrate_value_4_50+=value4
            print('load cell 1: ',value1,'\n','load cell 2:' ,value2,'\n','load cell 3: ', value3,'\n','load cell 4: ',value4)
        calibrate_value_1_50 = calibrate_value_1_50/looper
        calibrate_value_2_50 = calibrate_value_2_50/looper
        calibrate_value_3_50 = calibrate_value_3_50/looper
        calibrate_value_4_50 = calibrate_value_4_50/looper
        print('the calibrated value for',weight1,' gms :',calibrate_value_1_50)
        print('the calibrated value for',weight2,' gms :',calibrate_value_2_50)
        print('the calibrated value for',weight3,' gms :',calibrate_value_3_50)
        print('the calibrated value for',weight4,' gms :',calibrate_value_4_50)
        numberofpress +=1

for i in range(10):
    raw_value1 = hx711_1.read_average(times=10)
    raw_value2 = hx711_2.read_average(times=10)
    raw_value3 = hx711_3.read_average(times=10)  
    raw_value4 = hx711_4.read_average(times=10)

    x1 = ((raw_value1-calibrate_value_1_50)*weight1/(calibrate_value_1_50-calibrate_value1))+weight1
    x2 = ((raw_value2-calibrate_value_2_50)*weight2/(calibrate_value_2_50-calibrate_value2))+weight2
    x3 = ((raw_value3-calibrate_value_3_50)*weight3/(calibrate_value_3_50-calibrate_value3))+weight3
    x4 = ((raw_value4-calibrate_value_4_50)*weight4/(calibrate_value_4_50-calibrate_value4))+weight4

    print("Weight of the object placed on load cell 1: ",x1)
    print("Weight of the object placed on load cell 2: ",x2)
    print("Weight of the object placed on load cell 3: ",x3)
    print("Weight of the object placed on load cell 4: ",x4)
   
    total_weight = x1+x2+x3+x4
    print("Total weight",total_weight)
    time.sleep(0.5)
   

# Placing the board

# variables
board_weight = 0
leg_1 = 0
leg_2 = 0
leg_3 = 0
leg_4 = 0

#enter number of loops for calibrating board
looper = 1

while numberofpress == 2:
    led.toggle()
    time.sleep(0.3)
    if button.value():
        led.value(1)
        for i in range(looper):
            raw_value1 = hx711_1.read_average(times=10)
            raw_value2 = hx711_2.read_average(times=10)
            raw_value3 = hx711_3.read_average(times=10)  
            raw_value4 = hx711_4.read_average(times=10)

            x1 = ((raw_value1-calibrate_value_1_50)*weight1/(calibrate_value_1_50-calibrate_value1))+weight1
            x2 = ((raw_value2-calibrate_value_2_50)*weight2/(calibrate_value_2_50-calibrate_value2))+weight2
            x3 = ((raw_value3-calibrate_value_3_50)*weight3/(calibrate_value_3_50-calibrate_value3))+weight3
            x4 = ((raw_value4-calibrate_value_4_50)*weight4/(calibrate_value_4_50-calibrate_value4))+weight4

            print("Weight of the object placed on load cell 1: ",x1)
            print("Weight of the object placed on load cell 2: ",x2)
            print("Weight of the object placed on load cell 3: ",x3)
            print("Weight of the object placed on load cell 4: ",x4)
               
            total_weight=x1+x2+x3+x4
            print("Total weight",total_weight)
           
            board_weight= board_weight + total_weight
            leg_1 = leg_1 +x1
            leg_2 = leg_2 +x2
            leg_3 = leg_3 +x3
            leg_4 = leg_4 +x4
            time.sleep(0.5)
           
        board_weight = board_weight/looper
        leg_1 = leg_1/looper
        leg_2 = leg_2/looper
        leg_3 = leg_3/looper
        leg_4 = leg_4/looper
        numberofpress +=1
   
while True:
    led.value(0)
    raw_value1 = hx711_1.read_average(times=10)
    raw_value2 = hx711_2.read_average(times=10)
    raw_value3 = hx711_3.read_average(times=10)  
    raw_value4 = hx711_4.read_average(times=10)
   # wt = (raw_value* (ref_wt/ref_value))
    x1 = ((raw_value1-calibrate_value_1_50)*weight1/(calibrate_value_1_50-calibrate_value1))+weight1
    x2 = ((raw_value2-calibrate_value_2_50)*weight2/(calibrate_value_2_50-calibrate_value2))+weight2
    x3 = ((raw_value3-calibrate_value_3_50)*weight3/(calibrate_value_3_50-calibrate_value3))+weight3
    x4 = ((raw_value4-calibrate_value_4_50)*weight4/(calibrate_value_4_50-calibrate_value4))+weight4
    print('x1:', x1, '\n', 'x2:', x2, '\n', 'x3:', x3, '\n', 'x4:', x4, '\n')
    print("Weight on leg 1: ",x1-leg_1)
    print("Weight on leg 2: ",x2-leg_2)
    print("Weight on leg 3: ",x3-leg_3)
    print("Weight on leg 4: ",x4-leg_4)
       
    total_weight=x1+x2+x3+x4
    print("Total weight",total_weight-board_weight)
    tared = abs(total_weight-board_weight)
   

    if abs(tared)>10:
        led.value(1)
        raw_value1 = hx711_1.read_average(times=10)
        raw_value2 = hx711_2.read_average(times=10)
        raw_value3 = hx711_3.read_average(times=10)  
        raw_value4 = hx711_4.read_average(times=10)
       # wt = (raw_value* (ref_wt/ref_value))
        x1 = ((raw_value1-calibrate_value_1_50)*weight1/(calibrate_value_1_50-calibrate_value1))+weight1
        x2 = ((raw_value2-calibrate_value_2_50)*weight2/(calibrate_value_2_50-calibrate_value2))+weight2
        x3 = ((raw_value3-calibrate_value_3_50)*weight3/(calibrate_value_3_50-calibrate_value3))+weight3
        x4 = ((raw_value4-calibrate_value_4_50)*weight4/(calibrate_value_4_50-calibrate_value4))+weight4
        #load_change = checker - [x1-leg_1,x2-leg_2,x3-leg_3,x4-leg_4]
        l1,l2,l3,l4 = abs(x1-leg_1),abs(x2-leg_2),abs(x3-leg_3),abs(x4-leg_4)
        cumm_load1= l1 + l4
        cumm_load3= l3 + l4

        x_axis= cumm_load1*22/tared
        y_axis= cumm_load3*22/tared
        print('The coordinates of change in weight is', x_axis, y_axis)
        if (x_axis-0.5)//2.625 == -1:
            ax = 'A'
            print('weight changed occured at A or something went wrong!')
        if (x_axis-0.5)//2.625 == 0:
            ax = 'A'
            print('weight changed occured at A')
        if (x_axis-0.5)//2.625 == 1:
            ax = 'B'
            print('weight changed occured at B')
        if (x_axis-0.5)//2.625 == 2:
            ax = 'C'
            print('weight changed occured at C')
        if (x_axis-0.5)//2.625 == 3:
            ax = 'D'
            print('weight changed occured at D')
        if (x_axis-0.5)//2.625 == 4:
            ax = 'E'
            print('weight changed occured at E')
        if (x_axis-0.5)//2.625 == 5:
            ax = 'F'
            print('weight changed occured at F')
        if (x_axis-0.5)//2.625 == 6:
            ax = 'G'
            print('weight changed occured at G')
        if (x_axis-0.5)//2.625 == 7:
            ax = 'H'
            print('weight changed occured at H')
        if (x_axis-0.5)//2.625 == 8:
            ax = 'H'
            print('weight changed occured at H or something went wrong!')
        
        if (y_axis-0.5)//2.625 == -1:
            ay = '1'
            print('weight changed occured at 1 or something went wrong!')
        if (y_axis-0.5)//2.625 == 0:
            ay = '1'
            print('weight changed occured at 1')
        if (y_axis-0.5)//2.625 == 1:
            ay = '2'
            print('weight changed occured at 2')
        if (y_axis-0.5)//2.625 == 2:
            ay = '3'
            print('weight changed occured at 3')
        if (y_axis-0.5)//2.625 == 3:
            ay = '4'
            print('weight changed occured at 4')
        if (y_axis-0.5)//2.625 == 4:
            ay = '5'
            print('weight changed occured at 5')
        if (y_axis-0.5)//2.625 == 5:
            ay = '6'
            print('weight changed occured at 6')
        if (y_axis-0.5)//2.625 == 6:
            ay = '7'
            print('weight changed occured at 7')
        if (y_axis-0.5)//2.625 == 7:
            ay = '8'
            print('weight changed occured at 8')
        if (y_axis-0.5)//2.625 == 8:
            ay = '8'
            print('weight changed occured at H or something went wrong!')
            
        looper=1
        board_weight = 0
        leg_1 = 0
        leg_2 = 0
        leg_3 = 0
        leg_4 = 0
        for i in range(looper):
            raw_value1 = hx711_1.read_average(times=10)
            raw_value2 = hx711_2.read_average(times=10)
            raw_value3 = hx711_3.read_average(times=10)  
            raw_value4 = hx711_4.read_average(times=10)

            x1 = ((raw_value1-calibrate_value_1_50)*weight1/(calibrate_value_1_50-calibrate_value1))+weight1
            x2 = ((raw_value2-calibrate_value_2_50)*weight2/(calibrate_value_2_50-calibrate_value2))+weight2
            x3 = ((raw_value3-calibrate_value_3_50)*weight3/(calibrate_value_3_50-calibrate_value3))+weight3
            x4 = ((raw_value4-calibrate_value_4_50)*weight4/(calibrate_value_4_50-calibrate_value4))+weight4

            print("Weight of the object placed on load cell 1: ",x1)
            print("Weight of the object placed on load cell 2: ",x2)
            print("Weight of the object placed on load cell 3: ",x3)
            print("Weight of the object placed on load cell 4: ",x4)
               
            total_weight=x1+x2+x3+x4
            print("Total weight",total_weight)
           
            board_weight= board_weight + total_weight
            leg_1 = leg_1 +x1
            leg_2 = leg_2 +x2
            leg_3 = leg_3 +x3
            leg_4 = leg_4 +x4
            time.sleep(0.5)
           
        board_weight = board_weight/looper
        leg_1 = leg_1/looper
        leg_2 = leg_2/looper
        leg_3 = leg_3/looper
        leg_4 = leg_4/looper
    time.sleep(0.5)    


