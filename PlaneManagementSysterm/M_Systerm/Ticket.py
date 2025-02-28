class Ticket:
    def __init__(self, seat, price):
        self.seat = seat
        self.price = price
        self.person = None  # To store associated Person object

    def print_info(self):
        print(f"Seat: {self.seat}")
        print(f"Price: {self.price}")
        if self.person:
            print("Passenger:")
            self.person.print_info()
        else:
            print("Passenger: Not Assigned")

    def save(self):
        filename = f"{self.seat}.txt"
        with open(filename, "w") as file:
            file.write(f"Seat: {self.seat}\n")
            file.write(f"Price: {self.price}\n")
            if self.person:
                file.write("Passenger:\n")
                file.write(f"\tSurname: {self.person.surname}\n")
                file.write(f"\tPhone Number: {self.person.phone_number}\n")
                file.write(f"\tEmail: {self.person.email}\n")
            else:
                file.write("Passenger: Not Assigned\n")