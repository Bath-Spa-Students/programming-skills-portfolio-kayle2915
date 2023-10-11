# people invited to my dinner party
guests = ["chupapi", "lancelot", "nateman", "cousin"]

# Name of the person who can't make it and the new person to invite
busy_friend = "nateman"
new_guest = "drei"



# Replace the old guest with the new guest
if busy_friend in guests:
    index = guests.index(busy_friend)
    guests[index] = new_guest


# Print the messages for the people invited 
for guest in guests:
    print(f"hello {guest}!, you are invited to my dinner party at exactly 8 pm. Dont be late!")


