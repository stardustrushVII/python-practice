def multiply_list(numbers):
    product = 1
    for item in numbers:
        if isinstance(item, (int, float)):  # only multiply if numerical val
            product *= item
    return product

# ze math:
my_list = [2, 4, 6, 16]
print(multiply_list(my_list)) 
