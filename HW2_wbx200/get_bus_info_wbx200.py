from __future__ import print_function
import json
import urllib2
import os
import sys
import csv

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
    try:
        stopname = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    except KeyError:
        stopname = "N/A"
    try:
        status = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    except KeyError:
        status = "N/A"
    print ('Bus', a, 'is at latitude', latitude, 'and longitude', longitude, stopname, status)
    a = a + 1

outfile_path='/home/CUSP/wbx200/' + sys.argv[2] +'.csv'
writer = csv.writer(open(outfile_path, 'w'))
headers = ['Latitude', 'Longitude', 'Stop Name', 'Stop Status']
writer.writerow(headers)

