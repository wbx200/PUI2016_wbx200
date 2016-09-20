from __future__ import print_function
import json
import urllib2
import os
import sys

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]

response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

position = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

busline = 'Bus line : ' + sys.argv[2]
numberofbuses = len(position)
print (busline)
print ('Number of Active Buses :', numberofbuses)
a = 0
for i in position:
    latitude = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print ('Bus', a, 'is at latitude', latitude, 'and longitude', longitude)
    a = a + 1
