def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for _ in range(2,9):
       if num % _ == 0:
           return False
    return True
is_prime(5)