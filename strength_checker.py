import pyfiglet
import re
text = "strength checker"
result = pyfiglet.figlet_format(text)
print(result)
def password_strength(password):
    if len(password) < 8:
        return "weak:- It should be at least 8 characters long."
    elif re.search(r"[a-z]", password) and re.search(r"[A-Z]", password) and re.search(r"\d", password) and re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password):
        return "strong:- Password is strong! Well done!"
    else:
        return "medium:- Password should contain special character, numbers, uppercase letter, lowercase letter"

#Input :
password = input("Enter a password: ")
print(f"Password strength: {password_strength(password)}")