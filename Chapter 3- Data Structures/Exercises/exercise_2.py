# Old G groups with nicknames

name_of_friends = [ "Chupapi" , "lancelot" , "Cousin" , "nateman" , "BAGANG!" , "Sleepyklein" , "Beatosis" , "Autistic" ]

#message to friends

message = "hello , {}! We hope u have a good day!."

# loop through the list of friends nickname 

for name_of_friends in name_of_friends:
	personalize_message = message.format(name_of_friends)
	print(personalize_message)