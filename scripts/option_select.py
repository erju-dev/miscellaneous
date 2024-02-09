import sys
import os


x = input("opcio: ")
print (x)
#sys.exit()

opcio = ""
while (opcio != 4):
    #os.system('clear')
    print ("(1) Alta usuari")
    print ("(2) Modificar usuari")
    print ("(3) Eliminar usuari")
    print ("(4) Sortir\n")
    opcio = int(input('Opcio:'))
    print (type(opcio ))