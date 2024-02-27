# Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a drugi
# typu int . Funkcja ma sprawdzić (zwracając typ logiczny bool ), czy lista z
# parametru pierwszego zawiera taką wartość jaką przekazano w parametrze
# drugim.

lista = [ "raz", "dwa", "trzy"]
slowo = "raz"

def sprawdz (lista, slowo):

    if  slowo in lista:
        return True

    else:
        return False

sprawdzanie = sprawdz(lista, slowo)

print(sprawdzanie)