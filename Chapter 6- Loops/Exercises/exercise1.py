# Prompting the user for pizza toppings
toppings=[]

# loop

while True:
    topping = input("Enter a pizza topping (enter 'quit' to finish): ")
    if topping == 'quit':
        break
    toppings.append(topping)
    print(f"You'll add {topping} to your pizza.")

print("Finished adding toppings to your pizza.")
for topping in toppings:
    print(topping)


