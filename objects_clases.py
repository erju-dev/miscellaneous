class Producte():
    
    def __init__(self, id, nom, desc):
        self.id = id
        self.nom = nom
        self.desc = desc

    def __str__(self):
        return "Id ({}), Nom ({}), Desc ({})".format(self.id, self.nom, self.desc)

class Aliment(Producte):
    productor = "TBD"
    distribuidor = "TBD"
    
    def __str__(self):
        return "Id ({}), Nom ({}), Desc ({}), productor ({}), distribuidor ({})".format(self.id, self.nom, self.desc, self.productor, self.distribuidor)
    

llet = Aliment(id=57283, nom="Llet Nostra", desc="Llet semi")
llet.productor="Cadi"
#llet.distribuidor="Llets SL"
print(llet)