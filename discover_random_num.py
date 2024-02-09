import random

nums  = 3
limit = 10

class not_int(Exception):
    def __init__(self, msg="Error"):
        msg = msg
        #super(not_int, self).__init__(msg)
class limit_exceed(Exception):
    def __init__(self, msg="Error"):
        msg = msg

def check_str(num):
    abc = "abcdefghijklmnopqrstuvwxyz"
    for x in abc:
        if x in num:
            raise not_int

try:
    print(f"Tria un numero del 0 al {limit}")
    num = input("") # default all str
    print(f"> {num}")
    check_str(num)
    num = int(num)
    
    if num > limit:
        raise limit_exceed
    
    llista = []
    for x in range(nums):
        llista.append(random.randrange(limit))
    
    print()
    if num in llista:
        print("[OK] Has encertat :)")
        print(f"Numero triat {num}, llista {llista}")
    else:
        print("[KO] Has fallat :(")
        print(f"Numero triat {num}, llista {llista}")

    #print(random.choice(llista))
except not_int:
    print("\n[Error] No has introduit un numero!")
except limit_exceed:
    print(f"\n[Error] Numero fora del limit 0-{limit}!")



