def make_amount(rupees_to_make, no_of_five, no_of_one):
    five_needed = min(rupees_to_make // 5, no_of_five)

    while five_needed >= 0:
        remaining = rupees_to_make - (five_needed * 5)
        if remaining <= no_of_one:
            print(f"No. of Five needed : {five_needed} No. of One needed : {remaining}")
            return
        five_needed -= 1

    print("-1")
