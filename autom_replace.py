import sys


def substituir(text, paraula):
    tamany = len(paraula)
    subs = ""
    for s in range(tamany):
        subs = subs + "*"
    return text.replace(paraula, subs)
    

print (substituir("Aqui provarem contrasenya de posar la contrasenya aqui", "contrasenya"))
