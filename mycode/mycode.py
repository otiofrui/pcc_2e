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