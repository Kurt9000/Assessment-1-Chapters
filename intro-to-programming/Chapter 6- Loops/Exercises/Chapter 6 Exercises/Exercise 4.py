print("\n"+"Exercise 4.")
sandwich_orders = ['tuna', 'turkey', 'ham', 'cheese', 'veggie']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich) 

print("\nHere are the sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich.title())
