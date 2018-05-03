class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num

    def is_valid(self):
        # Spaces are the only non-numeric characters accepted
        card_num_clean = str(self.card_num).replace(' ', '')
        if not card_num_clean.isdigit():
            return False

        # Minimum length of 2 digits
        if len(card_num_clean) < 2:
            return False

        # Strip zeros at beginning
        card_num_clean = str(int(card_num_clean))

        # Calculate the checksum
        luhn_sum = 0
        for k, c in enumerate(card_num_clean):
            digit = int(c)
            luhn_sum += digit
            if k % 2 == 0:
                luhn_sum += digit
                if digit > 4:
                    luhn_sum -= 9

        return luhn_sum % 10 == 0
