#!/usr/bin/python

import requests
from bs4 import *
import sys
import os

raw_data = requests.get("http://www.worldometers.info/coronavirus").content
# getting raw data from Worldometers.info
data = BeautifulSoup(raw_data, features='lxml')
# Initialising BeatifulSoup
parsed_data = str(str(data.find('title','')).replace("<title>Coronavirus Update (Live)","")).replace(': ','').replace('Cases and ','cases\n').replace('Deaths from COVID-19 Virus Pandemic - Worldometer</title>','deaths ');

def write_temps():
	_file = open(".tmp","w+");
	_file.write(parsed_data);
	_file.close();

def get_data():
	print(parsed_data + '\r');
#############################################
try:
	if(sys.argv[1] == '--create-temps') : 
		write_temps();
		get_data();
		
	elif(sys.argv[1] == '--help') : 
		print('''Usage: covid19 [optional args]

--create-temps - creates the .tmp file with data
		''');
	elif(sys.argv[1] == '--numbers-only') : 
		print(parsed_data.replace(" cases","").replace(" deaths",""));
	
except IndexError:
	os.system("true");
	get_data();
##############################################


