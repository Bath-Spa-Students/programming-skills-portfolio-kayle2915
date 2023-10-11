# people invited to my dinner party
guests = ["chupapi", "lancelot", "nateman", "cousin"]

# print a message saying that only two people can come to dinner party
print("sorry, there are only 2 seat available for the dinner party")

# removing to guests for dinner party

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"sorry {removed_guest}, Due to limited sitting I can only invite two people to dinner.")

# message to people who are still invited 

for guest in guests:
    print(f"{guest}, you're still invited to dinner.")

# removing 2 from the list 

del guests[:]

# confirm guest 

print("Guest list is now empty:",guests )


