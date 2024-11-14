Listaspesa = [""]
def aggiungi(): 
    spesa = int(input("inserisci elemento alla lista della spesa: "))
    for i in range (spesa):
        prodotti = input("inserisci il prodotto: ")
        Listaspesa.append(prodotti)

def visualizza():
    print(Listaspesa)


                        