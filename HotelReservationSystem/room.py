def display_rooms():
    print("\n===== ROOM SELECTION =====")
    print("1. Standard Room - ₱1,500.00 per night")
    print("2. Deluxe Room   - ₱2,500.00 per night")
    print("3. Suite Room    - ₱4,000.00 per night")

def select_room():
    display_rooms()
    
    while True:
        try:
            choice = int(input("\nSelect Room (1-3): "))
            if choice == 1:
                room_type, price = "Standard Room", 1500.0
                break
            elif choice == 2:
                room_type, price = "Deluxe Room", 2500.0
                break
            elif choice == 3:
                room_type, price = "Suite Room", 4000.0
                break
            else:
                print("Invalid room selection! Please choose from 1 to 3.")
        except ValueError:
            print("Invalid input! Please enter a number (1-3).")

    while True:
        try:
            nights = int(input("\nEnter Number of Nights: "))
            if nights <= 0:
                print("Invalid input! Number of nights must be positive.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            
    return room_type, price, nights