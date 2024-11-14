Listaspesa = [""]
def aggiungi(): 
    spesa = int(input("inserisci elemento alla lista della spesa: "))
    for i in range (spesa):
        prodotti = input("inserisci il prodotto: ")
        Listaspesa.append(prodotti)

def visualizza():
    print(Listaspesa)

def elimina():
 id = int(print("inserisci l'id del prodotto che vuoi rimuovere"))
 Listaspesa.pop (id - 1)

def conta ():
    print(len(Listaspesa))

def svuota ():
    Listaspesa.clear()
    print("lista della spesa svuotata")



                        