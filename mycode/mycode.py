# personal cheat sheet

the_answer=42
print(the_answer)
the_answer="fourty two"
print(the_answer)

lwrcase_text="das SOLLTE Eigentlich aLLes groß sein am Anfang oder klein.. keine Ahnung"
print(lwrcase_text.title())
print(lwrcase_text.lower())
print(lwrcase_text.upper())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)

x = 2*3
print(f"Mult: {x}")
print(f"Exp: {2**3}")

big_number=20_000_000_000
print(big_number)

x,y,z=0,0,0
print(x, y, z)

import this

print("\n ")

words=['gin','beer','mezcal','tequila','wine']
print(words[1].title())
words[1]='test'
print(words[1].upper())
words.append('zoom')
print(words[2])
words.insert(2,'webex')
print(words[2])
del words[2]
print(words)
print(sorted(words, reverse=True))
print(words)
words.sort(reverse=True)
print(words)
print(len(words))

new=[]
for word in words:
    new.append(f"{word}, auch drin")
    print(f"{word}, is great\n")

print(new)

print('de nada')

newer=list(range(1,6))
print(newer)

sqrts=[]
for value in range (2, 11, 2):
    sqrt= value ** -2
    sqrts.append(sqrt)

print(sqrts)
print(min(sqrts))

squares = [value**2 for value in range(1, 11)]
print(squares)

print(squares[:3])
print(squares[3:])

tupels = (10, 20, 30)
for tupel in tupels:
    print(tupel)

car = 'audi'
print(car == 'bmw')

age_0 = 22
age_1 = 18

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

switch_on=False
number_switch=1
ipf = range(1,11,2)
pp = range(100, 210, 10)
if switch_on is True:
    for i in ipf:
        for p in pp:
            d=p*i
            print (d-1)
elif number_switch is 0:
    print("Number Switch is off too!")
else:
    print("Switches are off!")

# Pizza Orders

print("\nPizza Orders\n")

green_peppers=5
print(green_peppers)
#ushrooms=2
#extra_cheese=1

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            if green_peppers is 0:
                print("Sorry, we are out of green peppers right now.")
            else:
             print(f"Adding {requested_topping}.")
             green_peppers = green_peppers-1
        else:
             print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

print(green_peppers)