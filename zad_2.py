

# a. Utwórz funkcję, która otrzyma w parametrze listę 5 imion, a następnie
# wyświetli każde z nich.

imiona = ["Kasia", "Basia", "Asia", "Zosia", "Krysia"]


def wyswietlanie_imion(imiona):
    for imie in imiona:
        print (imie)


wyswietlanie_imion(imiona)

# b. Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5
# dowolnych liczb, każdy jej element pomnoży przez 2, a na końcu ją
# zwróci. Zadanie należy wykonać w 2 wersjach:
# i. Wykorzystując pętle for .


liczby = [10, 20, 30, 40, 50]

def mnozenie_liczb(liczby):
    for liczba in liczby:

        liczba *=2
        print(liczba)


mnozenie_liczb(liczby)

# ii. Wykorzystując listę składaną.

def mnozenie_razy2(liczby):
    return [liczba * 2 for liczba in liczby]


wynik_mnozenia = mnozenie_razy2(liczby)

print(wynik_mnozenia)



# c. Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
# (rekomendowane wykorzystanie funkcji range ), a następnie wyświetli
# jedynie parzyste elementy.

liczby = list(range(1, 11))

def parzyste_liczby(liczby):
    for liczba in liczby:
        if liczba%2==0:
            print(liczba)

parzyste_liczby(liczby)



# d. Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
# (rekomendowane wykorzystanie funkcji range ), a następnie wyświetli co
# drugi element.

def co_drugi_element(liczby):
    for i in range(1, len(liczby), 2):
        print(liczby[i])



co_drugi_element(liczby)
