from constraint import Problem, AllDifferentConstraint

H = [1, 2, 3, 4, 5]
C = ['red', 'green', 'blue', 'white', 'yellow']
P = ['German', 'Norwegian', 'Brit', 'Swede', 'Dane']
D = ['coffee', 'tea', 'milk', 'beer', 'water']
S = ['PallMall', 'Dunhill', 'Blend', 'BlueMaster', 'Prince']
T = ['dog', 'bird', 'cat', 'horse', 'zebra']

p = Problem()

for g in C + P + D + S + T:
    p.addVariable(g, H)

for category in [C, P, D, S, T]:
    p.addConstraint(AllDifferentConstraint(), category)

p.addConstraint(lambda brit, red: brit == red, ('Brit', 'red'))
p.addConstraint(lambda swede, dog: swede == dog, ('Swede', 'dog'))
p.addConstraint(lambda dane, tea: dane == tea, ('Dane', 'tea'))
p.addConstraint(lambda green, coffee: green == coffee, ('green', 'coffee'))
p.addConstraint(lambda green, white: green == white - 1, ('green', 'white'))
p.addConstraint(lambda pall, bird: pall == bird, ('PallMall', 'bird'))
p.addConstraint(lambda yellow, dunhill: yellow == dunhill, ('yellow', 'Dunhill'))

sol = p.getSolution()

for h in H:
    print(f"House {h}: ", end="")
    for category in C + P + D + S + T:
        if sol[category] == h:
            print(category, end=", ")
    print()

zebra_owner = ""
for person in P:
    if sol[person] == sol['zebra']:
        zebra_owner = person
        break

print("\nZebra owner:", zebra_owner)

water_drinker = ""
for person in P:
    if sol[person] == sol['water']:
        water_drinker = person
        break

print("Water drinker:", water_drinker)
