# 6-2 Favorite Numbers: Use a dictionary to store people's favorite numbers.
# Think of five names, and use them as keys in your dictionary. 
# Think of a favorite number for each person , and store each as a value in your dictionary.
# Print each person's name and their favorite number.
# For even more fun, poll a few friends and get some actual data for your program.

favorite_numbers = {'Sattire': 729,
    'Wey': 67,
    'Losercat': 13,
    'larper': 24,
    'tsoi': 69
    }

people = ['Sattire', 'Wey', 'Losercat', 'larper', 'tsoi']

for person in people:
    print(f"{person}'s favorite number is {favorite_numbers[person]}.")