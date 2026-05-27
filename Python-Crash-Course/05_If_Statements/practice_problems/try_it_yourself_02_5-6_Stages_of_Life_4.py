# 5-6 Stages of Life: Write an if-elif-else chain that determines a person's stage of life. Set a value for the variable age, and then:
# If a person is less than 2 years old, print a message that the person is a baby
# If a person is atleast 2/4/13/20 years old, but less than 4/13/20/65, print a message that the person is a toddler/kid/teenager/adult.
# If a person is age 65 or older, print a message that the person is an elder.

age = 17

if age < 2:
    print("The person is a baby")
elif age >= 2 and age < 4:
    print("The person is a toddler")
elif age >= 4 and age < 13:
    print("The person is a kid")
elif age >= 13 and age < 20:
    print("The person is a teenager")
elif age >= 20 and age < 65:
    print("The person is an adult")
else:
    print("The person is an elder")
