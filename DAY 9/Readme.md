Problem 1: Bank Loan Eligibility System
Objective
To create a program that determines if a user is eligible for a bank loan based on their age, salary, and credit score.

Approach
Input: User provides their age, salary, and credit score.

Logic:

Check if the user's age is between 21 and 60.

If the salary is greater than or equal to ₹20,000.

If the credit score is greater than or equal to 650.

Output: Based on the conditions, return either "Loan Approved" or specific reasons for denial.

Nested Conditionals: Used to evaluate eligibility step-by-step.

Code Comments
python
# Check if age is within the eligible range
if 21 <= age <= 60:
    # Check if salary meets the minimum requirement
    if salary >= 20000:
        # Check if credit score meets the threshold
        if credit_score >= 650:
            return "Loan Approved!"
        else:
            return "Loan Denied: Low Credit Score."
    else:
        return "Loan Denied."
else:
    return "Age not within eligible range."
Problem 2: AI Chatbot with Conditional Responses
Objective
To design a chatbot that responds based on user input (greetings, farewells, or general queries).

Approach
Input: User types a message.

Logic:

Use predefined lists (greetings and farewells) to match user input.

Use conditionals to handle specific phrases like "how are you" or "your name."

Output: Chatbot responds appropriately or asks for clarification.

Loop: Keeps running until the user types "bye."

Code Comments
python
# Match user input with predefined greetings
if userinput in greetings:
    return "Hello! How can I assist you today?"

# Match user input with predefined farewells
if userinput in farewells:
    return "Goodbye! Have a great day!"

# Handle specific queries
if "how are you" in userinput:
    return "I'm just a bot, but I'm doing great! How about you?"
Problem 3: Traffic Light Simulation
Objective
Simulate a traffic light system that cycles through RED, YELLOW, and GREEN lights.

Approach
Logic:

Use a list of tuples (lights) containing light colors and their durations.

Loop through the list indefinitely using while True.

Use time.sleep() to simulate waiting for each light's duration.

Output: Display the current light and its duration.

Code Comments
python
# Define traffic light sequence with durations
lights = [("RED", 5), ("YELLOW", 2), ("GREEN", 5)]

# Infinite loop to simulate traffic light cycling
while True:
    for light, duration in lights:
        print(f"{light} - Wait for {duration} seconds")
        time.sleep(duration)  # Pause execution for the specified duration
Problem 4: Smart Home Automation
Objective
To implement a smart home system that controls fans, dehumidifiers, and lights based on temperature, humidity, and motion detection.

Approach
Input: User provides temperature (°C), humidity (%), and motion detection status.

Logic:

Turn on/off fans based on temperature threshold (30°C).

Turn on/off dehumidifiers based on humidity threshold (70%).

Turn on/off lights based on motion detection.

Output: Display the status of each appliance.

Code Comments
python
# Turn fan ON/OFF based on temperature
if temp > 30:
    fan = "ON"
else:
    fan = "OFF"

# Turn dehumidifier ON/OFF based on humidity
if humidity > 70:
    dehumidifier = "ON"
else:
    dehumidifier = "OFF"

# Turn lights ON/OFF based on motion detection
if motion:
    light = "ON"
else:
    light = "OFF"
Problem 5: Password Strength Checker
Objective
Classify passwords as "Weak," "Medium," or "Strong" based on their characteristics.

Approach
Input: User provides a password.

Logic:

Check for length, presence of lowercase/uppercase letters, digits, and special characters.

Classify passwords based on conditions met.

Output: Display password strength classification.

Code Comments
python
# Check password characteristics
has_lowercase = any(char.islower() for char in password)
has_uppercase = any(char.isupper() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password)

# Classify password strength based on conditions met
if length < 8 or conditions_met < 2:
    return "Weak"
elif conditions_met >= 2 and length >= 8:
    return "Medium"
elif length >= 12 and has_lowercase and has_uppercase and has_digit and has_special:
    return "Strong"
Problem 6: Banking System with ATM Functionality
Objective
Simulate an ATM system where users can check balance, deposit money, withdraw money, or exit.

Approach
Initial Balance: Set to ₹1000.

Logic:

Provide options (check balance, deposit, withdraw, exit).

Update balance based on deposit/withdrawal amounts.

Output: Display updated balance or appropriate messages (e.g., insufficient funds).

Code Comments
python
# Check balance option

if choice == "1":
    print(f"\nYour current balance is: {balance}")

# Deposit money option

elif choice == "2":
    deposit = float(input("Enter deposit amount: ₹"))
    if deposit > 0:
        balance += deposit

# Withdraw money option

elif choice == "3":
    withdrawal = float(input("Enter withdrawal amount: "))
    if withdrawal > balance:
        print("\nInsufficient balance!")

This set of problems demonstrates practical use cases of conditionals and loops in Python. Each problem is implemented with clear logic and appropriate comments to ensure readability and maintainability.