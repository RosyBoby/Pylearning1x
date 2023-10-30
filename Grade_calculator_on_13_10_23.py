# Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
# input- score - 89
# output- B
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

marks=int(input("Enter the marks that you received out of 100\n"))
if  marks >=90 and marks<=100 :result='A'
elif marks>=80 and marks<=89 :result='B'
elif marks >= 70 and marks <= 79 :result='C'
elif marks >= 60 and marks <= 69 :result='D'
else:result='F'
print("The Grade received is:",result)
