import re
text = input("Enter a paragraph: ")
numbers = re.findall(r'\d+', text)
total = 0
for n in numbers:
    total += int(n)
print("Sum of numbers:", total)