# movie theater ticket price

age = ("enter the persons age: ")
age +=("enter 'exit' once finish: ")

while True:
    person = input(age)
    if person == 'exit':
        break
    person = int(person)
  
# determining the ticket prices base on persons age

    if person < 3:
        print("the tickets are free")

    elif person < 13:
        print("the ticket is 10$")

    else:
        print("the ticket is 15$")




 
 

