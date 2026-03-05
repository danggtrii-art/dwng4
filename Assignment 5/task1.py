import re
code = input("Enter course code: ")
pattern = r'^[A-Z]{2,3}\d{3}$'
if re.fullmatch(pattern, code):
    print("Valid course code")
else:
    print("Invalid course code")