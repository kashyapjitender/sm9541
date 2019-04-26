
#firstly ensure that the sensor sm9541 library is installled in the pi 
#also make sure your raspberry pi i2c interface is enable ,if not :enable it from configuration settings
#install smbus library for the sensor from command "apt-get install python-smbus" and update it with 'apt-get update'
import os 
import time #for time delay
import requests #for sending data to cloud
from SM9541 import *
sensor = SM9541()
def read_data():
	values = sensor.read_all()
	if values is not None:
		print(('Pressure = {0:0.2f} cmH2O'.format(values[1]))) #f used to get floating point values of pressure
		print(('Temp     = {0:0.2f} deg C'.format(values[2])))
		time.sleep(1)
	else:
		print('fail to get reading from sensor')
		time.sleep(1)
		payload={'pressure':values[1],'other':values[2]}
		return payload
######################
while True: 
	try:
		r= requests.post('http://things.ubidots.com/api/v1.6/devices/raspberry/?token=******insert your token key here********',data=read_data())
		print('posting data to ubidots cloud')
		print(read_data())
	except:
		print"check sensor connection to pi"