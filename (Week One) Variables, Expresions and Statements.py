def sum_of_multiples(start, end, divisor):
    total = sum(num for num in range(start, end + 1) if num % divisor == 0)
    return total


print(sum_of_multiples(1, 10, 2))  # Output
