def prime_floor(z):
    "Find the biggest prime number below z, where z is an int > 2."
    for i in range(z,2,-1):
        is_prime = True
        for j in range(2,i//2):
            if i//j == i/j:
                is_prime = False
                break
        if is_prime:
            return i
