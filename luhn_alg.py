
def check_number(card_number: str) -> str:
    size = len(card_number)
    offset = size % 2
    doubled_digit_sum = sum([int(x) for x in "".join([str(2*int(x)) for x in card_number[offset::2]])])
    other_digit_sum = sum([int(x) for x in card_number[1-offset::2]])
    total_sum = doubled_digit_sum + other_digit_sum

    base_valid = not total_sum % 10
    is_amex = base_valid and size == 15 and card_number[0] == '3' and (card_number[1] in ['4', '7'])
    is_mcard = base_valid and size == 16 and card_number[0] == '5' and (int(card_number[1]) in range(1, 6))
    is_visa = base_valid and size in [13, 16] and card_number[0] == '4'

    if is_amex:
        return "AMEX"
    if is_mcard:
        return "MASTERCARD"
    if is_visa:
        return "VISA"
    return "INVALID"

if __name__ == '__main__':
    card_number = input("Number: ")
    print(check_number(card_number))
