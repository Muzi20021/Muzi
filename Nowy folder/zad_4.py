

# Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma
# dwóch pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę
# informację jako typ logiczny bool



def sprawdz (liczba1, liczba2, liczba3):

    if liczba1 + liczba2 >= liczba3:
        return True

    else:
        return False


sprawdzanie = sprawdz (3,4,9)

print(sprawdzanie)