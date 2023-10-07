from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
import random

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    password_input.delete(0, END)
    password_input.insert(0, f"{password}")
    password_input.clipboard_clear()
    password_input.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    web = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if web != "" and email != "" and password != "":
        messagebox.askokcancel(title=web, message=f"There are the details entered: \nEmail: {email}"
                                                  f"\nPassword: {password} \nIs it ok to save?")
        with open("data.txt", "a") as file:
            file.write(f"{web} | {email} | {password}\n")
        website_input.delete(0, END)
        password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# canvas
canvas = Canvas(width=200, height=223, highlightthickness=0)
imagine = PhotoImage(file="logo.png")
canvas.create_image(100, 89, image=imagine)
canvas.grid(row=0, column=1)

# labels
website = Label(text="Website:", font=("Comis Sans", 12))
website.grid(column=0, row=1, sticky="w")
email = Label(text="Email/Username:", font=("Comis Sans", 12))
email.grid(column=0, row=2, sticky="w")
Password = Label(text="Password:", font=("Comis Sans", 12))
Password.grid(column=0, row=3, sticky="w")

# text inputs
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2, sticky="w", padx=5)
website_input.focus()
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky="w", padx=5)
email_input.insert(END,"email@gmail.com")
password_input = Entry(width=28)
password_input.grid(column=1, row=3, sticky="w", padx=5)

# buttons
password_generate_button = Button(text="Generate Password", command=password_generator)
password_generate_button.grid(column=2,row=3)
add_button = Button(text="Add",width=36,command=save_data)
add_button.grid(column=1,row=4,columnspan=2)


window.mainloop()
