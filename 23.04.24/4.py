import re
import sys

def is_correct_mobile_phone_number_ru(number):
    pattern = r'^(\+?7|8)[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}$'
    return bool(re.match(pattern, number))

def main():
    input_number = sys.stdin.readline().strip()
    if is_correct_mobile_phone_number_ru(input_number):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
