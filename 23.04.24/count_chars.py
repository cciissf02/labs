def count_chars(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count
 
