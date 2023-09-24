def gcd(a, b):
    # Calculate the greatest common divisor using Euclid's algorithm
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(a, b):
    # Simplify a fraction by dividing both the numerator and denominator by their GCD
    common_divisor = gcd(a, b)
    return a // common_divisor, b // common_divisor

def find_pairs(n, a0, b0):
    # Initialize the set S with the initial pair R = a0/b0
    S = {(a0, b0)}

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if (a, b) not in S:
                # Calculate the new pair (p, q) and simplify it
                p, q = simplify_fraction(a + a0, b + b0)

                if p == a0 and q == b0:
                    # If (p, q) matches the initial pair, add it to S
                    S.add((a, b))
                elif (p, q) in S:
                    # If (p, q) is already in S, remove it (it doesn't satisfy the conditions)
                    S.remove((p, q))

    return S

# Initial values a0 and b0
a0 = 1
b0 = 2
n = 20  # Value of n

result = find_pairs(n, a0, b0)
print(result)
