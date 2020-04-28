
## interactive_story_1
* greet
    - utter_greet
* location_select{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_valid_location
    - slot{"location": "rishikesh"}
* location_select{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - utter_ask_cuisine
* cuisine_select{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* budget_select{"price": "1"}
    - slot{"price": "1"}
    - action_search_restaurants
    - slot{"location": "allahabad"}
    - utter_ask_send_mail
* send_mail
    - action_send_mail
    - utter_sent
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location_select{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_valid_location
    - utter_ask_cuisine
* cuisine_select{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* budget_select{"price": "3"}
    - slot{"price": "3"}
    - action_search_restaurants
    - utter_ask_send_mail
* send_mail{"email": "pratishgupta91@gmail.com"}
    - slot{"email": "pratishgupta91@gmail.com"}
    - action_send_mail
    - utter_sent
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* location_select{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_valid_location
    - utter_ask_cuisine
* cuisine_select{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* budget_select{"price": "1"}
    - slot{"price": "1"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_send_mail
* affirm
    - utter_ask_mail_id
* send_mail{"email": "pratishgupta91@gmail.com"}
    - slot{"email": "pratishgupta91@gmail.com"}
    - action_send_mail
    - slot{"location": "kolkata"}
    - utter_sent
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location_select{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_valid_location
    - utter_ask_cuisine
* cuisine_select{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* budget_select{"price": "1"}
    - slot{"price": "1"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_send_mail
* affirm
    - utter_ask_mail_id
* send_mail{"email": "pratishgupta91@gmail.com"}
    - slot{"email": "pratishgupta91@gmail.com"}
    - action_send_mail
    - slot{"location": "mumbai"}
    - utter_sent
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* location_select{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_valid_location
    - utter_ask_price
* budget_select{"price": "1"}
    - slot{"price": "1"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_ask_send_mail
* dont_send_mail
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location_select{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_valid_location
    - utter_ask_cuisine
* cuisine_select{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* budget_select{"price": "2"}
    - slot{"price": "2"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_send_mail
* send_mail{"email": "pratishgupta91@gmail.com"}
    - slot{"email": "pratishgupta91@gmail.com"}
    - action_send_mail
    - slot{"location": "kolkata"}
    - utter_sent
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* location_select{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_valid_location
    - slot{"location": null}
* location_select{"location": "surat"}
    - slot{"location": "surat"}
    - utter_ask_cuisine
* cuisine{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* budget_select{"price": "2"}
    - slot{"price": "2"}
    - action_search_restaurants
    - slot{"location": "surat"}
    - utter_ask_send_mail
* send_mail{"email": "abc@gmal.com"}
    - slot{"email": "abc@gmal.com"}
    - action_send_mail
    - utter_sent
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* location_select{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_valid_location
    - utter_ask_cuisine
* cuisine{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* price{"price": "3"}
    - slot{"price": "3"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_send_mail
* affirm
    - utter_ask_mail_id
* send_mail{"email": "pratishgupta91@gmail.com"}
    - slot{"email": "pratishgupta91@gmail.com"}
    - action_send_mail
    - slot{"location": "kolkata"}
    - utter_sent
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location_select{"location": "mubai"}
    - slot{"location": "mubai"}
    - action_valid_location
    - slot{"location": null}
* location_select{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* cuisine{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* price{"price": "3"}
    - slot{"price": "3"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_send_mail
* affirm
    - utter_ask_mail_id
* send_mail{"email": "pratishgupta91@gmail.com"}
    - slot{"email": "pratishgupta91@gmail.com"}
    - action_send_mail
    - slot{"location": "mumbai"}
    - utter_sent
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* location_select{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - action_valid_location
    - utter_ask_cuisine
* cuisine{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_price
* price{"price": "3"}
    - slot{"price": "3"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_ask_send_mail
* dont_send_mail
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location_select{"location": "surat"}
    - slot{"location": "surat"}
    - action_valid_location
    - utter_ask_cuisine
* cuisine{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* price{"price": "1"}
    - slot{"price": "1"}
    - action_search_restaurants
    - slot{"location": "surat"}
    - utter_ask_send_mail
* dont_send_mail
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* cuisine_select{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* location_select{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - action_valid_location
    - utter_ask_price
* price{"price": "2"}
    - slot{"price": "2"}
    - action_search_restaurants
    - slot{"location": "ahmedabad"}
    - utter_ask_send_mail
* send_mail{"value": "prkum@microsoft.com"}
    - utter_sent
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* cuisine_select{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* location_select{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - action_valid_location
    - slot{"location": null}
* location_select{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_price
* price{"price": "2"}
    - slot{"price": "2"}
    - action_search_restaurants
    - slot{"location": "ahmedabad"}
    - utter_ask_send_mail
* send_mail{"value": "prkum@microsoft.com"}
    - utter_sent
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* location_select{"cuisine": "chinese", "location": "chandigrh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigrh"}
    - action_valid_location
    - slot{"location": null}
* location_select{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_price
* budget_select{"price": "1"}
    - slot{"price": "1"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_ask_send_mail
* dont_send_mail
    - utter_goodbye
    - action_restart