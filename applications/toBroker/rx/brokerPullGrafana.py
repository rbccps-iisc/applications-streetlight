#!/usr/bin/env python


import sys
import json
import urllib2

from influxdb import InfluxDBClient







def callback(ch, method, properties, body):
    # print(" [x] %r:%r" % (method.routing_key, body))
    print method.routing_key
    decodedData = json.loads(body)

    series = []

    # if("citizendIssue" in method.routing_key):


    #         pointValues = {
    #             "time": (decodedData['bt']*1000),
    #             "measurement": decodedData['e']['n'],
    #             'fields': {
    #                 'value': decodedData['e']['v'],
    #             },
    #             'tags': {
    #                 "geohash":  decodedData['e']['g'],
    #             },
    #         }
    #         series.append(pointValues)


    # else:



# {

#   "dataSamplingInstant":"2017-06-06T16:05:45+05:30"
#   "caseTemperature": 33,
#   "powerConsumption": 145,
#   "luxOutput":15
#   "ambientLux": 10,

#   "targetPowerState": "ON",
#   "targetBrightnessLevel":"70"
#   "targetControlPolicy": "AUTO_TIMER",
#   "targetAutoTimerParams": { "targetOnTime": 343434, "targetOffTime": 606400},
#   "targetAutoLuxParams": { "targetOnLux":5, "targetOffLux":10}
# }




    
    pointValues = {
        "time": decodedData["dataSamplingInstant"],
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
        "time": decodedData["dataSamplingInstant"],
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
        "time": decodedData["dataSamplingInstant"],
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

    
    client.write_points(series, time_precision='n')


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()






