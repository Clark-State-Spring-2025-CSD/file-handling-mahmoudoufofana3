#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the number
#Average
#Highest number
#Lowest number
#Correct answers for the included file:

with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file if line.strip()]

count = len(numbers)
total = sum(numbers)
average = total / count if count != 0 else 0
highest = max(numbers)
lowest = min(numbers)

print("How many numbers in the file:", count)
print("Total of all the numbers:", total)
print("Average:", average)
print("Highest number:", highest)
print("Lowest number:", lowest)
