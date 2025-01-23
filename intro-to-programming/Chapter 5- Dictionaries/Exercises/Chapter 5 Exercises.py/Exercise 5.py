print("\n"+"Exercise 5")
pet1 = {'kind': 'dog', 'owner': 'Jeliopina'}
pet2 = {'kind': 'cat', 'owner': 'Aricy'}
pet3 = {'kind': 'duck', 'owner': 'Dejio'}
pet4 = {'kind': 'cockroach', 'owner': 'Eric'}

pets = [pet1, pet2, pet3, pet4]

for pet in pets:
    print(f"The pet is a {pet['kind']} and the owner's name is {pet['owner']}.")
