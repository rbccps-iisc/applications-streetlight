import base64
import actuated_pb2

import paho.mqtt.client as mqtt
import json
import sys


# Define Variables
MQTT_HOST = "10.156.14.16"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "application/2/node/70b3d58ff0031de5/tx"



MQTT_MSG = sys.argv[1]


MQTT_USERNAME = "loraserver"
MQTT_PASSWORD = "password"

# Define on_publish event function
def on_publish(client, userdata, mid):
    print "Message Published..."

def on_connect(client, userdata, flags, rc):
    client.subscribe(MQTT_TOPIC)
    client.publish(MQTT_TOPIC, MQTT_MSG)

def on_message(client, userdata, msg):
    print(msg.topic)
    print(msg.payload) 
    client.disconnect() 

# Initiate MQTT Client
mqttc = mqtt.Client()

# Register publish callback function

mqttc.on_publish = on_publish
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

# Connect with MQTT Broker
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

# Loop forever
mqttc.loop_forever()
