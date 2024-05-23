def is_palindrome(data):
    data = data.replace(" ", "").lower()
    return data == data[::-1]

def test_is_palindrome():
    test_cases = ["level", "radar", "A man a plan a canal Panama", "hello"]
    for case in test_cases:
        result = "YES" if is_palindrome(case) else "NO"
        print(result)

test_is_palindrome()

 
