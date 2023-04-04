# Generation Girl Final Project

# dictionary of available dates
booking_list = {
  "1" : {"date" : "17/03/2023", "slot" : 2},
  "2": {"date" : "18/03/2023", "slot" : 1},
  "3": {"date" : "19/03/2023", "slot" : 1},
  "4": {"date": "20/03/2023", "slot": 3}
}

# list to store bookings made
booking_details = []

# function to display menu
def view_menu():
  print("""Barbeqyoo BBQ
  MENU

  1. Two Good To Be True (for 2 people)
     IDR 400,000,-
     - Beef Shortplate 250 gr
     - Beef Patties 2 x 100 gr
     - Bratwurst 100 gr
     - French Fries/Mashed Potatoes 300 gr
     - A Portion of Vegetable Platter: Lettuce, Paprika, Mushroom, Onion
  2. Three Of A Kind (for 3 people)
     IDR 550,000,-
     - Beef Shortplate 400 gr
     - Beef Patties 3 x 100 gr
     - Bratwurst 200 gr
     - French Fries/Mashed Potatoes 500 gr
     - A Portion of Vegetable Platter: Lettuce, Paprika, Mushroom, Onion
  3. Ohana Means Family (min. 4 people)
     IDR 175,000,- per pax
     - Beef Shortplate 125 gr (per pax)
     - Beef Patties 100 gr (per pax)
     - Bratwurst 75 gr (per pax)
     - French Fries/Mashed Potatoes 150 gr (per pax)
     - Portions of Vegetable Platter: Lettuce, Paprika, Mushroom, Onion
  """)

# function to make booking
def booking():
  name = input("Name: ")
  phone = input("Phone Number: ")
  address = input("Address: ")

  print("")
  print(f"Hello {name}! This is your biodata:")
  print(f"Phone number: {phone}")
  print(f"Address: {address}")
  print("")
  print("These are the available slots for this month:")
  
  # array to store only the available dates
  arr = []
  for chosen_date in booking_list.values():
    print(f"{chosen_date['date']} has {chosen_date['slot']} slots")
    arr.append(chosen_date['date'])
  print("")
  selected_date = input("Select a date: ")

  while (selected_date not in arr) :
    print("Date is unavilable! Please choose another date")
    print("")
    selected_date = input("Select a date: ")
  print("Yay! Date is available")
  print("")

  # OPTIONAL: iterate if wrong input
  chosen_menu = int(input("Select a menu to dine (1/2/3): "))
  print("")
  if(chosen_menu == 3):
    menu = "Ohana Means Family (min. 4 people)"
    print(f"You have selected {menu} menu")
    qty = int(input("Input how many people you will be dining with (min. 4): "))
    price, tax, grand_total = calculate(chosen_menu, qty)
    print(f"Menu price: {price}")
    print(f"Service tax (10%): {tax}" )
    print(f"Grand total: {grand_total}" )
  elif(chosen_menu == 1):
    price, tax, grand_total = calculate(chosen_menu, 2)
    menu = "Two Good To Be True"
    print(f"You have selected {menu} menu")
    print(f"Menu price: {price}")
    print(f"Service tax (10%): {tax}" )
    print(f"Grand total: {grand_total}" )
  else:
    price, tax, grand_total = calculate(chosen_menu, 3)
    menu = "Three of A Kind"
    print(f"You have selected {menu} menu")
    print(f"Menu price: {price}")
    print(f"Service tax (10%): {tax}" )
    print(f"Grand total: {grand_total}" )
    
  booking_details.append([selected_date, name, grand_total])

# function to view all bookings
def view_bookings():
  if(len(booking_details) == 0 ):
    print("No bookings made yet!")
  else:
    print("These are the available bookings:")
    print("[Booking Date]], [Name], [Price]")
    for booking_detail in booking_details:
      print(booking_detail)
    print("")

# function to cancel a booking
def cancel_booking(to_delete):
  confirmation = input(f"Are you sure you would like to cancel booking under the name {to_delete} (yes/no)? ")
  if(confirmation =="yes"):
    index_to_delete = 0
    is_found = False
    # asumsi nama yg diinput unik
    for booking_detail in booking_details:
      for nested_booking_detail in booking_detail:
        if (nested_booking_detail == to_delete):
          is_found = True
      if(is_found == False):
        index_to_delete += 1

    if(is_found): 
      print("Deleting data...")
      booking_details.pop(index_to_delete)
    else:
      print("Name was not found")
  else:
    print("Undo action...")

# function to calculate total, service tax, and grand total
def calculate(menu, qty):
  if(menu == 1):
    price = 400000*qty
    tax = price*0.1
    grand_total = price+tax
  elif(menu == 2):
    price = 550000*qty
    tax = price*0.1
    grand_total = price+tax
  else:
    price = 175000*qty
    tax = price*0.1
    grand_total = price+tax
  return (price, tax, grand_total)

# function to print options 
def print_choice():
  print("""==============================================
  Barbeqyoo BBQ
  We help you grill without worries
  contactus@barbeqyoo.bbq
  
  Welcome to Barbeqyoo BBQ, can we help you?
  1. View Menu
  2. Book BBQ Home Service
  3. View All Bookings
  4. Cancel Booking
  5. Quit
""")

# function to choose an option
# - asumsi no invalid input
def select_choice():
  print_choice()
  choice = int(input("Input (1..5): "))
  print("==============================================")
  while(choice < 5 and choice > 0):
    if(choice == 1):
      view_menu()
    elif(choice == 2):
      booking()
    elif(choice == 3):
      view_bookings()
    elif(choice == 4):
      view_bookings()
      print("")
      to_delete = input("Input the booking name you would like to cancel: ")
      cancel_booking(to_delete)
    else:
      print("Thank you for visiting Barbeqyoo. Hope to see you next time <3")
    print_choice()
    choice = int(input("Input (1..5): "))
  
  if(choice == 5):
    print("Thank you for visiting Barbeqyoo. Hope to see you next time <3")
  elif(choice < 5 and choice > 0):
    print("Invalid input!")
    select_choice()
    
select_choice()
