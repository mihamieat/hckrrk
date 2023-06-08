def validator(string):
    has_alphanum = False
    has_alphabetic = False
    has_digits = False
    has_lowercase = False
    has_uppercase = False
    for char in string:
        if char.isalnum():
            has_alphanum = True
        if char.isalpha():
            has_alphabetic = True
        if char.isdigit():
            has_digits = True
        if char.islower():
            has_lowercase = True
        if char.isupper():
            has_uppercase = True
    return (
        has_alphanum, has_alphabetic, has_digits, has_lowercase, has_uppercase
        )


if __name__ == "__main__":
    s = input()
    for result in validator(s):
        print(result)
