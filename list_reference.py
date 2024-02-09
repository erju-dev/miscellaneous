
llista = ["Txell", "Eric", "Lia", "Nil"]
print("Llista: ", llista)

print("Fem referencia llista2 a llista")
llista2 = llista

print("Llista2 pos 3: ", llista2[3])

print("Cambiem llista2 pos 3")
llista2[3] = "Niiil"

print("Llista2 pos 3: ", llista2[3])

print("Llista pos 3: ", llista[3])


print()
print()

llista = ["Txell", "Eric", "Lia", "Nil"]
print("Llista: ", llista)

print("Fem copia llista2 a llista")
llista2 = llista.copy()

print("Llista2 pos 3: ", llista2[3])

print("Cambiem llista2 pos 3")
llista2[3] = "Niiil"

print("Llista2 pos 3: ", llista2[3])

print("Llista pos 3: ", llista[3])