# Import necessary libraries
import string
import random
import tkinter as tk
from tkinter import messagebox
import pyperclip

# Function to generate a random password with specified criteria
def generate_password(password_length, include_digits=True, include_special_chars=True, include_uppercase=True, max_special_chars=2):
    characters = list(string.ascii_letters)

    # Include digits if specified
    if include_digits:
        characters.extend(string.digits)
    # Include special characters if specified
    if include_special_chars:
        characters.extend(string.punctuation)
    # Include uppercase letters if specified
    if include_uppercase:
        characters.extend(string.ascii_uppercase)

    # If special characters are included and their count is more than the allowed maximum,
    # remove extra special characters randomly
    if include_special_chars and characters.count(string.punctuation) > max_special_chars:
        characters = [char for char in characters if char not in string.punctuation]
        random.shuffle(characters)
        characters = characters[:max_special_chars]

    # Shuffle the characters for randomness
    random.shuffle(characters)

    # Initialize variables for password generation
    password = []
    special_char_count = 0

    # Generate the password character by character
    for x in range(password_length):
        char = random.choice(characters)
        # If the character is a special character, track its count
        if char in string.punctuation:
            special_char_count += 1
            # If the count exceeds the allowed maximum, skip the character
            if special_char_count > max_special_chars:
                continue
        password.append(char)

    # Shuffle the password for additional randomness
    random.shuffle(password)

    # Convert the password list to a string and return
    return "".join(password)

# Function to generate a pronounceable password
def generate_pronounceable_password(length=12):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    password = []

    # Generate the password alternating between consonants and vowels
    for i in range(length):
        if i % 2 == 0:
            password.append(random.choice(consonants))
        else:
            password.append(random.choice(vowels))

    # Convert the password list to a string and return
    return "".join(password)

# Function to handle the "Generate Password" button click
def generate_password_button_click():
    # Retrieve user input
    password_length = int(entry_password_length.get())
    include_digits = include_digits_var.get()
    include_special_chars = include_special_chars_var.get()
    include_uppercase = include_uppercase_var.get()

    # Generate the password based on user input
    if pronounceable_var.get():
        generated_password = generate_pronounceable_password(password_length)
    else:
        generated_password = generate_password(password_length, include_digits, include_special_chars, include_uppercase)

    # Calculate position for the message box
    window_x = window.winfo_x()
    window_y = window.winfo_y()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    pop_up_x = window_x + window_width // 2
    pop_up_y = window_y + window_height

    # Display the generated password in a message box
    messagebox.showinfo("Generated Password", generated_password, master=window)
    messagebox.geometry(f"+{pop_up_x}+{pop_up_y}")

    # Copy the password to the clipboard
    pyperclip.copy(generated_password)

    # Save the password to a file
    save_to_file(generated_password)

# Function to save the generated password to a file
def save_to_file(password):
    with open("generated_passwords.txt", "a") as file:
        file.write(password + "\n")

# Function to handle the "Generate with Custom Wordlist" button click
def generate_with_custom_wordlist():
    # Retrieve user input
    custom_wordlist = entry_custom_wordlist.get().split()
    if not custom_wordlist:
        messagebox.showwarning("Warning", "Custom wordlist is empty.")
        return

    password_length = int(entry_password_length.get())
    include_digits = include_digits_var.get()
    include_special_chars = include_special_chars_var.get()
    include_uppercase = include_uppercase_var.get()

    # Initialize characters based on user input
    characters = list(string.ascii_letters)
    if include_digits:
        characters.extend(string.digits)
    if include_special_chars:
        characters.extend(string.punctuation)
    if include_uppercase:
        characters.extend(string.ascii_uppercase)

    # Generate the password based on user input
    if pronounceable_var.get():
        generated_password = generate_pronounceable_password(password_length)
    else:
        generated_password = generate_password(password_length, include_digits, include_special_chars, include_uppercase)

    # Calculate position for the message box
    window_x = window.winfo_x()
    window_y = window.winfo_y()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    pop_up_x = window_x + window_width // 2
    pop_up_y = window_y + window_height

    # Display the generated password in a message box
    messagebox.showinfo("Generated Password", generated_password, master=window)
    messagebox.geometry(f"+{pop_up_x}+{pop_up_y}")

    # Copy the password to the clipboard
    pyperclip.copy(generated_password)

    # Save the password to a file
    save_to_file(generated_password)

# Function to exit the program
def exit_program():
    window.destroy()

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Get the screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the window size to full screen
window.geometry(f"{screen_width}x{screen_height}")

# Create and pack GUI elements
label_password_length = tk.Label(window, text="Password Length:")
label_password_length.pack()

entry_password_length = tk.Entry(window)
entry_password_length.pack()

include_digits_var = tk.IntVar()
include_digits_checkbox = tk.Checkbutton(window, text="Include Digits", variable=include_digits_var)
include_digits_checkbox.pack()

include_special_chars_var = tk.IntVar()
include_special_chars_checkbox = tk.Checkbutton(window, text="Include Special Characters", variable=include_special_chars_var)
include_special_chars_checkbox.pack()

include_uppercase_var = tk.IntVar()
include_uppercase_checkbox = tk.Checkbutton(window, text="Include Uppercase Letters", variable=include_uppercase_var)
include_uppercase_checkbox.pack()

pronounceable_var = tk.IntVar()
pronounceable_checkbox = tk.Checkbutton(window, text="Pronounceable Password", variable=pronounceable_var)
pronounceable_checkbox.pack()

label_custom_wordlist = tk.Label(window, text="Custom Wordlist (separated by spaces):")
label_custom_wordlist.pack()

entry_custom_wordlist = tk.Entry(window)
entry_custom_wordlist.pack()

generate_with_custom_wordlist_button = tk.Button(window, text="Generate with Custom Wordlist", command=generate_with_custom_wordlist)
generate_with_custom_wordlist_button.pack()

generate_button = tk.Button(window, text="Generate Password", command=generate_password_button_click)
generate_button.pack()

exit_button = tk.Button(window, text="Exit", command=exit_program)
exit_button.pack()

window.mainloop()
