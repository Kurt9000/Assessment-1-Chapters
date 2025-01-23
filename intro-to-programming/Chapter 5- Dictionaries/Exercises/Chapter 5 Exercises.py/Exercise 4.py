print("\n"+"Exercise 4")
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
    'mississippi': 'usa',
    'ganges': 'india'
}

for river, country in rivers.items():
    print(f"The {river.title()} stream runs through {country.title()}.")

print("\nRivers:")
for river in rivers.keys():
    print(river.title())

print("\nCountries:")
for country in rivers.values():
    print(country.title())
