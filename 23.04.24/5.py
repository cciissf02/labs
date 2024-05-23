import string

def strip_punctuation_ru(data):
    clean_data = data.translate(str.maketrans('', '', string.punctuation))
    return ' '.join(clean_data.split())

def test_strip_punctuation_ru():
    test_cases = [
        ("Привет, как дела?", "Привет как дела"),
        ("Это тестовая строка!", "Это тестовая строка"),
        ("Привет!!!", "Привет"),
        ("Удалим знаки!@#$%^&*()", "Удалим знаки%^")
    ]
    for data, expected_result in test_cases:
        result = strip_punctuation_ru(data)
        if result == expected_result:
            print("YES")
        else:
            print("NO")

test_strip_punctuation_ru()
 
