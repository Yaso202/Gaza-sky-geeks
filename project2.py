import os

# Initialize the list of buses
buses = [{'name': 'Bus 1', 'destination': 'New York', 'capacity': 50, 'seats_taken': 0},
         {'name': 'Bus 2', 'destination': 'Chicago', 'capacity': 40, 'seats_taken': 0},
         {'name': 'Bus 3', 'destination': 'Los Angeles', 'capacity': 45, 'seats_taken': 0}]

# Function to display the available buses and destinations
def show_buses():
  print('\nAvailable buses:')
  for i, bus in enumerate(buses):
    print(f'{i+1}. {bus["name"]} to {bus["destination"]}')

# Function to check the seat availability
def check_availability():
  show_buses()
  bus_number = int(input('\nEnter the bus number: '))
  bus = buses[bus_number-1]
  seats_available = bus['capacity'] - bus['seats_taken']
  print(f'\nSeats available on {bus["name"]}: {seats_available}')

# Function to book a seat
def book_seat():
  show_buses()
  bus_number = int(input('\nEnter the bus number: '))
  bus = buses[bus_number-1]
  if bus['seats_taken'] < bus['capacity']:
    bus['seats_taken'] += 1
    print(f'\nSeat booked on {bus["name"]} to {bus["destination"]}')
  else:
    print('\nSorry, this bus is full.')

# Main function
def main():
  while True:
    print('\nWelcome to the Shuttle Bus booking app!')
    print('\nPlease select an option:')
    print('1. View available buses and destinations')
    print('2. Check seat availability')
    print('3. Book a seat')
    print('4. Exit')
    choice = int(input('\nEnter your choice: '))
    if choice == 1:
      show_buses()
    elif choice == 2:
      check_availability()
    elif choice == 3:
      book_seat()
    elif choice == 4:
      break
    else:
      print('\nInvalid choice. Please try again.')
      if name == 'main':
          Main()