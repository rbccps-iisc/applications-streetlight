
import paho.mqtt.client as mqtt
import json

# Define Variables
MIDDLEWARE_MQTT_HOST = "10.156.14.6"
MIDDLEWARE_MQTT_PORT = 2333
MIDDLEWARE_MQTT_KEEPALIVE_INTERVAL = 45
MIDDLEWARE_MQTT_TOPIC = "70b3d58ff0031de5_update"




configuration = {}




MIDDLEWARE_MQTT_MSG = ""


MIDDLEWARE_MQTT_USERNAME = "rbccps"
MIDDLEWARE_MQTT_PASSWORD = "rbccps@123"




print("1. Manual Control")
print("2. Auto Lux")
print("3. Auto Timer")

mode = int(raw_input())

if ( mode == 1):
	configuration["ManualControlParams"] = {}
	configuration["configurationMode"] = "ManualControl"
	configuration["ManualControlParams"]["targetBrightnessLevel"] = int(raw_input('Enter Led Brightness     '))
	MIDDLEWARE_MQTT_MSG = json.dumps(configuration)

if ( mode == 2):

	configuration["AutoLuxParams"] = {}
	configuration["configurationMode"] = "AutoLux"
	configuration["AutoLuxParams"]["targetOnLux"] =  int(raw_input('Enter On Lux     '))
	configuration["AutoLuxParams"]["targetOffLux"] = int(raw_input('Enter Off Lux     '))
	MIDDLEWARE_MQTT_MSG = json.dumps(configuration)

if ( mode == 3):
	configuration["AutoTimerParams"] = {}
	configuration["configurationMode"] = "AutoTimer"
	configuration["AutoTimerParams"]["targetOnTime"] = int(raw_input('Enter minutes  from now to turn on'))*60*1000
	configuration["AutoTimerParams"]["targetOffTime"] = int(raw_input('Enter minutes from now to turn off'))*60*1000
	MIDDLEWARE_MQTT_MSG = json.dumps(configuration)





# Define on_publish event function
def on_publish(client, userdata, mid):
    print "Message Published..."

def on_connect(client, userdata, flags, rc):
    
    client.publish(MIDDLEWARE_MQTT_TOPIC, MIDDLEWARE_MQTT_MSG)



def on_message(client, userdata, msg):
    print(msg.topic)
    print(msg.payload) 
    client.disconnect() 






# Initiate MQTT Client
middleware_mqttc = mqtt.Client()

# Register publish callback function

middleware_mqttc.on_publish = on_publish
middleware_mqttc.on_connect = on_connect
middleware_mqttc.on_message = on_message
middleware_mqttc.username_pw_set(MIDDLEWARE_MQTT_USERNAME, MIDDLEWARE_MQTT_PASSWORD)

# Connect with MQTT Broker
middleware_mqttc.connect(MIDDLEWARE_MQTT_HOST, MIDDLEWARE_MQTT_PORT, MIDDLEWARE_MQTT_KEEPALIVE_INTERVAL)

# Loop forever
middleware_mqttc.loop_forever()








	# NS_MQTT_MSG = json.dumps(data)

	# NS_MQTT_USERNAME = "loraserver"
	# NS_MQTT_PASSWORD = "password"
