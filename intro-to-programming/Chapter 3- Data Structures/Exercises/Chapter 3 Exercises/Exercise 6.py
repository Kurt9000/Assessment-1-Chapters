Inv=["Jeager", "FrazBear", "Leonardo"]
for guest in Inv:
    print(f"Honored Guest {guest} would love it if such a kind gentlemen like u come forward to dinner.")

print(f"It is unfortunate that honored guest's ({Inv[1]}) could not attend the diner.")
Inv[1]= "Ci'leora"

for guest in Inv:
    print(f"Honored Guest {guest} are still available into coming to the diner.")

print("Unfortunately, the new dinner table won't arrive in time, so I can invite only two people for dinner.")

while len(Inv) > 2:
    Bye_bye = Inv.pop()
    print(f"Sorry, {Bye_bye}, I can't invite you to dinner.")

for guest in Inv:
    print(f"Honored Guest {guest}, you are still invited to dinner.")

del Inv[:]
print("Final guest list:", Inv)
