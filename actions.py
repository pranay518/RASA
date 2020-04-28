from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy as zo
import json
import smtplib 

def get_is_valid_city(city):
		valid_cities = """Bangalore, Chennai, Delhi, Hyderabad, Kolkata, Mumbai, Ahmedabad,
		Pune,Agra, Ajmer, Aligarh, Amravati, Amritsar, Asansol, Aurangabad,
		Bareilly, Belgaum, Bhavnagar, Bhiwandi, Bhopal, Bhubaneswar, Bikaner, 
		Bilaspur, Bokaro Steel City, Chandigarh, Coimbatore, Nagpur, Cuttack, 
		Dehradun, Dhanbad, Bhilai, Durgapur, Erode, Faridabad, Firozabad, 
		Ghaziabad, Gorakhpur, Gulbarga, Guntur, Gwalior, Gurgaon, Guwahati, 
		Hamirpur, Hubli–Dharwad, Indore, Jabalpur, Jaipur, 
		Jalandhar, Jammu, Jamnagar, Jamshedpur, Jhansi, Jodhpur, Kakinada, Kannur, 
		Kanpur, Kochi, Kolhapur, Kollam, Kozhikode, Kurnool, Ludhiana, Lucknow, Madurai, 
		Malappuram, Mathura, Goa, Mangalore, Meerut, Moradabad, Mysore, Nanded, Nashik, 
		Nellore, Noida, Patna, Pondicherry, Purulia Prayagraj, Raipur, Rajkot, 
		Rajahmundry, Ranchi, Rourkela, Salem, Sangli, Shimla, Siliguri, Solapur, Srinagar, 
		Thiruvananthapuram, Thrissur, Tiruchirappalli, Tiruppur, Ujjain, Bijapur, Vadodara, 
		Varanasi, Vasai-Virar City, Vijayawada, Vellore, Warangal, Surat, Visakhapatnam"""
		
		cities_list = valid_cities.split(",")
		cities_list = [city.strip() for city in cities_list]
		cities_list = [city.lower() for city in cities_list]
		
		city = city.lower()
		if city in cities_list:
			return True
		return False

def filter_budget(restaurants, budget):
	res = []
	for restaurant in restaurants:
		if (budget == 1) & (restaurant[3] < 300):
			res.append(restaurant)
		elif (budget == 2) & (restaurant[3] >= 300) & (restaurant[3] <= 700):
			res.append(restaurant)
		elif (budget == 3) & (restaurant[3] > 700):
			res.append(restaurant)
	return res
		
def get_location(location, zomato):
	location = location.lower()
	location_detail=zomato.get_location(location, 1)
	d1 = json.loads(location_detail)
	lat = d1["location_suggestions"][0]["latitude"]
	long = d1["location_suggestions"][0]["longitude"]
	print (lat)
	print(long)
	return (lat, long)

def get_cuisine(cuisine): 
	cuisine = cuisine.lower()
	cuisines_dict={'american':1,'chinese':25,'mexican':73,'italian':55,'north indian':50,'south indian':85}
	return (cuisines_dict.get(cuisine))

def get_restaurants(location, cuisine, zomato):
	results = zomato.restaurant_search("", location[0], location[1], cuisine, 5000)
	return results

def search(loc, cuisine, budget, count):
	config={ "user_key":"b0e432423bfbb0e4d344dab8e18f6137"}
	zomato = zo.initialize_app(config)
	
	response = ""
	
	if get_is_valid_city(loc) == False:
		response = "We do not operate in that area yet"
	else:
		location = get_location(loc, zomato)
		cuisine = str(get_cuisine(cuisine))
		restaurants = get_restaurants(location, cuisine, zomato)
		
		json_response = json.loads(restaurants)
		if json_response['results_found'] == 0:
			response = "no results found"
		else:
			res = []
			for restaurant in json_response["restaurants"]:
				res.append(tuple((restaurant['restaurant']['name'],
							restaurant['restaurant']['location']['address'],
							restaurant['restaurant']['user_rating']['aggregate_rating'],
							int(restaurant['restaurant']['average_cost_for_two']))))
				
			res = filter_budget(res, budget)
			res = sorted(res, key = lambda tup: tup[2], reverse=True)
			
			for result in res:
				if count >= 0:
					response += result[0] + " in " + result[1] + " has been rated " + result[2] + '\n'
					count -= 1
				else:
					break
	return response

def send_mail(mail, message):
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	s.starttls() 
	s.login("pratchat.upgrad@gmail.com", "vatayan123") 
	s.sendmail("pratchat.upgrad@gmail.com", mail, message) 
	s.quit()

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
	
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		price = int(price)
		response = search(loc, cuisine, price, 5)
		
		dispatcher.utter_message("Showing you top rated restaurants:\n"+response)
		return [SlotSet('location',loc)]	

class SendMail(Action):
	def name(self):
		return 'action_send_mail'
	
	def run(self, dispatcher, tracker, domain):

		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		email = tracker.get_slot('email')
		price = int(price)
		response = search(loc, cuisine, price, 10)
		send_mail(email, response);
		return [SlotSet('location',loc)]

class ValidLocation(Action):
	def name(self):
		return 'action_valid_location'
	
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		is_valid = get_is_valid_city(loc)
		if is_valid == False:
			dispatcher.utter_message("Sorry, we don’t operate in this city. Can you please specify some other location")
			return [SlotSet('location',None)]
