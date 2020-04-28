## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- please
- send
- please yes
- yes please
- yes. Please
- yes. please

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- search for restaurants
- find me a restaurant
- list down restaurants
- show me some restaurants
- find a lunch place
- search for a fine dine place
- which restaurant to go to
- a food place nearby
- where will i find food
- looking out for some good restaurants
- I am hungry. Looking out for some good restaurants
- I am hungry. Looking for some good restaurants
- Im hungry. Looking out for some good restaurants
- find me some good restaurants

## intent:location_select
- find a restaurant in [delhi](location)
- show me restaurant in [kolkata](location)
- find a restaurant in [chennai](location)
- [Delhi](location:delhi)
- in [Chennai](location:chennai)
- in [mumbai](location)
- please find me a restaurant in [ahmedabad](location)
- in [Gurgaon](location)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- anywhere in the [west](location)
- Please find me a restaurant in [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in the [centre](location)
- [delhi](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- find restaurants in [delhi](location)
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- in [kanpur](location)
- find a restaurant in [lucknow](location)
- in [surat](location)
- find a [mexican](cuisine) restaurant in [kolkata](location)
- [allahabad](place)
- find a restaurant in [allahabad](location)
- can you suggest some good restaurants in [kolkata](location)
- [Bangalore](location)
- find some restaurants in [pune](location)
- [kolkata](location)
- [Kolkata](location:kolkata)
- Can you suggest some good restaurants in [Rishikesh](location:rishikesh)
- okay shome some in [allahabad](location)
- [hyderabad](location)
- Can you suggest some restaurants in [kolkata](location)
- looking for good [chinese](cuisine) restaurant in [chandigarh](location)
- show me in [surat](location)
- in [mubai](location)
- In [Mumbai](location:mumbai)
- find a restaurant in [chandigarh](location)
- In [surat](location)
- in [Ahmedabad](location:ahmedabad)

## intent:budget_select
- in [<300](price:1)
- [>700](price:3)
- show me [mid](price:2) range results
- [expensive](price:3) ones
- show me [cheap](price:1) places
- i am looking for [cheap](price:1) places
- [<300](price:1)
- [> 700](price:3)
- [400](price:2)
- [cheap](price:1)
- [500](price:2)
- [600](price:2)
- [less than 300](price:1)

## intent:cuisine_select
- [Italian](cuisine)
- [Chinese](cuisine)
- I am looking for [Thai](cuisine:thai) food
- show me [chinese](cuisine) restaurants
- [Mexican](cuisine:mexican)
- [North Indian](cuisine:north indian)
- [chinese](cuisine)
- can you find me a [chinese](cuisine) restaurant
- find a [mexican](cuisine) restaurant
- I will prefer [chinese](cuisine)
- [north indian](cuisine)
- I like [american](cuisine)
- just [american](cuisine)
- [italian](cuisine)
- I will prefer [mexican](cuisine)
- I wil prefer [American](cuisine:american)
- [american](cuisine)
- find a [mexican](cuisine) restaurant

## intent:send_mail
- send at [pratishgupta91@gmail.com](email)
- yes please send it to [pratishgupta91@gmail.com](email)
- yes. Please send it to [xyz@sth.edu](email)
- yes. Please send to [pratishgupta91@gmail.com](email)
- [pratishgupta91@gmail.com](email)
- yes. Please send it to [pratishgupta91@gmail.com](email)
- please send to [abc@gmal.com](email)
- yes. send at [prkum@microsoft.com](value)

## intent:dont_send_mail
- no
- dont
- nope
- dont send
- don't send
- no
- no I am okay
- I am good
- no. thanks
- no
- no thanks

## synonym:1
- <300
- cheap
- less than 300

## synonym:2
- mid
- 400
- 500
- 600

## synonym:3
- >700
- expensive
- > 700

## synonym:Delhi
- New Delhi
- dilli

## synonym:american
- American

## synonym:bangalore
- Bengaluru

## synonym:cheap
- pocket friendly

## synonym:chennai
- Chennai
- madras

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:delhi
- Delhi

## synonym:expensive
- luxary
- fine dine

## synonym:italian
- Italian
- italy
- itlian

## synonym:kolkata
- Kolkata
- Calcuta
- calcutta
- kolkatta

## synonym:mexican
- Mexican

## synonym:mid
- moderate
- middle

## synonym:mumbai
- Mumbai
- bambai
- bombay

## synonym:north indian
- North Indian
- northy
- northindian

## synonym:thai
- Thai

## synonym:vegetarian
- veggie
- vegg
- veggies

## regex:greet
- hey[^\s]*

