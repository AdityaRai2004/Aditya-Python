def classify_password(password):
    
    length = len(password)
    has_lowercase = any(char.islower() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password)

    conditions_met = sum([has_lowercase, has_uppercase, has_digit, has_special])

    if length < 8 or conditions_met < 2:
        return "Weak"
    elif conditions_met >= 2 and length >= 8:
        return "Medium"
    elif length >= 12 and has_lowercase and has_uppercase and has_digit and has_special:
        return "Strong"
    else:
        return "Medium"

def main():
    while True:
        password = input("Enter a password: ")
        classification = classify_password(password)
        print(f"Classified as: {classification}")
        
        if classification == "Strong":
            print("You've entered a Strong password.")
            break
        else:
            print("Please try again.")

if __name__ == "__main__":
    main()
