from MQTTPubSub import MQTTPubSub
from google.protobuf.json_format import MessageToJson
import actuated_pb2
import sensed_pb2
import time




##############################################
#	NS Components
#############################################

def NSPub_onConnect(mqttc, obj, flags, rc):
    print("rc: "+str(rc))

def NSPub_onMessage(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

def NSPub_onPublish(mqttc, obj, mid):
    print("mid: "+str(mid))

def NSPub_onSubscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))




def NSSub_onConnect(mqttc, obj, flags, rc):
    print("rc: "+str(rc))

def NSSub_onMessage(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

def NSSub_onPublish(mqttc, obj, mid):
    print("mid: "+str(mid))

def NSSub_onSubscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))




##############################################
#	MW Components
#############################################



def MWPub_onConnect(mqttc, obj, flags, rc):
    print("rc: "+str(rc))

def MWPub_onMessage(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

def MWPub_onPublish(mqttc, obj, mid):
    print("mid: "+str(mid))

def MWPub_onSubscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))




def MWSub_onConnect(mqttc, obj, flags, rc):
    print("rc: "+str(rc))

def MWSub_onMessage(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

def MWSub_onPublish(mqttc, obj, mid):
    print("mid: "+str(mid))

def MWSub_onSubscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))





################################################


def main():

	ns_url = "m2m.eclipse.org"
	ns_port = 1883
	ns_timeout = 60
	ns_topic = "$SYS/broker/bytes/sent"

	ns = MQTTPubSub(NSSub_onMessage, NSSub_onConnect, NSSub_onPublish, NSSub_onSubscribe, ns_url, ns_port, ns_topic, ns_timeout, username = None, password = None)
	ns_rc = ns.run()



	print ("&&&&&&&&&&&&&&&&&&&&&&&&&")
	print("$$$$$$$$$$$$$$$$$$$$$$$$$")
	print ("Connecting to Middleware")

	mw_url = "10.156.14.16"
	mw_port = 1883
	mw_timeout = 60
	mw_topic = "application/2/node/70b3d58ff0031de5/rx"
	mw_username = "loraserver"
	mw_password = "password"

	mw = MQTTPubSub(MWSub_onMessage, MWSub_onConnect, MWSub_onPublish, MWSub_onSubscribe, mw_url, mw_port, mw_topic, mw_timeout, mw_username, mw_password)
	mw_rc = mw.run()
	print("mw_rc:" + str(mw_rc))

	while True:
		time.sleep(0.5)

if __name__ == "__main__":
    main()
