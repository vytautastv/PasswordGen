import random
import string

def generate_password(length=12):
    """Generates a secure random password."""
    
    # Define possible characters: lowercase, uppercase, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the password has at least one character from each group
    password = [
        random.choice(string.ascii_lowercase),  # At least one lowercase letter
        random.choice(string.ascii_uppercase),  # At least one uppercase letter
        random.choice(string.digits),           # At least one digit
        random.choice(string.punctuation)       # At least one special character
    ]
    
    # Fill the rest of the password length with random characters from the full set
    password += random.choices(characters, k=length-4)
    
    # Shuffle the password list to prevent predictable patterns
    random.shuffle(password)
    
    # Join the list into a string and return the password
    return ''.join(password)

# Generate a password of desired length (default is 12 characters)
password = generate_password(16)  # You can change the number to any length you need
print(f"Generated Password: {password}")
