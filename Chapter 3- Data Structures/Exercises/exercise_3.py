# mode of transportation

mode_of_transportation = {"Airbus" , "boeing" , "bombardie" , "beechcraft" , "cessna" , "assault"}


# message 


message = "I want to use {} to travel around the world"

#stored brand of transportation

for mode_of_transportation in mode_of_transportation:

	personalize_message = message.format(mode_of_transportation)

	print(personalize_message)