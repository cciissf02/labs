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
        raise LengthError("Длина пароля должна быть не менее 9 символов.")

    # Проверка наличия больших и маленьких букв
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    if not (has_upper and has_lower):
        raise LetterError("Пароль должен содержать и большие, и маленькие буквы.")

    # Проверка наличия хотя бы одной цифры
    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        raise DigitError("Пароль должен содержать хотя бы одну цифру.")

    # Проверка отсутствия комбинаций из 3 буквенных символов, стоящих рядом на клавиатуре
    keyboard_sequences = ['qwe', 'asd', 'zxc', 'йцу', 'фыв', 'ячс']
    for seq in keyboard_sequences:
        if seq in password.lower():
            raise SequenceError("Пароль содержит недопустимую последовательность символов.")

    # Если все критерии выполнены, возвращаем "ok"
    return "ok"

# Пример использования функции
try:
    password = input("Введите пароль: ")
    result = check_password(password)
    print(result)
except PasswordError as e:
    print("Ошибка:", e)