import sys

def is_palindrome(data):
    data = data.replace(" ", "").lower()
    return data == data[::-1]

def main():
    input_string = sys.stdin.readline().strip()
    if is_palindrome(input_string):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()

