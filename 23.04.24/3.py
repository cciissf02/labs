import re
def is_correct_mobile_phone_number_ru(number):
    pattern = r'^(\+?7|8)[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}$'
    return bool(re.match(pattern, number))

def test_is_correct_mobile_phone_number_ru():
    test_cases = ["+7 999 123-45-67", "8(900)1234567", "+79261234567", "1234567890"]
    for case in test_cases:
        result = "YES" if is_correct_mobile_phone_number_ru(case) else "NO"
        print(result)

test_is_correct_mobile_phone_number_ru()
