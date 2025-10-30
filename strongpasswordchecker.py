import re

def check_password_strength(password):
    # Initialize strength score
    strength = 0
    remarks = ""

    # Criteria checks
    if len(password) < 8:
        remarks = "Password too short. Minimum 8 characters required."
    else:
        strength += 1

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks += "\nAdd at least one lowercase letter."

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks += "\nAdd at least one uppercase letter."

    if re.search(r"\d", password):
        strength += 1
    else:
        remarks += "\nAdd at least one number."

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks += "\nAdd at least one special character."

    # Strength rating
    if strength == 5:
        rating = "Strong 💪"
    elif 3 <= strength < 5:
        rating = "Moderate ⚠️"
    else:
        rating = "Weak ❌"

    print(f"\nPassword Strength: {rating}")
    if remarks:
        print("Suggestions to improve:", remarks)


# Run the program
if __name__ == "__main__":
    print("🔐 Strong Password Checker 🔐")
    user_password = input("Enter your password to check: ")
    check_password_strength(user_password)
