from tkinter import *
from tkinter import messagebox
import time
import json

FONT = ("Arial", 12, "bold")
BEIGE = "#FFFADD"
logged_in = False

with open("total_users.txt", "r") as data_file:
    data = data_file.read()
    total_users = int(data)
    print(total_users)

#--------------------------UI------------------------------#
def login_screen():

    def signup():
        global total_users
        new_user = username_entry.get()
        new_pass = password_entry.get()

        new_user_data = {
            f"{total_users}": {
                "Username": new_user,
                "Name": "",
                "Password": new_pass,
                }
        }

        valid_user = False

        with open("data.json", "r") as data:
            read_data = json.load(data)
            print(read_data)
            if read_data[total_users]["Username"].lower() == new_user.lower():
                messagebox.showerror(title="Error", message=f"The username: {new_user} is already in use.\n Please enter another username.")
            else:
                valid_user = True
        
        if valid_user == True and len(new_pass) >= 4:
            is_ok = messagebox.askyesno(title="User Info", message=f"Username: {new_user}\nPassword: {new_pass}\n\nDoes this look correct?")

            if is_ok == True:
                total_users += 1
                with open("total_users.txt", "w") as data_file:
                    data_file.write(f"{total_users}")
                    print(total_users)


                with open("data.json", "w") as data:
                    json.dump(new_user_data, data, indent=3)
                
                username_entry.delete(0, END)
                password_entry.delete(0, END)
        elif len(new_pass) < 4 and new_user != "":
            messagebox.showerror(title="Password Error", message="Please make sure password is atleast 4 characters long.")
        else:
            messagebox.showerror(title="Error", message="Please enter a valid Username and Password.")

    def login():
        global logged_in
        username = username_entry.get()
        password = password_entry.get()
        valid_user = False
        valid_pass = False

        with open("data.json", "r") as data:
            read_data = json.load(data)
            if read_data["Username"] == username:
                valid_user = True
            if read_data["Password"] == password:
                valid_pass = True

        if valid_pass == True and valid_user == True:
            print("Logged In")
            logged_in = True
            window.destroy()
        else:
            messagebox.showerror(title="Wrong Info", message="Please Enter Valid Username and Password.")


    #Window
    window = Tk()
    window.title("Expense Tracker")
    window.minsize(width=417, height=525)
    window.config(bg=BEIGE, padx=20, pady=10)
    window.eval('tk::PlaceWindow . center')

    #Labels
    username_label = Label(text="Username: ", font=FONT, bg=BEIGE)
    username_label.grid(column=1, row=1)
    password_label = Label(text="Password:", font=FONT, bg=BEIGE)
    password_label.grid(column=1, row=2)

    #Buttons
    login_button = Button(text="Login", width=15, command=login)
    login_button.config(pady=5)
    login_button.grid(column=1, row=3)
    signup_button = Button(text="Sign Up", width=15, command=signup)
    signup_button.config(pady=5)
    signup_button.grid(column=2, row=3)

    #Entries
    username_entry = Entry(width=40)
    username_entry.grid(column=2, row=1)
    username_entry.focus()
    password_entry = Entry(width=40)
    password_entry.grid(column=2, row=2)

    #Canvas
    canvas = Canvas(width=417, height=425, highlightthickness=0)
    bg_image = PhotoImage(file="C:\\Users\\Yungstaz\\Documents\\Projects\\Expense Tracker\\img\\login_screen.png")
    canvas.create_image(208, 212, image=bg_image)
    canvas.grid(column=0, row=0, columnspan=4)

    window.mainloop()

def profile_screen():
    window = Tk()
    window.title("Expense Tracker")
    window.minsize(width=417, height=525)
    window.config(bg=BEIGE, padx=20, pady=10)
    window.geometry("600x250")
    window.eval('tk::PlaceWindow . center')

    window.mainloop()

if __name__ == "__main__":
    login_screen()
    if logged_in == True:
        print("Loading")
        profile_screen()

