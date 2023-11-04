age_msg = "Enter the person's age: (Enter 'exit' when finished): "

while True:
    age = input(age_msg)
    if age.lower() == 'exit':
        break
    age = int(age)

    # Determine the ticket prices based on the person's age
    if age < 3:
        print("The tickets are free.")
    elif age < 13:
        print("The ticket is $10.")
    else:
        print("The ticket is $15.")




 
 

