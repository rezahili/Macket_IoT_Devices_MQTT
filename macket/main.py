import random
import paho.mqtt.publish as publish
import time
import json
import os
#ENV
Address = os.environ.get("ADDRESS")
Mqtt_port = int(os.environ.get("PORT"))
Delay = int(os.environ.get("DELAY"))

#Random values
current = [10,11,12,14,15,13.2,12.1,14.2,6.5]
fan = [0,1]
gas =  [0,1]
temp = [18,19,20,21,22.3,23,24,25,26,27,50,35.5,24.3,24.2]
door = [0,1]
lux = [10,200,400]
humidity = [20,73,80,85,100]
mobility = [0,1]

while True :
    try:
       publish.single( Address +"/fan01" , json.dumps({"Value" : random.choice(fan)}), qos=2, retain=False, hostname="localhost",
            port=Mqtt_port, client_id="fan01", keepalive=60)
       time.sleep(Delay)
       publish.single(Address + "/gas01" , json.dumps({"Value" : random.choice(gas)}), qos=2, retain=False, hostname="localhost",
            port=Mqtt_port, client_id="gas01", keepalive=60)
       time.sleep(Delay) 
       publish.single(Address + "/current01" , json.dumps({"Value" : random.uniform(10 , 15)}), qos=2, retain=False, hostname="localhost",
            port=Mqtt_port, client_id="current01", keepalive=60)
       time.sleep(Delay) 
       publish.single(Address + "/temp01" , json.dumps({"Value" : random.uniform(18,30)}), qos=2, retain=False, hostname="localhost",
            port=Mqtt_port, client_id="temp01", keepalive=60)
       time.sleep(Delay) 
       publish.single(Address + "/door01" , json.dumps({"Value" : random.choice(door)}), qos=2, retain=False, hostname="localhost",
            port=Mqtt_port, client_id="door01", keepalive=60)
       time.sleep(Delay)
       publish.single(Address + "/lux01" , json.dumps({"Value" : random.choice(lux)}), qos=2, retain=False, hostname="localhost",
            port=Mqtt_port, client_id="lux01", keepalive=60)
       time.sleep(Delay)
       publish.single(Address + "/humidity01" , json.dumps({"Value" : random.choice(humidity)}), qos=2, retain=False, hostname="localhost",
            port=Mqtt_port, client_id="humidity01", keepalive=60)
       time.sleep(Delay)


    except Exception as e:
        print(e)
        continue   
