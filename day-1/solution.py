import os

input = open(os.path.abspath("day-1/input.txt"), 'r')
modules = input.read().split('\n')

total_mass = 0

for mass in modules:
    mass = int(mass)
    required_fuel = mass // 3 - 2
    total_mass += required_fuel
    print(required_fuel)

    while required_fuel // 3 - 2 >= 0:
        required_fuel = required_fuel // 3 - 2
        total_mass += required_fuel

print('total:',total_mass)