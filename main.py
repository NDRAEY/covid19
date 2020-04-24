import requests
from bs4 import * 

raw_data = requests.get("http://www.worldometers.info/coronavirus").content
# getting raw data from Worldometers.info
data = BeautifulSoup(raw_data, features='lxml')
# Initialising BeatifulSoup
parsed_data = str(str(data.find('title','')).replace("<title>Coronavirus Update (Live)","")).replace(': ','').replace('Cases and ','\n').replace('Deaths from COVID-19 Virus Pandemic - Worldometer</title>','')
print(parsed_data)

