def check_password_strength(password, min_length=8, require_special=True):
    total_score = (calculate_length_score(password, min_length) + calculate_case_score(password) +
                   calculate_number_score(password) + calculate_special_char_score(password))

    if calculate_special_char_score(password) == 0:
        total_score = 0

    get_strength_rating(total_score)


def calculate_length_score(password, min_length):
    return min(25, max(0, (len(password) - min_length) * 5))

def calculate_case_score(password):
    capital = 0
    not_capital = 0
    for char in password:
        if char == char.upper():
            capital += 1
        elif char == char.lower():
            not_capital += 1
    ratio = capital / not_capital
    return min(25, int(ratio * 50))
#Calculate the ratio of uppercase to total letters

def calculate_number_score(password):
    count = 0
    for char in password:
        if char.isdigit():
            count += 1
    return min(25, count * 8)
#Count the number of digits in the password

def calculate_special_char_score(password):
    count = 0
    for char in password:
        if not(char.isalnum()):
            count += 1
    return min(25, count * 8)
#Count the number of special characters in the password


def get_strength_rating(score):
    if score > 80:
        print("Very Strong")
    elif score > 60:
        print("Strong")
    elif score > 40:
        print("Average")
    elif score > 20:
        print("Weak")
    elif score >= 0:
        print("Very Weak")
    else:
        print("Something went wrong!")

password = input("Enter Password:\n")
check_password_strength(password, 10, True)
