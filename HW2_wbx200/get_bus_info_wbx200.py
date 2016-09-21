from __future__ import print_function
import json
import urllib2
import os
import sys
import csv

headers = ['Latitude', 'Longitude', 'Stop Name', 'Stop Status']
writer = csv.writer(open(sys.argv[3], 'w'))
writer.writerow(headers)

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]

response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

position = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

busline = 'Bus line : ' + sys.argv[2]
numberofbuses = len(position)
#print (busline)
#print ('Number of Active Buses :', numberofbuses)
a = 0
for i in position:
    latitude = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    try:
        stopname = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    except KeyError:
        stopname = "N/A"
    try:
        status = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    except KeyError:
        status = "N/A"
a = a + 1

b = 0 
for i in position:
    row = []
    row.append(str(i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']))
    row.append(str(i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
    row.append(str(i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']))
    row.append(str(i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']))
    writer.writerow(row)
    b = b + 1
        #    print ('Bus', a, 'is at latitude', latitude, 'and longitude', longitude, #stopname, status)
