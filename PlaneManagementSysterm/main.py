from M_Systerm.seating_system import SeatingSystem
MS = SeatingSystem()

def read_menu_from_file(filename):
    with open(filename, 'r') as file:
        menu_text = file.read()
        print(menu_text)

while True:
    read_menu_from_file('menu.txt')

    try:
        user_input = int(input("Please select an option: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if user_input < 0 or user_input > 6:
      print("Please select a valid option number from the menu.")
    elif user_input == 0:
      print("Thank you for coming!")
      break
    elif user_input == 1:
      MS.buy_seat()
    elif user_input == 2:
      MS.cancel_seat()
    elif user_input == 3:
      MS.find_first_available_seat()
    elif user_input == 4:
      MS.show_seating_plan()
    elif user_input == 5:
      MS.print_ticket_information_and_total_sales()
    else:
      MS.search_ticket()
