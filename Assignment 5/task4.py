import re
text = "You may reach Mr. Đăng through his office number: +842439999999 during work hours, or his cell phone number: 0987654321,"
pattern = r'\+84\d+|\d{10}'
result = re.sub(pattern, "[REDACTED}", text)
print(result)