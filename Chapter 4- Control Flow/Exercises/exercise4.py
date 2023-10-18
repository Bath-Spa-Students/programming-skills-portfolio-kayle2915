# a persons stage of life 
age = int(input("a persons age: "))

# persons stage of life
if age < 2:
    print("that person is a baby")

elif age < 4:
    print("that person is a toddler")

elif age < 13:
    print("that person is a kid")

elif age < 20:
    print("that person is a teenager")

elif age < 65:
    print("that person is an adult")

else:
    print("that person is an elder")