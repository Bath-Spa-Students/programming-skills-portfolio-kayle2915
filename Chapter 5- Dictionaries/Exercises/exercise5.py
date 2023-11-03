# pets 

pets = {
    'dog' : 'kayle',
    'cat' : 'audrey',
    'lion' : 'drey',
    'bird' : 'francis',
    'fish' : 'keefe'
}

for pets, owner in pets.items():
    print(f"these {pets} are own by {owner}")

# information about the animals.
pets = input("Enter a pet: ")
print("pets information: ")



if pets == "dog":
    print("""this animal is a mans bestfriend.\nDogs are the most popular and oldest pets in the world.""")

elif pets == "cats":
    print("""cats is a quiet friend.\ncat species that among others include the lion,tiger,cheetah""")

elif pets == "lion":
    print("""lions is the king of a jungle.\nLions are the second largest cats in the world.""")

elif pets == "fish":
    print("""fish lives in a bowl with water.\nFish are aquatic animals.""")

elif pets == "bird":
    print("""bird can fly.\nBirds are vertebrate animals adapted for flight.""")

else:
    print("invalid output")

