def primeNumber(num):
    if num <2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    if num == 3:
        return True
    if num % 3 == 0:
        return False
    if num == 5:
        return True
    if num % 5 == 0:
        return False
    
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

print("Prime numbers between 1 and 250 are: ")
for num in range(1, 250):
    if primeNumber(num):
        print(num, end=" ")