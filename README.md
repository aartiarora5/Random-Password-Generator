# Password Generator

## Overview

Using the Tkinter toolkit, this Python script creates a straightforward GUI application for creating passwords. Users can create random passwords using this application by giving it several parameters to work with, like length, number inclusion, special characters, and capital letters. Pronounceable password generators are another option available to users.

## Features

1. **Random Password Generation**:  Users can create passwords at random that meet predetermined requirements, such as being at least one digit, contain special characters, and all capital letters.
   
2. **Pronounceable Passwords**: By switching between vowels and consonants, users can create pronounceable passwords.

3. **Custom Wordlist**: This feature gives users flexibility when creating passwords by allowing them to use a custom wordlist.

4. **Clipboard Copy**: For convenience, the generated password is copied to the clipboard.

5. **Logging Passwords**: A text file called `generated_passwords.txt} contains the generated passwords.

## How to Use

1. **Password Length**: Fill in the "Password Length" field with the desired password length.

2. **Incorporate Choices**:

   - To add numerical digits to the password, check the "Include Digits" box.

   - To add special characters to the password, check the "Include Special Characters" box.

   - To add capital letters to the password, check the "Include Uppercase Letters" box.

3. **Pronounceable Passwords**: To create a password that alternates between consonants and vowels, check the "Pronounceable Password" box.

4. **Custom Wordlist**: To create passwords based on particular words, you can optionally supply a custom wordlist that is divided by spaces.

5. **Elements**:

   Select "Generate Password" to create a password according to the given parameters.

   - To create a password using the custom wordlist, click "Generate with Custom Wordlist".

   - To exit the application, click "Exit".

## Dependencies

- Python 3.x

- Tkinter library (part of the standard Python distribution) 

## How to Run

1. Verify that Python is installed on your computer.

2. Open your terminal or command prompt and type the following command to launch the script:
    {{bash} python password_generator.py





