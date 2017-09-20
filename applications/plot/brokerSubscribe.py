#!/usr/bin/env python


import paho.mqtt.client as mqtt
import sys
import json
import requests
import time
from influxdb import InfluxDBClient





influxClient = InfluxDBClient('127.0.0.1', 8086, 'root', 'root', 'streetlight')



# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("70b3d58ff0031de5")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

    print msg.payload
    epochTime = int(time.time()) * 1000000000

    decodedData = json.loads(msg.payload)["data"]
    series = []
    pointValues = {
        "time": epochTime,
        "measurement": "caseTemperature",
        'fields': {
            'value': decodedData["caseTemperature"],
        },
        'tags': {
            "sensorName": "caseTemperature",
        },
    }
    series.append(pointValues)




    pointValues = {
        "time": epochTime,
        "measurement": "powerConsumption",
        'fields': {
            'value': decodedData["powerConsumption"],
        },
        'tags': {
            "sensorName": "powerConsumption",
        },
    }
    series.append(pointValues)




    pointValues = {
        "time": epochTime,
        "measurement": "luxOutput",
        'fields': {
            'value': decodedData["luxOutput"],
        },
        'tags': {
            "sensorName": "luxOutput",
        },
    }
    series.append(pointValues)

    print series

    
    influxClient.write_points(series, time_precision='n')

    





client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("admin","admin@123")

client.connect("10.156.14.6", 2333, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()








