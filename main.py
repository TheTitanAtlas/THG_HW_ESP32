import machine
import distance
from distance import HCSR04
import dstemp
from machine import Pin
import time
import esp32
import utime
from time import sleep
import boot
import storedata
import sender
import mqtt
import json
p2led = Pin(2, Pin.OUT)

y=0
while True:
    if y < 6:
        time.sleep(10)
        sender.client.check_msg()
        y+=1
    elif y == 6:
        y=0
        with open('waterdata.json', 'r') as file:
            tdata = json.load(file)
            maxwater = tdata['wdata']
        p2led.value(1)
        time.sleep(0.6)
        p2led.value(0)
        time.sleep(1)
        sender.send_temp(dstemp.temp_measure())
        currentLevel = storedata.calc()
        if currentLevel >= 10:
            currentLevel = 10 + maxwater
        sender.send_distance(100-10*(currentLevel-maxwater))
    #do_connect("Temp in apartment: " + str(dstemp.temp_measure()) + "Distance from device: " + str(sensor.distance_cm())+ "cm" +"Read from memory: " + str(data))
