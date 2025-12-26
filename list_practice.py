
# PYTHON LIST PRACTICE


# Q1: Create a list of 5 integers and print it
a = [10, 20, 30, 40, 50]
print("Q1:", a)


# Q2: Print first and last element
print("Q2 First element:", a[0])
print("Q2 Last element:", a[-1])


# Q3: Change 3rd element to 100
a[2] = 100
print("Q3:", a)


# Q4: Length of the list
print("Q4 Length:", len(a))


# Q5: Print all elements using for loop
print("Q5 Elements:")
for i in a:
    print(i)


# MEDIUM QUESTIONS


# Q6: Print even numbers
print("Q6 Even numbers:")
for i in a:
    if i % 2 == 0:
        print(i)


# Q7: Reverse list using slicing
b = a[::-1]
print("Q7 Reversed list:", b)


# Q8: Sum of all elements using loop
total = 0
for i in a:
    total += i
print("Q8 Sum:", total)


# Q9: Maximum and Minimum
print("Q9 Max:", max(a))
print("Q9 Min:", min(a))


# Q10: Count frequency of a number
nums = [10, 20, 50, 30, 40, 20, 60, 30, 70, 80, 50, 40, 30]
key = int(input("Enter a number to count: "))
count = 0

for i in nums:
    if i == key:
        count += 1

print("Q10 Count:", count)


# MEDIUM – LOGIC QUESTIONS

# Q11: Remove duplicates from list
unique_nums = list(set(nums))
print("Q11 Unique elements:", unique_nums)


# Q12: Create list of only positive numbers
mixed = [-10, 20, -30, 40, 50, -5]
positive = []

for i in mixed:
    if i > 0:
        positive.append(i)

print("Q12 Positive numbers:", positive)
