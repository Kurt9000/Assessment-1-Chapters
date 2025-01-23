print("\n"+"Exercise 1")
prompt = "\nWhat pizza topping would you like?"
prompt += "\nEnter 'quit' once you are finished: "

while True:
    topping = input(prompt)
    if topping == 'quit':
         break
    else:
         print(f"Sure! I'll start adding {topping} to your pizza.")
