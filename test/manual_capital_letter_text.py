def separacio(var):
    if var == " ":
        sep = " "
        return sep
    elif var == ".":
        sep = "."
        return sep
    elif var == ",":
        sep = ","
        return sep
    else:
        return False 

def majus(txt):
    # Fem llista i contador
    txt_list = list(txt)
    txt_count = len(txt_list)
    count = 0
    print (txt_count)
    
    # Majus inici frase
    txt_list[0] = txt_list[0].upper()
    
    # Majus altres paraules
    for x in range(txt_count):
        sep = separacio(txt_list[x])
        if sep != False:
            txt_pos = txt_list.index(sep,count)
            txt_list[txt_pos+1] = txt_list[txt_pos+1].upper()
            count = txt_pos + 1
    
    # Preparar sortida
    txt = ''.join(txt_list)
    return txt

print (majus("hola bon dia. com. estas, jo,estic    be"))