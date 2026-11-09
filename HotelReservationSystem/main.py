import guest_info
import room
import billing

def get_yes_no(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Invalid response! Please enter yes or no.")

def main():
    print("=" * 50)
    print("        HOTEL RESERVATION SYSTEM")
    print("=" * 50)

    while True:
        try:
            name, contact, num_guests = guest_info.get_guest_info()
            room_type, price_per_night, nights = room.select_room()

            print("\n===== ADDITIONAL SERVICES =====")
            has_breakfast = get_yes_no("Do you want breakfast? (yes/no): ")
            has_extra_bed = get_yes_no("Do you want an extra bed? (yes/no): ")
            has_pickup = get_yes_no("Do you want airport pickup? (yes/no): ")

            room_cost = billing.calculate_room_cost(price_per_night, nights)
            disc_rate, disc_amount = billing.calculate_discount(room_cost)
            bf_cost, eb_cost, ap_cost = billing.calculate_additional_charges(
                num_guests, nights, has_breakfast, has_extra_bed, has_pickup
            )
            
            total_additional = bf_cost + eb_cost + ap_cost
            final_bill = billing.calculate_final_bill(room_cost, disc_amount, total_additional)

        except Exception as e:
            print(f"\nAn error occurred during processing: {e}")
            
        else:
            print("\n\n===== RESERVATION RECEIPT =====")
            print(f"Guest Name: {name}")
            print(f"Contact Number: {contact}")
            print(f"Number of Guests: {num_guests}\n")
            
            print(f"Room Type: {room_type}")
            print(f"Room Price per Night: ₱{price_per_night:,.2f}")
            print(f"Number of Nights: {nights}\n")
            
            print(f"Room Cost:          ₱{room_cost:,.2f}")
            print(f"Discount Rate:      {int(disc_rate * 100)}%")
            print(f"Discount Amount:    ₱{disc_amount:,.2f}\n")
            
            print("===== ADDITIONAL CHARGES =====")
            print(f"Breakfast:          ₱{bf_cost:,.2f}")
            print(f"Extra Bed:          ₱{eb_cost:,.2f}")
            print(f"Airport Pickup:     ₱{ap_cost:,.2f}\n")
            
            print("-----------------------------------")
            print(f"Room Cost:          ₱{room_cost:,.2f}")
            print(f"Less Discount:      ₱{disc_amount:,.2f}")
            print(f"Additional Charges: ₱{total_additional:,.2f}")
            print("-----------------------------------")
            print(f"FINAL BILL:         ₱{final_bill:,.2f}")
            print("===================================\n")

        finally:
            print("Reservation processing completed.")
            make_another = get_yes_no("Do you want to make another reservation? (yes/no): ")
            
            if not make_another:
                print("\nThank you for using the Hotel Reservation System!")
                break
            else:
                print("\n" + "=" * 50 + "\n")

if __name__ == "__main__":
    main()