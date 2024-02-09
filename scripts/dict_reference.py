dict = {
    'Nom': 'Eric',
    'Cognom': 'Julia'
}

print("Referencia dict2 a dict")
dict2 = dict

print("dict2: ", dict2['Nom'])

print("Cambiem nom")
dict2['Nom'] = "Txell"

print("dict2: ", dict2['Nom'])

print("dict: ", dict['Nom'])

print()
print()

dict = {
    'Nom': 'Eric',
    'Cognom': 'Julia'
}

print("Referencia dict2 a dict")
dict2 = dict.copy()

print("dict2: ", dict2['Nom'])

print("Cambiem nom")
dict2['Nom'] = "Txell"

print("dict2: ", dict2['Nom'])

print("dict: ", dict['Nom'])


