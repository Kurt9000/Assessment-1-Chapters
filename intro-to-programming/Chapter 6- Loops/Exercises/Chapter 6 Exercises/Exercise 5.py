print("\n"+"Exercise 5")
sandwich_orders = ['tuna', 'pastrami', 'turkey', 'pastrami', 'ham', 'cheese', 'pastrami', 'veggie']
finished_sandwiches = []

print("Sorry, we ran out of pastrami sandwiches.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()  
    print(f"Your {current_sandwich} sandwich is ready!")
    finished_sandwiches.append(current_sandwich) 

print("\nHere are the sandwiches that were finished:")
for sandwich in finished_sandwiches:
    print(sandwich.title())
