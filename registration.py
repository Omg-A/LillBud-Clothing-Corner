import hashlib 
from tkinter import *
from firebase import firebase
import tkinter.messagebox as tkmb

firebase = firebase.FirebaseApplication("https://lillbud-clothing-corner-2-default-rtdb.firebaseio.com/", None)

registration_window = Tk()
registration_window.config(bg="SlateGray1")
registration_window.title("LillBud Clothing Corner")
registration_window.geometry("400x400")

login_username = ''
login_pasword = ''

def login_window():
    
    registration_window.destroy()
    login_window = Tk()
    login_window.title("LillBud Clothing Corner")
    login_window.config(bg="SlateGray1")
    login_window.geometry("400x400")
    
    log_heading_label = Label(login_window, text="Log In", font='arial 18 bold', bg="SlateGray1")
    log_heading_label.place(relx=0.5, rely=0.2, anchor=CENTER)
    
    login_username_label = Label(login_window, text="Username: ", font='arial 13', bg="SlateGray1")
    login_username_label.place(relx=0.3, rely=0.4, anchor=CENTER)
    
    login_username_entry = Entry(login_window)
    login_username_entry.place(relx=0.6, rely=0.4, anchor=CENTER)
    
    login_password_label = Label(login_window, text="Password: ", font='arial 13', bg="SlateGray1")
    login_password_label.place(relx=0.3, rely=0.5, anchor=CENTER)
    
    login_password_entry = Entry(login_window)
    login_password_entry.place(relx=0.6, rely=0.5, anchor=CENTER)
    
    btn_login = Button(login_window, text="Log In" , font='arial 13 bold' , command=login, relief=FLAT, bg="SteelBlue1")
    btn_login.place(relx=0.5, rely=0.65, anchor=CENTER)
    
    login_window.mainloop()

def register():
    username = username_entry.get()
    password = password_entry.get()
    encrypted = hashlib.md5(password.encode())
    hexd = encrypted.hexdigest()
    print("Hexadecimal format: ", hexd)
    put_data = firebase.put("/", username, hexd)

def login():
    global login_username
    global login_pasword
    login_username = login_username_entry.get()
    login_password = login_password_entry.get()
    encrypted = hashlib.md5(login_password.encode())
    hexd = encrypted.hexdigest()
    print("Hexadecimal format: ", hexd)
    get_password = firebase.get("/", login_username)
    if(get_password != None):
        if(get_password == hexd):
            tkmb.showinfo("Alert", "Successfully Logged In")
        else:
            tkmb.showinfo("Alert", "Passwordd or Username Is Incorrect")
    else:
        tkmb.showinfo("Alert", "Username not found")

heading_label = Label(registration_window, text="Sign Up", font='arial 18 bold', bg="SlateGray1")
heading_label.place(relx=0.5, rely=0.2, anchor=CENTER)

username_label = Label(registration_window, text="Username: ", font='arial 13', bg="SlateGray1")
username_label.place(relx=0.3, rely=0.4, anchor=CENTER)

username_entry = Entry(registration_window)
username_entry.place(relx=0.6, rely=0.4, anchor=CENTER)

password_label = Label(registration_window, text="Password: ", font='arial 13', bg="SlateGray1")
password_label.place(relx=0.3, rely=0.5, anchor=CENTER)

password_entry = Entry(registration_window)
password_entry.place(relx=0.6, rely=0.5, anchor=CENTER)

btn_reg = Button(registration_window, text="Sign Up" , font='arial 13 bold', command=register, relief=FLAT, padx=10, bg="SteelBlue1")
btn_reg.place(relx=0.5,rely=0.75, anchor=CENTER)

btn_login_window = Button(registration_window, text="Log In", font='arial 10 bold', command=login_window, relief=FLAT, bg="SteelBlue1")
btn_login_window.place(relx=0.9, rely=0.06, anchor=CENTER)

registration_window.mainloop()