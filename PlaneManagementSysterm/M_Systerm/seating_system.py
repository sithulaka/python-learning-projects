from Person import Person
from Ticket import Ticket

class SeatingSystem:
    def __init__(self):
        self.seat = {
            "A": [0 for _ in range(14)],
            "B": [0 for _ in range(12)],
            "C": [0 for _ in range(12)],
            "D": [0 for _ in range(14)]
        }

        self.ticket_prices = {
            "1-5": 200,
            "6-9": 150,
            "10-14": 180
        }

    def get_row_letter_seat_number(self):
        while True:
            try:
                self.row_letter = input("Please enter the row letter (A, B, C, D): ").upper()
                self.seat_number = int(input("Please enter the seat number: "))
            except ValueError:
                print("Invalid input. Please try again.")
                continue

            if self.row_letter not in self.seat:
                print("Invalid row letter. Please enter A, B, C, or D.")
                continue

            if self.seat_number < 1 or self.seat_number > len(self.seat[self.row_letter]):
                print("Invalid seat number. Please choose a seat within the range.")
                continue
            break

    def buy_seat(self):
        surname = input("Enter passenger surname: ")
        phone_number = input("Enter passenger phone number: ")
        email = input("Enter passenger email: ")
        self.get_row_letter_seat_number()
        if self.seat[self.row_letter][self.seat_number - 1] == 1:
            print("Sorry, this seat is already taken. Please choose another seat.")
        else:
            self.seat[self.row_letter][self.seat_number - 1] = 1
            print(f"Seat {self.row_letter}{self.seat_number} has been successfully purchased.")

        if 1 <= self.seat_number <= 5:
            price = self.ticket_prices["1-5"]
        elif 6 <= self.seat_number <= 9:
            price = self.ticket_prices["6-9"]
        elif 10 <= self.seat_number <= 14:
            price = self.ticket_prices["10-14"]
        
        person = Person(surname, phone_number, email)
        ticket = Ticket(f"{self.row_letter}{self.seat_number}", price)
        ticket.person = person
        ticket.save()

    

    def cancel_seat(self):
        self.get_row_letter_seat_number()
        if self.seat[self.row_letter][self.seat_number - 1] == 0:
            print("Sorry, this seat is already available. Please choose another seat to cancel.")
        else:
            self.seat[self.row_letter][self.seat_number - 1] = 0
            print(f"Seat {self.row_letter}{self.seat_number} has been successfully canceled and is now available.")

            # for ticket in tickets_sold:
            #     if ticket.seat == f"{row}{seat_number}":
            #         tickets_sold.remove(ticket)
            #         break

    def find_first_available_seat(self):
        for row_letter, seats in self.seat.items():
            for seat_number, availability in enumerate(seats, start=1):
                if availability == 0:
                    print(f"The first available seat is {row_letter}{seat_number}.")
                    return
        print("Sorry, no available seats.")

    def show_seating_plan(self):
        print("\n      ", end="")  # For alignment with seat numbers
        for seat_number in range(1, 15):
            print(f"{seat_number:2}", end=" ")
        print()  # Move to the next line after printing all seat numbers

        for row_letter, seats in self.seat.items():
            print(f"Row {row_letter}:", end=" ")
            for availability in seats:
                if availability == 1:
                    status = "X" 
                else:
                    status = "O"
                print(f"{status:2}", end=" ")
            print()

        print("\n\"0\" is Available.")
        print("\"x\" is Booked.")

    def print_ticket_information_and_total_sales(self):
        total_seats = sum(sum(row) for row in self.seat.values())
        total_sales = 0
        for row_letter, seats in self.seat.items():
            for seat_number, availability in enumerate(seats, start=1):
                if 1 <= seat_number <= 5:
                    total_sales += availability * self.ticket_prices["1-5"]
                elif 6 <= seat_number <= 9:
                    total_sales += availability * self.ticket_prices["6-9"]
                elif 10 <= seat_number <= 14:
                    total_sales += availability * self.ticket_prices["10-14"]

        print(f"Total seats sold: {total_seats}")
        print(f"Total sales: ${total_sales}")

    def search_ticket(self):
        self.get_row_letter_seat_number()
        if self.row_letter in self.seat and 1 <= self.seat_number <= len(self.seat[self.row_letter]):
            if self.seat[self.row_letter][self.seat_number - 1] == 1:
                print(f"Ticket found at seat {self.row_letter}{self.seat_number}.")
            else:
                print(f"No ticket found at seat {self.row_letter}{self.seat_number}.")
        else:
            print("Invalid row letter or seat number.")
