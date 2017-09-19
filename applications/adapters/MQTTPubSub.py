#!/usr/bin/python
# Copyright (c) 2013 Roger Light <roger@atchoo.org>
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Distribution License v1.0
# which accompanies this distribution. 
#
# The Eclipse Distribution License is available at 
#   http://www.eclipse.org/org/documents/edl-v10.php.
#
# Contributors:
#    Roger Light - initial implementation
# This example shows how you can use the MQTT client in a class.
import sys
import os
import inspect
import paho.mqtt.client as mqtt
import threading


class MQTTPubSub:
    def __init__(self, onMessage, onConnect, onPublish, onSubscribe, url, port, topic, timeout, username, password):

        self.url = url
        self.port = port
        self.timeout = timeout
        self.topic = topic

        self._mqttc = mqtt.Client(None)
        if( username):
            self.username = username
            if( password):
                self.password = password
            self._mqttc.username_pw_set(self.username,self.password)

        self._mqttc.on_message = onMessage
        self._mqttc.on_connect = onConnect
        self._mqttc.on_publish = onPublish
        self._mqttc.on_subscribe = onSubscribe
    
    def run(self):
        self._mqttc.connect(self.url, self.port, self.timeout)
        self._mqttc.subscribe(self.topic, 0)
        threading.Thread(target=self._mqttc.loop_start()).start()
        print("Thread " + self.topic + " Started")






