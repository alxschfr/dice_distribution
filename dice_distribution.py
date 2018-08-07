import random

ergebnis = {}

#input how many sides dice should have
sides = input('Wie viele Seiten soll dein Würfel haben. Gib eine Zahl zwischen 1 und 20 ein: ')

#while loop that asks the user until he gives the right input and discriminates between two possible wrong input-types
while not sides.isdigit() or int(sides) < 1 or int(sides) > 20:
    print('So einen Würfel haben wir nicht da. Such dir doch einen anderen aus!')
    print()
    sides = input('Wie viele Seiten soll dein Würfel haben. Gib eine Zahl zwischen 1 und 20 ein: ')

#input how many rolls should be performed
attempts = input('Wie oft soll der Würfel fallen? Gib eine Zahl ein: ')

#while loop that asks the user until he gives the right input and discriminates between two possible wrong input-types
while not attempts.isdigit() or int(attempts) < 1:
    print('Das funktioniert leider nicht. Gib eine positive Zahl ein!')
    print()
    attempts = input('Wie oft soll der Würfel fallen? Gib eine Zahl ein: ')

#converts input to int
sides = int(sides)
attempts = int(attempts)

#adds new dictonaire element for every side the dice will have with the associated number as dict keys
for n in range(sides):
    ergebnis[str(n + 1)] = 0

#performces as many dice rolls as the user inputs and adds 1 to the specific dict key
for roll in range(attempts):
    value = random.randint(1, sides)
    ergebnis[str(value)] += 1

#summarises users choices
print('So, dein {0!s}-seitiger Würfel wurde jetzt {0!s} Mal geworfen. Hier die Ergebnisse:'.format(sides, attempts))

#prints each dict key and value to a string
for k in ergebnis:
    print('Die Zahl {} ist {} Mal vorgekommen.'.format(k, ergebnis[k]))