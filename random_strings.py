import random
import string

letters = string.ascii_uppercase
numbers = string.digits
code = ''.join(random.choice(letters) for i in range(3))
num = ''.join(random.choice(numbers) for j in range(8))

print (f"Codi {code} Rang {num}\n\n")


#Posibles combinacions
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.whitespace)  # ' \t\n\r\x0b\x0c'
print(string.punctuation)

