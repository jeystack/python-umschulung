number = int(input("Enter a number: "))

prime_numbers = []

# Start at 2: 1 is not prime, and 0 and negatives give an empty range
for i in range(2, number + 1):
    is_prime = True

    # 1 and i itself always divide i, so only 2 .. i-1 can disprove primality
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            # One divisor is enough, no need to keep checking
            break

    if is_prime:
        print(f"The number {i} is a prime number.")
        prime_numbers.append(i)
    else:
        print(f"The number {i} is not a prime number.")

print(f"The prime numbers are: {prime_numbers}")
