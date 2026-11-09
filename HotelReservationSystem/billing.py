def calculate_room_cost(price_per_night, nights):
    return price_per_night * nights

def calculate_discount(room_cost):
    if room_cost >= 10000:
        discount_rate = 0.15
    elif 5000 <= room_cost <= 9999.99:
        discount_rate = 0.10
    else:
        discount_rate = 0.0
        
    discount_amount = room_cost * discount_rate
    return discount_rate, discount_amount

def calculate_additional_charges(num_guests, nights, has_breakfast, has_extra_bed, has_pickup):
    breakfast_cost = (250 * num_guests * nights) if has_breakfast else 0.0
    extra_bed_cost = (500 * nights) if has_extra_bed else 0.0
    pickup_cost = 800.0 if has_pickup else 0.0
    
    return breakfast_cost, extra_bed_cost, pickup_cost

def calculate_final_bill(room_cost, discount_amount, total_additional_charges):
    return room_cost - discount_amount + total_additional_charges