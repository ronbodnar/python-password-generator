import sys
import random
import string

def process_random_passwords():
    # Prompt user for number of passwords to generate
    num_passwords = prompt_user("How many passwords would you like to generate? (10-30):", [10, 30], "You must enter a number between 10 and 30.")
        
    passwords = []
    
    # Iterate through the number of passwords and generate a random password using random parameters
    for i in range(num_passwords):
        length = random.randrange(10, 20) # Select random length
        include_symbols = True if random.randrange(1, 4) == 1 else False # Randomly include symbols
        include_digits = True if random.randrange(1, 4) == 1 else False # Randomly include digits
        include_uppercase = True if random.randrange(1, 4) == 1 else False # Randomly include uppercase characters
        passwords.append(generate_password(length, include_uppercase, include_symbols, include_digits)) # Add the generated password to the passwords list
        
    # Output the number of generated passwords  
    print("Generated", len(passwords), "passwords:")
    
    # Iterate through the generated passwords and output them one by one  
    for i in range(len(passwords)):
        print(f"Password {i+1}:", passwords[i])


def process_single_password():
    # Prompt the user for the password length
    password_length = prompt_user("How many characters should the password be? (8-20):", [8, 20], "You must enter a number between 8 and 20.")
    
    # Prompt the user to determine whether uppercase characters should be used
    include_uppercase = prompt_user("Should the password include uppercase letters? (Y/N):", ["y", "n"], "You must enter y for yes or no for no.")
    
    # Prompt the user to determine whether digits should be used
    include_digits = prompt_user("Should the password include digits? (Y/N):", ["y", "n"], "You must enter y for yes or no for no.")
    
    # Prompt the user to determine whether symbols should be used
    include_symbols = prompt_user("Should the password include symbols? (Y/N):", ["y", "n"], "You must enter y for yes or no for no.")
        
    # Output the paramters used to generate the password
    print("Generated password with the following parameters:\n")
    print(f"Password length: {password_length}")
    print("Include uppercase letters: " + "Y" if include_uppercase is True else "N" + "")
    print("Include digits: " + "Y" if include_digits is True else "N" + "")
    print("Include symbols: " + "Y" if include_symbols is True else "N" + "")
    
    # Generate the password
    password = generate_password(password_length, include_uppercase, include_digits, include_symbols)
    
    # Output the generated password
    print("Generated Password: " + password)
    
def prompt_user(prompt_text, acceptable_inputs, error_text):
    # Continually listen for proper user input given specified acceptable inputs
    while True:
        try:
            # Ensure both types are equal, otherwise exit program
            if type(acceptable_inputs[0]) == type(acceptable_inputs[1]):
                # Conditionally handle when acceptable input is type of string
                if type(acceptable_inputs[0]) is str:
                    # Prompt user
                    response = input(prompt_text + " ")
                    
                    # Validate user input to listen for acceptable inputs, if input is not valid inform user and restart loop
                    if (acceptable_inputs[0] not in response.lower() and acceptable_inputs[1] not in response.lower()):
                        print(f"[INVALID INPUT] {error_text} {response} is not valid.\n")
                        continue
                    
                    # Return based on response
                    return True if "y" in response.lower() else False
                
                # Conditionally handle when acceptable input is type of integer
                elif type(acceptable_inputs[0]) is int:
                    # Prompt user
                    response = int(input(prompt_text + " "))
                    
                    # Validate user input to listen for acceptable integer inputs, if input is valid but out of range, inform user and restart loop.
                    if (response < acceptable_inputs[0] or response > acceptable_inputs[1]):
                        print(f"[INVALID INPUT] You must enter a number between {acceptable_inputs[0]} and {acceptable_inputs[1]}. {response} is out of range.\n")
                        continue
                    
                    # Return the user response
                    return response
                
                # If acceptable input list is not a string or integer, gracefully exit program
                else:
                    print("[INVALID INPUT] Acceptable input type not supported.");
                    sys.exit(1)
                    
            # If acceptable inputs are not of the same type, gracefully exit the program
            else:
                print("Type mismatch.")
                sys.exit(1)
        
        # If input is not of the same type requested, inform the user and prompt to re-enter their input
        except ValueError:
            print("[INVALID INPUT] " + error_text + "\n")
            continue
  
def generate_password(length, include_uppercase, include_symbols, include_digits):
    # Add all lowercase characters to the possible character string
    possible_chars = string.ascii_lowercase
    
    # If uppercase letters should be included, append them to the possible character string
    if include_uppercase:
        possible_chars += string.ascii_uppercase
    
    # If symbols should be included, append them to the possible character string    
    if include_symbols:
        possible_chars += string.punctuation
    
    # If digits should be included, append them to the possible character string    
    if include_digits:
        possible_chars += string.digits
        
    password = '';
    
    # Iterate over the specified password length
    for i in range(length):
        # Append a random character from the possible character string to the password string
        password += possible_chars[random.randrange(0, len(possible_chars))]
        
    # Return the generated password
    return password


# Begin the program by prompting the user to input their preferred password generation type
program_run_type = prompt_user("Would you like to generate a single password with options OR randomly generate multiple passwords?\n(1 = single password, 2 = multiple random passwords)", [1, 2], "You must enter a 1 to generate a single password or 2 to generate multiple random passwords.")

# Conditionally continue the program dependant on user input
if program_run_type == 1:
    process_single_password()
elif program_run_type == 2:
    process_random_passwords()
