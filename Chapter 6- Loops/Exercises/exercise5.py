# list of sandwiches
sandwich_orders = ["pastrami", "tuna", "steak"]
finished_sandwiches = []

# printing we've run out of pastrami
while 'pastrami' in sandwich_orders:
     print("I'm sorry, we're all out of pastrami today.")
     sandwich_orders.remove("pastrami")

# loops
while True:
    order = input("Enter your sandwich (type 'exit' to finish): ")
    if order.lower() == 'exit':
        break
    elif order.lower() not in [sandwich.lower() for sandwich in sandwich_orders]:
        print("Sorry, we don't have that sandwich.")
        continue
    print(f"I made your {order} sandwich.")
    finished_sandwiches.append(order)

# printing the finished sandwiches
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
