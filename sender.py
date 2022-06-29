import time                   # Allows use of time.sleep() for delays                # Base library for Pycom devices
from mqtt import MQTTClient  # For use of MQTT protocol to talk to Adafruit IO
import ubinascii              # Needed to run any MicroPython code
import machine                # Interfaces with hardware components
import micropython            # Needed to run any MicroPython code
import storedata
import config


# Adafruit IO (AIO) configuration
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "AtlasO"
AIO_KEY = config.AIOKEY
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())  # Can be anything
TEMP_FEED = "AtlasO/feeds/tinyhydrogarden.temp"
DISTANCE_FEED = "AtlasO/feeds/tinyhydrogarden.waterlevel"
RESET_FEED = "AtlasO/feeds/tinyhydrogarden.resetwaterlevel"
# Function to respond to messages from Adafruit IO

def sub_cb(topic, msg):
    print((topic, msg))
    if msg == b"1":
        storedata.setLevel()
    elif msg == b"0":
        pass
    else:
        print("Value is out of bounds")

def send_temp(value):
    print("temp:", value)
    try:
        client.publish(topic=TEMP_FEED, msg=str(value))
        print("DONE")
    except Exception as e:
        print("FAILED")

def send_distance(value):

    print("distance",value)
    if value >= 105:
        value =0
    try:
        client.publish(topic=DISTANCE_FEED, msg=str(value))
        print("DONE")
    except Exception as e:
        print("FAILED")


# Use the MQTT protocol to connect to Adafruit IO
client = MQTTClient(AIO_CLIENT_ID, AIO_SERVER, AIO_PORT, AIO_USER, AIO_KEY)

# Subscribed messages will be delivered to this callback
client.set_callback(sub_cb)
client.connect()
client.subscribe(RESET_FEED)
print("Connected to %s, subscribed to %s topic" % (AIO_SERVER, RESET_FEED))
