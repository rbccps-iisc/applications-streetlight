import base64
import actuated_pb2

import paho.mqtt.client as mqtt
import json

import thread
import os


# Define Variables
MIDDLEWARE_MQTT_HOST = "10.156.14.6"
MIDDLEWARE_MQTT_PORT = 2333
MIDDLEWARE_MQTT_KEEPALIVE_INTERVAL = 45
MIDDLEWARE_MQTT_TOPIC = "70b3d58ff0031de5_update"



configuration = actuated_pb2.targetConfigurations()


midllewareJson = {}
middlewareJsonString = ""




MIDDLEWARE_MQTT_USERNAME = "rbccps"
MIDDLEWARE_MQTT_PASSWORD = "rbccps@123"







def on_connect(client, userdata, flags, rc):
    client.subscribe(MIDDLEWARE_MQTT_TOPIC)
    #client.publish(MIDDLEWARE_MQTT_TOPIC, MIDDLEWARE_MQTT_MSG)



def on_message(client, userdata, msg):
    print(msg.topic)
    
     


    middlewareJson = json.loads(msg.payload)
    

    if ( middlewareJson["configurationMode"] == "ManualControl"):
	configuration.ManualControlParams.targetBrightnessLevel = middlewareJson["ManualControlParams"]["targetBrightnessLevel"]

	if ( middlewareJson["configurationMode"] == "AutoLux"):
		configuration.AutoLuxParams.targetOnLux =  middlewareJson["AutoLuxParams"]["targetOnLux"]
		configuration.AutoLuxParams.targetOffLux = middlewareJson["AutoLuxParams"]["targetOffLux"]

	if ( middlewareJson["configurationMode"] == "AutoTimer" ):
		configuration.AutoTimerParams.targetOnTime = middlewareJson["AutoTimerParams"]["targetOnTime"]*60*1000
		configuration.AutoTimerParams.targetOffTime = middlewareJson["AutoTimerParams"]["targetOffTime"]*60*1000


	data = {}
	data['reference'] = 'a'
	data['confirmed'] = False
	data['fport'] = 1
	data['data'] = base64.b64encode(configuration.SerializeToString())

	dataString = json.dumps(data)
	print dataString
	os.system("python publishToNs.py " + dataString )
	






# Initiate MQTT Client
middleware_mqttc = mqtt.Client()

# Register publish callback function

middleware_mqttc.on_connect = on_connect
middleware_mqttc.on_message = on_message
middleware_mqttc.username_pw_set(MIDDLEWARE_MQTT_USERNAME, MIDDLEWARE_MQTT_PASSWORD)


# Connect with MQTT Broker


# Connect with MQTT Broker
middleware_mqttc.connect(MIDDLEWARE_MQTT_HOST, MIDDLEWARE_MQTT_PORT, MIDDLEWARE_MQTT_KEEPALIVE_INTERVAL)

# Loop forever
middleware_mqttc.loop_forever()











	# NS_MQTT_MSG = json.dumps(data)

	# NS_MQTT_USERNAME = "loraserver"
	# NS_MQTT_PASSWORD = "password"
