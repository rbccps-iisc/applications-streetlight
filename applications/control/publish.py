import base64
import paho.mqtt.client as mqtt
import json

# Define Variables
MQTT_HOST = "10.156.14.6"
MQTT_PORT = 2333
MQTT_KEEPALIVE_INTERVAL = 60
MQTT_TOPIC = "70b3d58ff0031de5_update"


print("1. Manual Control")
print("2. Auto Lux")
print("3. Auto Timer")

mode = int(raw_input())

command = {}


if ( mode == 1):
    command["ManualControlParams"] = {}
    command["ManualControlParams"]["targetBrightnessLevel"] = int(raw_input('Enter Led Brightness     '))

if ( mode == 2):
    command["AutoLuxParams"] = {}
    command["AutoLuxParams"]["targetOnLux"] =  int(raw_input('Enter the On threshold'))
    command["AutoLuxParams"]["targetOffLux"] =  int(raw_input('Enter the Off threshold'))

if ( mode == 3):
    command["AutoTimerParams"] = {}
    command["AutoTimerParams"]["targetOnTime"] = int(raw_input('Enter minutes  from now to turn on'))*60*1000
    command["AutoTimerParams"]["targetOffTime"] = int(raw_input('Enter minutes from now to turn off'))*60*1000



MQTT_MSG = json.dumps(command)


MQTT_USERNAME = "admin"
MQTT_PASSWORD = "admin@123"

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
