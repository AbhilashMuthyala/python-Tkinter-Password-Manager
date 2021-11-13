from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]
    random.shuffle(password_list)
    final_password = ''.join([char for char in password_list])
    entry_password.delete(0, END)
    entry_password.insert(0, final_password)
    pyperclip.copy(final_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    user_entry = entry_website.get() + '|' + entry_email.get() + '|' + entry_password.get()
    print(len(entry_email.get()))
    if len(entry_email.get()) == 0 or len(entry_email.get()) == 0 or len(entry_email.get()) == 0:
        messagebox.showerror(title='Oops', message="Please enter all the fields")
    else:
        is_ok = messagebox.askokcancel(title=entry_website.get(), message=f"Please verify the below details \n email - {entry_email.get()} \n password - {entry_password.get()}")
        if is_ok:
            f = open("data.txt", "a")
            f.write(f"{user_entry}\n")
            f.close()
            clear_entries()

def clear_entries():
    entry_password.delete(0, END)
    entry_email.delete(0, END)
    entry_website.delete(0, END)
    entry_email.insert(0,'commonly used email')
    entry_website.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=30,pady=30)

canvas = Canvas(height=200,width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

label_website = Label(text='Website')
label_website.grid(row=2,column=0)

label_email = Label(text='Email/Username')
label_email.grid(row=3,column=0)

label_password = Label(text='Password')
label_password.grid(row=4,column=0)

entry_website = Entry(width=33)
entry_website.grid(row=2,column=1,columnspan=2)
entry_website.focus()

entry_email = Entry(width=33)
entry_email.grid(row=3,column=1,columnspan=2)
entry_email.insert(0,'commonly used email')

entry_password = Entry(width=20)
entry_password.grid(row=4,column=1)


button = Button(text="Generate password",command=generate_password)
button.grid(row=4,column=3)

button_add = Button(text="Add", width=30, command=save)
button_add.grid(row=5,column=1)

window.mainloop()
