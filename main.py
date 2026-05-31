import random
dice_art = {
    0: ("┌─────────┐",
        "│         │",
        "│         │",
        "│         │",
        "└─────────┘"),

    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")

}

num_of_dices = int(input("How many dice? "))
total = 0
dices = [random.randint(1,6) for _ in range(num_of_dices)]

for die in range(num_of_dices):
    dices.append(random.randint(1,6))

#for die in range(num_of_dices):
#    for line in dice_art.get(dices[die]):
#        print(line)

for line in range(5):
    for die in dices:
        print(dice_art.get(die)[line], end="")
    print()

for die in dices:
    total += die

print(f"Adding all the dices give you a total of {total}")