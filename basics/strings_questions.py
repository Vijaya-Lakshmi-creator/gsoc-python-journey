#  String length, uppercase, lowercase
s = input("Enter a string: ")
print("Length:", len(s))
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())


#  First and last character
print("First character:", s[0])
print("Last character:", s[-1])


#  Reverse a string
print("Reversed string:", s[::-1])


#  Palindrome check
rev = s[::-1]
if s == rev:
    print("Palindrome")
else:
    print("Not a palindrome")

