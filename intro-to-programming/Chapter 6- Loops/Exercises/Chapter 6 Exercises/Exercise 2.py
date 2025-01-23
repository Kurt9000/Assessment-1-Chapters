print("\n"+"Exercise 2")
while True:
    user = input("Please enter your age (or 'quit' to exit): ")

    # Check if the user wants to quit the program
    if user == 'quit':
        print("Goodbye!")
        break

    # Check if the input is a valid number (digit)
    if user.isdigit():
        age = int(user)
        
        # Check the age and determine ticket price
        if age < 3:
            print("Your ticket is free!")
        elif 3 <= age <= 12:
            print("Your ticket will costs $10.")
        else:
            print("Your ticket will costs $15.")
    else:
        print("Please enter a valid number for your age.")