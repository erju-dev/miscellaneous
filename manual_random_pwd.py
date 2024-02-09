import random
import sys

tamany = 26
numeros = "0123456789"
lletres = "abcdefghijklmnopkrstuvwxyz"
especials = "@#€_&-+()/\"?!;:*|×}{\][%$]})"
pwd = ""
pos_num = 0
pos_car = 0
pos_esp = 0
    

def aleatori(tipus):
    if tipus == "num":
        pos_num = random.randrange(0,len(numeros))
        return pos_num
    elif tipus == "car":
        pos_car = random.randrange(0,len(lletres))
        return pos_car
    elif tipus == "esp":
        pos_esp = random.randrange(0,len(especials))
        return pos_esp

#for x in range(tamany):
while (len(pwd)) <= tamany - 3:
    pos_num = aleatori("num")
    pos_car = aleatori("car")
    pos_esp = aleatori("esp")
    #print (pos_num, pos_car, pos_esp)
    num = numeros[pos_num]
    car = lletres[pos_car]
    esp = especials[pos_esp]
    ordre = random.randrange(1,3)
    #print (ordre)
    if ordre == 1:
        pwd = pwd + num + car + esp
    elif ordre == 2:
        pwd = car + pwd + num + esp
    elif ordre == 3:
        pwd = esp + num + car + pwd

print (pwd)
#print (len(pwd))

