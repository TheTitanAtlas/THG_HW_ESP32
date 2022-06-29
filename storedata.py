def calc():
    from distance import HCSR04
    import time
    from time import sleep
    import dstemp

    waterlevel= [0,0,0,0,0]
    x = 1

    while x < 6:
        sensor = HCSR04(trigger_pin=13, echo_pin=12, echo_timeout_us=10000)
        waterlevel[x-1] = sensor.distance_cm()
        x+=1
        time.sleep(0.2)

    waterlevel.sort()
    return waterlevel[2]

def setLevel():
    from distance import HCSR04
    import sender
    import time
    import json
    maxWaterLevel = 0
    level= [0,0,0,0,0]
    z = 1
    while z < 6:
        sensor2 = HCSR04(trigger_pin=13, echo_pin=12, echo_timeout_us=10000)
        level[z-1] = sensor2.distance_cm()
        z+=1
        time.sleep(0.2)

    level.sort()
    with open('waterdata.json', 'r') as f:
        tempdata = json.load(f)

    wdata = tempdata
    wdata['wdata']=level[2]

    with open('waterdata.json', 'w') as f:
        json.dump(wdata, f)
    time.sleep(0.2)
    with open('waterdata.json', 'r') as file:
        tdata = json.load(file)
        maxwater = tdata['wdata']
    sender.send_distance(100-10*(calc()-maxwater))
