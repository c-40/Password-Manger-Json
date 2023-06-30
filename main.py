from tkinter import *
from tkinter import messagebox
import  Pass


def login():
    username = entry_username.get()
    password = entry_password.get()

    # Check if the username and password are correct
    if username == "admin" and password == "1234":
        window1.destroy()
        open_password_manager()
    else:
        messagebox.showerror("Error", "Invalid username or password")
def open_password_manager():
    Pass.win()








window1 = Tk()
window1.title("Login")
window1.config(padx=100,pady=100)
# Add the required UI elements for the login window
label_username = Label(window1, text="Username:")
label_username.grid(row=0, column=0)

entry_username = Entry(window1)
entry_username.grid(row=0, column=1)

label_password = Label(window1, text="Password:")
label_password.grid(row=1, column=0)

entry_password = Entry(window1, show="*")
entry_password.grid(row=1, column=1)

button_login = Button(window1, text="Login", command=login)
button_login.grid(row=2, columnspan=2)

window1.mainloop()

