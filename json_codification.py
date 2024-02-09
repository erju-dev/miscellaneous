# Codificamos fichero JSON
d_verdura1 = {
    "Nombre": "tomate",
    "Cantidad": 10
}
d_verdura2 = {
    "Nombre": "pepino",
    "Cantidad": 9
}
d_fruta1 = {
    "Nombre": "kiwi",
    "Cantidad": 3
}
d_fruta2 = {
    "Nombre": "manzana",
    "Cantidad": 6
}
l_verduras = [d_verdura1, d_verdura2]
l_frutas = [d_fruta1, d_fruta2]
d_verduras = {
    "verduras": l_verduras
}
d_frutas = {
    "frutas": l_frutas
}
d_fruteria = {
    "fruteria": [d_verduras, d_frutas]
}
# codificamos la estructura anterior a json (dumps)
import json

json_fruteria = json.dumps(d_fruteria)
#print("Tipo dato:", type(json_fruteria), "\n")
#print("Datos --->", json_fruteria, "\n")

json_fruteria_indent = json.dumps(d_fruteria, indent=4, sort_keys=True)
print(json_fruteria_indent, "\n")



# guardamos json en fichero
#with open(r"info.json", "w") as file:
#    file.write(json_fruteria)
