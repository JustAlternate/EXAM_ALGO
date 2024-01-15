text = 'Hello'
word = 'le monde'
if text == 'Bonjour':
    word = 0o7  # chiffre 0 (z ́ero), lettre 'o' et chiffre 7 (sept)
    text += ' ' + word
print(text)

print(f'Dissection de la chaîne de caractères {repr(text)} :')
for index, cara in enumerate(text):
    print(index, cara)

text: str = 'Bonjour'
print(text)
