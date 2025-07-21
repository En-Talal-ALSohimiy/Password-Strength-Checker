import re

def check_password(password):
    if len(password) < 8:
        return "Password is too short (minimum 8 characters)."
    if not re.search(r"\d", password):
        return "Password must include at least one number."
    if not re.search(r"[A-Z]", password):
        return "Password must include at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return "Password must include at least one lowercase letter."
    if not re.search(r"[!@#$%^&*()_+]", password):
        return "Password must include at least one special character (!@#$%^&*()_+)."
    return "Strong password 👍"

if __name__ == "__main__":
    pwd = input("Enter password to check: ")
    result = check_password(pwd)
    print(result)
