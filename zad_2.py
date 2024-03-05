class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library: {self.city}, {self.street}, {self.zip_code}, Open hours: {self.open_hours}, Phone: {self.phone}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}, Hire date: {self.hire_date}, Birth date: {self.birth_date}, Address: {self.city}, {self.street}, {self.zip_code}, Phone: {self.phone}"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book: {self.author_name} {self.author_surname}, Published: {self.publication_date}, Pages: {self.number_of_pages}, {self.library}"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f"Order by {self.employee} for {self.student} on {self.order_date}:\nBooks: {', '.join([str(book) for book in self.books])}"


# Creating instances
library1 = Library("City1", "Street1", "12345", "9 AM - 5 PM", "111-222-333")
library2 = Library("City2", "Street2", "54321", "10 AM - 6 PM", "444-555-666")

employee1 = Employee("John", "Doe", "2020-01-01", "1990-05-15", "City1", "Street1", "12345", "111-222-333")
employee2 = Employee("Jane", "Smith", "2019-05-01", "1988-11-30", "City2", "Street2", "54321", "444-555-666")
employee3 = Employee("Bob", "Johnson", "2021-03-15", "1995-08-20", "City1", "Street1", "12345", "777-888-999")

book1 = Book(library1, "2022-02-01", "Author1", "Surname1", 200)
book2 = Book(library1, "2020-05-10", "Author2", "Surname2", 300)
book3 = Book(library2, "2021-10-15", "Author3", "Surname3", 250)
book4 = Book(library2, "2019-12-05", "Author4", "Surname4", 180)
book5 = Book(library1, "2023-03-20", "Author5", "Surname5", 150)

student1 = "Student1"
student2 = "Student2"
student3 = "Student3"

order1 = Order(employee1, student1, [book1, book2, book3], "2024-03-01")
order2 = Order(employee2, student2, [book4, book5], "2024-03-02")

# Displaying orders
print(order1)
print("\n")
print(order2)


