def is_password_valid(received_pass):
    is_valid = True
    if not 6 <= len(received_pass) <= 10:
        is_valid = False
        print(f'Password must be between 6 and 10 characters')

    for char in received_pass:
        if not (48 <= ord(char) <= 57 or 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122):
            is_valid = False
            print('Password must consist only of letters and digits')
            break

    digits = 0
    for char in received_pass:
        if 48 <= ord(char) <= 57:
            digits += 1
    if digits < 2:
        is_valid = False
        print(f'Password must have at least 2 digits')

    if is_valid:
        return print('Password is valid')


received_password = input()

is_password_valid(received_password)
