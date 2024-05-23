import string
import sys

def strip_punctuation_ru(data):
    clean_data = data.translate(str.maketrans('', '', string.punctuation))
    return ' '.join(clean_data.split())

def main():
    input_data = sys.stdin.readline().strip()
    result = strip_punctuation_ru(input_data)
    print(result)

if __name__ == "__main__":
    main()
