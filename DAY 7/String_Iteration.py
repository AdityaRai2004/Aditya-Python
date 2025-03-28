def count_vowels(input_string):
    # Define the vowels
    vowels = "aeiouAEIOU"
    
    # Initialize a counter for vowels
    vowel_count = 0
    
    # Iterate through each character in the input string
    for char in input_string:
        if char in vowels:
            vowel_count += 1
            
    return vowel_count

# Get user input
user_input = input("Enter a string: ")
# Count the vowels in the input string
vowel_count = count_vowels(user_input)

# Display the result
print(f"The number of vowels in the string is: {vowel_count}")
