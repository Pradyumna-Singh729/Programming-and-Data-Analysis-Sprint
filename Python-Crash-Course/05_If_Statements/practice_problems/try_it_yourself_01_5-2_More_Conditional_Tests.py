# 5-2 More Conditional Tests: You don’t have to limit the number of tests you create to 10. If you want to try more comparisons, write more tests and add them to conditional_tests.py. 
str_1 = 'Furina'
str_2 = 'Guilty'
str_3 = 'Furina'
str_4 = 'FuRina'

print("Is Furina Guilty? I predict False.")
print(str_1 == str_2)
print("\nIs str_1 == str_3? I predict True")
print(str_1 == str_3)
print("\nIs 'furina == str_4? I predict False")
print(str_1 == str_4)
print("\nIs 'furina' == str_4.lower()? I predict True")
print('furina' == str_4.lower())
# Rest is done in 5-1