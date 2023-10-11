# Old G groups with nicknames

name_of_friends = [ "Chupapi" , "lancelot" , "Cousin" , "nateman" , "BAGANG!" , "Sleepyklein" , "Beatosis" , "Autistic" ]

#message to friends

message = "hello , {}! I would like to invite you to dinner party that will be held at my house."

# loop through the list of friends nickname 

for name_of_friends in name_of_friends:
	personalize_message = message.format(name_of_friends)
	print(personalize_message)