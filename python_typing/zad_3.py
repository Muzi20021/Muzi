# Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w
# parametrze jest parzysta i zwróci tą informację jako typ logiczny bool
# ( True / False ). Należy uruchomić funkcję, wynik wykonania zapisać do
# zmiennej, a następnie wykorzystując warunek logiczny wyświetlić prawidłowy
# tekst "Liczba parzysta" / "Liczba nieparzysta"


liczba = 7
def czy_parzysta(liczba):
    if liczba % 2 == 0:
        return True
    else:
        return False


if czy_parzysta(liczba):
    print("Liczba jest parzysta.")
else:
    print("Liczba jest nieparzysta.")
