def check_password(password):
    try:
        # Проверка длины пароля
        assert len(password) >= 9, "Длина пароля должна быть не менее 9 символов."

        # Проверка наличия больших и маленьких букв
        assert any(char.isupper() for char in password) and any(char.islower() for char in password), "Пароль должен содержать и большие, и маленькие буквы."

        # Проверка наличия хотя бы одной цифры
        assert any(char.isdigit() for char in password), "Пароль должен содержать хотя бы одну цифру."

        # Проверка отсутствия комбинаций из 3 буквенных символов, стоящих рядом на клавиатуре
        keyboard_sequences = ['qwe', 'asd', 'zxc', 'йцу', 'фыв', 'ячс']
        for seq in keyboard_sequences:
            assert seq not in password.lower(), "Пароль содержит недопустимую последовательность символов."

        # Если все критерии выполнены, возвращаем "ok"
        return "ok"

    except AssertionError as e:
        return "error: " + str(e)

    except Exception as e:
        return "error: " + str(e)

# Пример использования функции
password = input("Введите пароль: ")
result = check_password(password)
print(result)