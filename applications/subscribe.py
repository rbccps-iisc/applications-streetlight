#!/usr/bin/env python


import paho.mqtt.client as mqtt
import sys
import json
import requests
import base64


import rxmsg_pb2


from influxdb import InfluxDBClient




rxmsg = rxmsg_pb2.sensor_values()



# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("application/2/node/70b3d58ff0031de5/rx")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

	decodedData = str(base64.b64decode(json.loads(str(msg.payload))["data"]))
	rxmsg.ParseFromString(decodedData)
	print ''
	print 'Temperature ' + str(rxmsg.caseTemperature)
	print 'Time ' + str(rxmsg.dataSamplingInstant/1000) + ' seconds'
	print 'Lux out ' + str(rxmsg.luxOutput)
	print 'power ' + str(rxmsg.powerConsumption)
	print 'Ambient ' + str(rxmsg.ambientLux)
	print 'Slave Alive ' + str(rxmsg.slaveAlive)
	print 'Battery '  + str(rxmsg.batteryLevel)
	print ''
    # series = []

    
    # pointValues = {
    #     "time": decodedData["dataSamplingInstant"],
    #     "measurement": "caseTemperature",
    #     'fields': {
    #         'value': decodedData["caseTemperature"],
    #     },
    #     'tags': {
    #         "sensorName": "caseTemperature",
    #     },
    # }
    # series.append(pointValues)




    # pointValues = {
    #     "time": decodedData["dataSamplingInstant"],
    #     "measurement": "powerConsumption",
    #     'fields': {
    #         'value': decodedData["powerConsumption"],
    #     },
    #     'tags': {
    #         "sensorName": "powerConsumption",
    #     },
    # }
    # series.append(pointValues)




    # pointValues = {
    #     "time": decodedData["dataSamplingInstant"],
    #     "measurement": "luxOutput",
    #     'fields': {
    #         'value': decodedData["luxOutput"],
    #     },
    #     'tags': {
    #         "sensorName": "luxOutput",
    #     },
    # }
    # series.append(pointValues)

    # print series

    
    # client.write_points(series, time_precision='n')






client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("loraserver","password")

client.connect("10.156.14.16", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()







