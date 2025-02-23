def factorial(n): 
    if n == 0 or n == 1: 
        return 1 
    return n * factorial(n - 1)

def is_prime(n): 
    if n < 2: 
        return False 
    for i in range(2, int(n ** 0.5) + 1): 
        if n % i == 0: 
            return False 
    return True
def is_power_of_5(n): 
    while n > 1 and n % 5 == 0: 
        n //= 5 
    return n == 1
def is_power_of_2(n): 
    return (n & (n - 1)) == 0 and n > 0
