class Person:
    def __init__(self, surname, phone_number, email):
        self.surname = surname
        self.phone_number = phone_number
        self.email = email

    def print_info(self):
        print(f"Surname: {self.surname}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Email: {self.email}")