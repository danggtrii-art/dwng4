import re
color = input("Enter hex color: ")
pattern = r'^#[0-9A-Fa-f]{6}$'
if re.fullmatch(pattern, color):
    print("Valid hex color")
else:
    print("Invalid hex color")