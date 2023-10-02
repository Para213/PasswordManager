import tkinter
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    web = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if web != "" and email != "" and password != "":
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
password_generate_button = Button(text="Generate Password")
password_generate_button.grid(column=2,row=3)
add_button = Button(text="Add",width=36,command=save_data)
add_button.grid(column=1,row=4,columnspan=2)


window.mainloop()
