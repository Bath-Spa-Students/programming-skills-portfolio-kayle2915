# list of sandwiches

sandwich_orders = ["pastrami", "tuna", "steak"]
finished_sandwiches = []

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

# print the finished sandwich
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)




