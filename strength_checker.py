import pyfiglet
import re
text = "strength checker"
result = pyfiglet.figlet_format(text)
print(result)
def password_strength(password):
    if len(password) < 8:
        return "weak"
    elif re.search(r"[a-z]", password) and re.search(r"[A-Z]", password) and re.search(r"\d", password):
        return "strong"
    else:
        return "medium"

#Input :
password = input("Enter a password: ")
print(f"Password strength: {password_strength(password)}")