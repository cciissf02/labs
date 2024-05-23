class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

class SequenceError(PasswordError):
    pass

def check_password(password):
    # Проверка длины пароля
    if len(password) < 9:
        raise LengthError

    # Проверка наличия больших и маленьких букв
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    if not (has_upper and has_lower):
        raise LetterError

    # Проверка наличия хотя бы одной цифры
    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        raise DigitError

    # Проверка отсутствия комбинаций из 3 буквенных символов, стоящих рядом на клавиатуре
    keyboard_sequences = ['qwe', 'asd', 'zxc', 'йцу', 'фыв', 'ячс']
    for seq in keyboard_sequences:
        if seq in password.lower():
            raise SequenceError

    # Если все критерии выполнены, возвращаем "ok"
    return "ok"

def main():
    while True:
        try:
            password = input("Введите пароль: ")

            if password.lower() == "ctrl+break":
                raise KeyboardInterrupt

            result = check_password(password)
            print(result)
            if result == "ok":
                break

        except PasswordError as e:
            print("Ошибка:", e.__class__.__name__)

        except KeyboardInterrupt:
            print("Bye-Bye")
            break

if __name__ == "__main__":
    main()