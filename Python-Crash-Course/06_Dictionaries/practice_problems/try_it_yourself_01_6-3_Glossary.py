# 6-3 Glossary: A python dictionary can be used to model an actual dictionary.
# However to avoid confusion, lets call it glossary.
# Think of 5 programming words you've learnt about in the previous chapters. Use these words a keys in your glossary, and store their meanings as values.  
# Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline charecter {\n} to insert a blank line between each word-meaning pair in your output.

glossary = {'print()': 'displays the value in terminal',
    'upper()': 'method that returns the value of a string as all uppercase',
    'pop()': 'method that deletes the last value in a list and lets us use it',
    'if': 'keyword that runs the indented code just below it if it has True and ignores if it has Falsee',
    'python': 'A programming language',
    }

print(f"print()\n{glossary['print()']}")
print(f"\nupper()\n{glossary['upper()']}")
print(f"\npop()\n{glossary['pop()']}")
print(f"\nif\n{glossary['pop()']}")
print(f"\npython\n{glossary['python']}")