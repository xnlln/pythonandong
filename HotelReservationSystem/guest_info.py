def get_guest_info():
    print("\n===== GUEST INFORMATION =====")
    name = input("Enter Guest Name: ").strip()
    contact = input("Enter Contact Number: ").strip()
    
    while True:
        try:
            num_guests = int(input("Enter Number of Guests: "))
            if num_guests <= 0:
                print("Invalid input! Number of guests must be positive.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            
    return name, contact, num_guests