# Create a program
# Take 5 numbers from users
# Add 1,2 duplicates
# Print the non duplicate number

input_string = input("Enter 5 duplicate numbers with spaces in between: ")
list1 = input_string.split()
print(list1)
print(sorted(set(list1)))
