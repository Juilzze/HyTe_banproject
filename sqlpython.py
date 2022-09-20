import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    username="test",
    password="test",
    database="bans_2022"
)

mydb.autocommit = True
mycursor = mydb.cursor()

from tkinter import *

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global key
    global username_entry
    global password_entry
    global key_entry
    global admincheck
    username = StringVar()
    password = StringVar()
    key = StringVar()
    admincheck = IntVar()

    Label(register_screen, text="Register", bg="white").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    key_lable = Label(register_screen, text="Key * ")
    key_lable.pack()
    key_entry = Entry(register_screen, textvariable=key, show='*')
    key_entry.pack()
    admincheck_entry = Checkbutton(register_screen, text="Admin", variable=admincheck, onvalue=1, offvalue=0)
    admincheck_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="green", command = 
register_user).pack()


def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("1920x1080")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
    

def register_user():
    nextstep = False
    username_info = username.get()
    password_info = password.get()
    key_info = key.get()
    admincheck_info = admincheck.get()
    print(username_info)

    namecheck = (f"SELECT username FROM users WHERE users.username = '{username_info}'")
    mycursor.execute(namecheck)
    myresult = mycursor.fetchall()
    print(myresult)
    for x in myresult:
        if username_info in x:
            Label(register_screen, text=f"There is already user: {username_info}", fg="red", font=("calibri", 11)).pack()

    for x in myresult:
        print(x)
        if username_info not in x:
            nextstep = True
            print("test")
            
    if nextstep == True or not myresult:
        if key_info == "123":
            print(username_info, password_info, admincheck_info)
            sql = f"INSERT INTO users (username, pass, admin) VALUES ('{username_info}', '{password_info}', {admincheck_info})"
            mycursor.execute(sql)
            Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
            

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    namecheck = (f"SELECT username FROM users WHERE users.username = '{username1}'")
    passcheck = (f"SELECT pass FROM users WHERE users.username = '{username1}'")
    print(namecheck)
    mycursor.execute(namecheck)
    myresult = mycursor.fetchall()
    mycursor.execute(passcheck)
    myresult2 = mycursor.fetchall()
    logincode1 = False
    logincode2 = False

    for x in myresult:
        if username1 in x:
            logincode1 = True
    for x in myresult2:
        if password1 in x:
            logincode2 = True

    if logincode1 == True and logincode2 == True:
        login_sucess()
        Label(login_screen, text="Login success", fg="green", font=("calibri", 11)).pack()
    elif logincode1 != True or logincode2 != True:
        Label(login_screen, text="Login failed", fg="red", font=("calibri", 11)).pack()


def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

def delete_login_success():
    login_success_screen.destroy()

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Login/Register")
    Label(text="Login/Register", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()