# SetUp Commands
Configuration user information used accross all local repositories

git config --global user.name "github username"

git config --global user.email "valid-emailid"

# SETUP & INIT
Configuration user information, initialization and cloning repositories.

Inialize an existing directory as GIT Repository 
git init 

# Retrieve an entire repository from a hosted location via URL
git clone [url]


import random
import string
def generate_password():
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Generate Random Characters
    password = random.choice(uppercase_letters) \
               + random.choice(lowercase_letters) \
               + random.choice(digits) \
               + random.choice(special_characters)
    
    # Fill remaining characters
    remaining_length = 8 - len(password)
    
    for _ in range(remaining_length):
        password += random.choice(uppercase_letters + lowercase_letters + digits + special_characters)

    # shuffle password
    password_list = list(password)
    random.shuffle(password_list)

    password = ''.join(password_list)
    return password

print(generate_password())
