# 4-6 Odd Numbers: Use a list comprehension to generate a list of the odd numbers from 1 to 20. Use a for loop to print each number.
odd_numbers = []
for odd_number in range(1, 21, 2):
    odd_numbers.append(odd_number)
for odd_number in odd_numbers:
    print(odd_number)
    