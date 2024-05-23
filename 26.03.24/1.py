def pass_check(word):
    if len(word) <= 8:
        return False

    has_low = any(a.islower() for a in word)
    has_upp = any(a.isupper() for a in word)
    has_dig = any(a.isdigit() for a in word)
    keyboard = {"qwertyuiop", "йцукенгшщзхъ", "asdfghjkl", "фывапролджэ", "zxcvbnm", "ячсмитьбю"}
    three_in_a_row = any(word[i:i + 3].lower() in keyboard for i in range(len(word) - 2))

    if not has_dig:
        return False

    if three_in_a_row:
        return False

    if not (has_low and has_upp):
        return False

    return True


password = input()
if pass_check(password):
    print("ok")
else:
    print("error")