import json
import requests


#App id as signed up from openweathermap.org
APPID = '780ebeaf90ee70836c71fc164346ad42'


def main():
	
	while (True):
    	#format of url when zipcode is given
		def get_forecasturl_zipcode(zipcode):
    			url = 'http://api.openweathermap.org/data/2.5/forecast?zip=%s&appid=%s' 
    			return  url


		#format of url when city is given
		def get_forecasturl_city(city):
    			url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&appid=%s' 
    			return url




		url_1 = 'http://api.openweathermap.org/data/2.5/forecast?zip='



		url_2 = 'http://api.openweathermap.org/data/2.5/forecast?q='

		user_input = input('Enter zip code or city: ')

		if type(user_input) == int :
			new_url = url_1 + user_input + '&appid=' + APPID
		else:
			new_url = url_2 + user_input + '&appid=' + APPID
		
		response = requests.get(new_url)


        #Check whether the connection was established
	try:
		response.raise_for_status()
		print('Connection was successful')
	except:
		print('Connection was not succesful')
		#perhaps add continue back here

	weathers = json.loads(response.text)['list']
	
	#Display the weather informationi to the user
	print('Weather today is ' + weathers[0]['weather'][0]['main'])
	print('Weather tomorrow is ' + weathers[1]['weather'][0]['main'])

if __name__ == "__main__":
	main()
