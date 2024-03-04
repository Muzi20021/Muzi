# Zadania do wykonania
# 1. Stworzyć klasę Student , która posiada 2 parametry (name i marks) oraz jedną
# metodę is_passed, która zwraca wartość logiczną, pozytywną gdy średnia
# ocen jest > 50 w przeciwnym przypadku negatywną. Następnie należy
# stworzyć 2 przykładowe obiekty klasy, tak aby dla pierwszego obiektu metoda
# zwracała true , a dla drugiego false .


from statistics import mean




class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if mean(self.marks) > 50:
            return True
        else:
            return False


studentT = Student("Jan", [50, 60, 70])
studentF = Student("Maria", [10, 20 , 25])

print(f"{studentT.name} Result: {studentT.is_passed()}")
print(f"{studentF.name} Result: {studentF.is_passed()}")


