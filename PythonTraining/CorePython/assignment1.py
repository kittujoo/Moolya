def reverse_string(s):
    return s[::-1]


def palindrome(s):
    return s == s[::-1]


def find_char_count_in_string(c, s):
    return s.count(c)


def split_string(split_item, s):
    return s.split(split_item)


if __name__ == '__main__':
    var = "Hello"
    # var = "KtK"
    char = 'l'

    print(f"Given string '{var}' and reversed string is : '{reverse_string(var)}'")
    print("Is given string palindrome : ", palindrome(var))
    print(f"The count of '{char}' in a string '{var}' is : ", find_char_count_in_string(char, var))
    print(split_string(char, var))
