# 5-1 Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test.
# Look closely at your results, and make sure you understand why each line evaluates to True or False.
# Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.

car = 'audi'
bike = 'honda'
number = 18
cars = ['toyota', 'honda', 'bmw']


print("Is car == 'audi'? I predict True.")
print(car == 'audi')
print("\nIs car == 'bmw'? I predict False.")
print(car == 'bmw')
print("\nIs car != 'audi'? I predict False.")
print(car != "audi")

print("\nIs 18 == number? I predict True.")
print(18 == number)
print("\nIs 18!= number? I predict False.")
print(18 != number)
print("\nIs 18>= number? I predict True.")
print(18 >= number)
print("\nIs 21 < number? I predict False.")
print(21 < number)

print("\nIs car == 'audi' and bike == 'pulsar'? I predict False")
print(car == 'audi' and bike == 'pulsar')
print("\nIs car == 'audi' or bike == 'pulsar'? I predict True")
print(car == 'audi' or bike == 'pulsar')

print("\nIs 'toyota' in cars? I predict True")
print('toyota' in cars)
print("\nIs 'mercedes' in cars? I predict False")
print('mercedes' in cars)
print("\nIs 'ferrari' not in cars? I predict True")
print('ferrari' not in cars)
print("\nIs 'bmw' in cars? I predict True")
print('bmw' in cars)
print("\nIs 'honda' not in cars? I predict False")
print('honda' not in cars)


