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

while True:
    numero = int(input("Inserisci un numero intero (0 per terminare): "))
    if numero == 0:
        break  
    elif numero == 1:
        (aggiungi)
    elif numero == 2:
        (visualizza)
    elif numero == 3:
        (elimina)
    elif numero == 4:
        (conta)
    elif numero == 5:
        (svuota)

                        