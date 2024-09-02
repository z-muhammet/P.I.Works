def is_prime(i, j=2):
    if i <= 2:
        return True if i == 2 else False
    if i % j == 0:
        return False
    if j * j > i:
        return True
    return is_prime(i, j + 1)

def find_prime_numbers(start, end):
    if start > end:
        return
    if is_prime(start):
        print(start)
    find_prime_numbers(start + 1, end)

find_prime_numbers(500, 600)