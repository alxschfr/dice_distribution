#!/usr/bin/env python3

import random

# fills the count_dict with the occuring numbers
def fill_count_dict(sides):
    for n in range(sides):
        count1[str(n + 1)] = 0
        count2[str(n + 1)] = 0

# performes as many dice rolls as the user inputs, appends the values for count and result for each dice as well as the added result to different lists and increments the count-dict-value by 1
def roll_the_dice(attempts, sides):
    for roll in range(attempts):
        dice1 = random.randint(1, sides)
        dice2 = random.randint(1, sides)
        dice_result1.append(dice1)
        dice_result2.append(dice2)
        dice_addition.append(dice1 + dice2)
        count1[str(dice1)] += 1
        count2[str(dice2)] += 1

# fills the dice_addition_dict with the occuring numbers as key values and increments by one for every occursion
def fill_addition_count_dict(dice_add):
    for n in dice_add:
       dice_addition_result[str(n)] = 0
    for n in dice_add:
       dice_addition_result[str(n)] += 1

# prints each dict key and value to a string
def print_count_results(count):
    for k in count:
        print('Die Zahl {} ist {} Mal vorgekommen.'.format(k, count[k]))

count1 = {}
count2 = {}
dice_result1 = []
dice_result2 = []
dice_addition = []
dice_addition_result = {}

# input how many sides dices should have and check if proper input
sides = input('Wie viele Seiten sollen deine Würfel haben. Gib eine Zahl zwischen 1 und 20 ein: ')
while not sides.isdigit() or int(sides) < 1 or int(sides) > 20:
    print('Solche Würfel haben wir nicht da. Such dir doch andere aus!')
    print()
    sides = input('Wie viele Seiten sollen deine Würfel haben. Gib eine Zahl zwischen 1 und 20 ein: ')
sides = int(sides)

# input how many rolls should be performed and check if proper input
attempts = input('Wie oft sollen deine Würfel fallen? Gib eine Zahl ein: ')
while not attempts.isdigit() or int(attempts) < 1:
    print('Das funktioniert leider nicht. Gib eine positive Zahl ein!')
    print()
    attempts = input('Wie oft sollen die Würfel fallen? Gib eine Zahl ein: ')
attempts = int(attempts)

# fills the count dict
fill_count_dict(sides)

# rolls the dice
roll_the_dice(attempts, sides)

# summarises users choices and results
print()
print('So, deine {}-seitigen Würfel wurden jetzt {} Mal geworfen. Hier die Ergebnisse:'.format(sides, attempts))
print()
print('Das Ergebnis des ersten Würfels ist:')
print_count_results(count1)
print()
print('Das Ergebnis des zweiten Würfels ist:')
print_count_results(count2)
print()
print('Würfel 1: ' + str(dice_result1))
print('Würfel 2: ' + str(dice_result2))
print('Würfel 1 + 2: ' + str(dice_addition))
dice_addition.sort()
fill_addition_count_dict(dice_addition)
print('Die Verteilung der addierten Werte: ' + str(dice_addition_result))
