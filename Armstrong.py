def CheckArmstrong(n):
    i = n
    count = 0

    # Count the number of digits
    while n != 0:
        count += 1
        n //= 10

    n = i
    result = 0

    # Calculate the Armstrong number
    while n != 0:
        r = n % 10
        p = 1
        for j in range(count):
            p *= r
        result += p
        n //= 10

    return i == result

n = int(input("Enter the number: "))

if CheckArmstrong(n):
    print(f"The Given Number is Armstrong: {n}")
else:
    print(f"The Given Number is not Armstrong: {n}")
