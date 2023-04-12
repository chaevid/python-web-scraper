age = int(input("your age ?"))

if age < 18:
    print("No drink")
elif age >= 18 & age <= 35:
    print("You drink beer!")
elif age == 60 | age == 70:
    print("Birthday party!")
else:
    print("Go ahead")
