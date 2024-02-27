# Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu
# list . Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć
# duplikaty, każdy element podnieść do potęgi 3 stopnia, a następnie zwrócić
# powstałą listę.


lista = [1,2,3]
lista2 = [3,4,1,1,2,5]



def connect (lista, lista2):

    listy = lista + lista2
    listy = list(set(listy))

    potega = [el**3 for el in listy]

    return potega


wynik = connect (lista, lista2)


print(wynik)
