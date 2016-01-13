#!/usr/bin/python

import smbus
import math
import RPi.GPIO as gpio
import time
import sys


# ================ MPU6050 ============

# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)


bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
address = 0x68       # This is the address value read via the i2cdetect command

# Now wake the 6050 up as it starts in sleep mode
bus.write_byte_data(address, power_mgmt_1, 0)

# ================ ./MPU6050 ============

# ================ motor controller ============

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

def forward(tf):
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()

# ================ ./motor controller ============

def key_input(event):
    init()
    print 'Key:', event.char
    key_press = event.char
    sleep_time = 0.030

    if key_press.lower() == 'w':
        forward(sleep_time)
    elif key_press.lower() == 's':
        reverse(sleep_time)
    elif key_press.lower() == 'a':
        turn_left(sleep_time)
    elif key_press.lower() == 'd':
        turn_right(sleep_time)
    elif key_press.lower() == 'q':
        pivot_left(sleep_time)
    elif key_press.lower() == 'e':
        pivot_right(sleep_time)
    elif key_press.lower() == 'c':
        turn_rightback(sleep_time)
    elif key_press.lower() == 'z':
        turn_leftback(sleep_time)
    else:
        pass

# ------------------- motors sleep time -------------------------
sleep_time =0.07375

while True:
    # ------------------------ MPU-6050 sleep time --------------------
    time.sleep(0.055)
    gyro_xout = read_word_2c(0x43)
    gyro_yout = read_word_2c(0x45)
    gyro_zout = read_word_2c(0x47)

    #print "gyro_xout : ", gyro_xout, " scaled: ", (gyro_xout / 131)
    #print "gyro_yout : ", gyro_yout, " scaled: ", (gyro_yout / 131)
    #print "gyro_zout : ", gyro_zout, " scaled: ", (gyro_zout / 131)

    accel_xout = read_word_2c(0x3b)
    accel_yout = read_word_2c(0x3d)
    accel_zout = read_word_2c(0x3f)

    accel_xout_scaled = accel_xout / 16384.0
    accel_yout_scaled = accel_yout / 16384.0
    accel_zout_scaled = accel_zout / 16384.0

    #print "accel_xout: ", accel_xout, " scaled: ", accel_xout_scaled
    #print "accel_yout: ", accel_yout, " scaled: ", accel_yout_scaled
    #print "accel_zout: ", accel_zout, " scaled: ", accel_zout_scaled

    x_rotation = get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
    y_rotation = get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)

    print "x rotation: ",x_rotation
    print "y rotation: ",y_rotation
    print "----------------------------------"

    if y_rotation > 11 :
        #print "forward",sleep_time
        init()
        forward(sleep_time)
    elif y_rotation < -9.8 :
        #print "reverse",sleep_time
        init()
        reverse(sleep_time)
    else:
        print "good"


