def calculate_bill_amount(food_type, quantity_ordered, distance_in_kms):
    # Validate inputs
    if food_type not in ['V', 'N']:
        return -1
    if quantity_ordered < 1 or distance_in_kms <= 0:
        return -1

    # Calculate base cost
    if food_type == 'V':
        base_price = 120
    else:  # food_type == 'N'
        base_price = 150

    total_food_cost = base_price * quantity_ordered

    # Calculate delivery charges
    if distance_in_kms <= 3:
        delivery_charge = 0
    elif distance_in_kms <= 6:
        delivery_charge = (distance_in_kms - 3) * 3
    else:
        delivery_charge = (3 * 3) + (distance_in_kms - 6) * 6

    return total_food_cost + delivery_charge
