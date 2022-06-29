import machine
from machine import Pin
import onewire
import ds18x20
import time
ds_pin = machine.Pin(4)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
rom = roms[0]

def temp_measure():
  ds_sensor.convert_temp()
  time.sleep_ms(750)
  return ds_sensor.read_temp(rom)
