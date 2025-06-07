import tkinter
from tkinter import messagebox
import string
import random
import pyperclip
import json

def generate_random_password():
    """
    Generates and returns a random password
    """
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    n_letters = random.randint(8, 10)
    n_numbers = random.randint(2, 4)
    n_symbols = random.randint(2, 4)

    total_length = n_letters + n_numbers + n_symbols
    password_characters = []

    for index in range(0, total_length):
        options = []
        if n_letters > 0:
            options.append(0)
        if n_numbers > 0:
            options.append(1)
        if n_symbols > 0:
            options.append(2)

        random_type = random.choice(options)

        if random_type == 0:
            password_characters.append(random.choice(letters))
            n_letters -= 1
        if random_type == 1:
            password_characters.append(random.choice(numbers))
            n_numbers -= 1
        if random_type == 2:
            password_characters.append(random.choice(symbols))
            n_symbols -= 1

    password = ''.join(password_characters)
    return password


def create_password():
    """
    Creates a random password, inserts it into a passoword field, and copies it to the clibboard
    """
    random_password = generate_random_password()
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, random_password)
    pyperclip.copy(random_password)


def store_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty")
    else:
        # Save credentials to a file
        try:
            with open("passwords.json", "r") as file:
                # Read old data
                json_data = json.load(file)
        except FileNotFoundError:
            # If file does not exist - we will save just new data
            json_data = new_data
        else:
            # Update old data with new data
            json_data.update(new_data)
        finally:
            # Save json data
            with open("passwords.json", "w") as file:
                json.dump(json_data, file, indent=4)

            # Clear fields
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)


def search_password():
    website = website_entry.get().lower()

    try:
        with open("passwords.json", "r") as file:
            json_data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Data file not found :(")
    else:
        if website in json_data:
            email = json_data[website]["email"]
            password = json_data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showerror(title="Oops", message=f"No data found for the website {website}")



window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
logo_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = tkinter.Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = tkinter.Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(tkinter.END, "myemail@example.com")

password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
btn_search = tkinter.Button(text="Search", width=13, command=search_password)
btn_search.grid(row=1, column=2)

btn_generate_password = tkinter.Button(text="Generate Password", command=create_password)
btn_generate_password.grid(row=3, column=2)

btn_store = tkinter.Button(text="Add / Store", width=36, command=store_data)
btn_store.grid(row=4, column=1, columnspan=2)

window.mainloop()
