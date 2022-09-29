import mysql.connector
from tkinter import *
from datetime import date, datetime, timedelta
from tkinter.ttk import Combobox

##
## Connecting Python to MySQL server
##

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="test",
    password="test",
    database="bans_2022"
)

mydb.autocommit = True
mycursor = mydb.cursor()

##
## User register screen (Tkinter) and functions
##

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.state('zoomed')
    register_screen.title("Register")
    register_screen.geometry("1920x1080")

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

    Label(register_screen, text="Register").pack()
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
    Button(register_screen, text="Register", width=10, height=1, command = 
register_user).pack()


def register_user():
    nextstep = False
    username_info = username.get()
    password_info = password.get()
    key_info = key.get()
    admincheck_info = admincheck.get()

    namecheck = (f"SELECT username FROM users WHERE users.username = '{username_info}'")
    mycursor.execute(namecheck)
    myresult = mycursor.fetchall()

    if len(username_info) >= 3 and len(password_info) >= 3:

        for x in myresult:
            if username_info in x:
                Label(register_screen, text=f"There is already user: {username_info}", fg="red", font=("calibri", 11)).pack()
    
        for x in myresult:
            if username_info not in x:
                nextstep = True
                
        if nextstep == True or not myresult:
            if key_info == "123":
                sql = f"INSERT INTO users (username, pass, admin) VALUES ('{username_info}', '{password_info}', {admincheck_info})"
                mycursor.execute(sql)
                Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
            else:
                Label(register_screen, text="Wrong key", fg="red", font=("calibri", 11)).pack()
    else:
        Label(register_screen, text="Your username or password is too short minium is 3 letter", fg="red", font=("calibri", 11)).pack()
            

##
## User login screen (Tkinter) and functions
##


def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.state('zoomed')
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

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    logincheck = (f"SELECT username FROM users WHERE users.username = '{username1}' and users.pass = '{password1}'")
    mycursor.execute(logincheck)
    myresult = mycursor.fetchall()
    loginverify = False

    for x in myresult:
        if username1 in x:
            loginverify = True

    if loginverify == True:
        main_screen.destroy()
        admincheck = (f"SELECT admin FROM users WHERE users.username = '{username1}'")
        mycursor.execute(admincheck)
        myresult2 = mycursor.fetchall()
        for i in myresult2:
            if 0 in i:
                user_view()
            elif 1 in i:
                admin_view()
    else:
        Label(login_screen, text="Login failed", fg="red", font=("calibri", 11)).pack()


##
## Tkinter screens
##

    
def user_view():
    global user_view
    user_view = Tk()
    user_view.state('zoomed')
    user_view.geometry("1920x1080")
    user_view.title("Select")
    Label(text="Select", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Banlist", height="2", width="30", command=banlist).pack()
    Label(text="").pack()
    Button(text="Warnlist", height="2", width="30", command=warnlist).pack()

def admin_view():
    global admin_view
    admin_view = Tk()
    admin_view.state('zoomed')
    admin_view.geometry("1920x1080")
    admin_view.title("Select")
    Label(text="Select", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Banlist", height="2", width="30", command=banlist).pack()
    Label(text="").pack()
    Button(text="Warnlist", height="2", width="30", command=warnlist).pack()
    Label(text="").pack()
    Button(text="Give warn", height="2", width="30", command=warn_screen).pack()
    Label(text="").pack()
    Button(text="Give ban", height="2", width="30", command=ban_screen).pack()


def banlist():
    banlist = Tk()
    banlist.state('zoomed')
    banlist.geometry("1920x1080") 

    mycursor.execute("SELECT * FROM bans")
    i=0 
    for bans in mycursor: 
        for j in range(len(bans)):
            e = Entry(banlist, width=10) 
            e.grid(row=i, column=j) 
            e.insert(END, bans[j])
        i=i+1

def warnlist():
    warnlist = Tk()
    warnlist.state('zoomed')
    warnlist.geometry("1920x1080") 

    mycursor.execute("SELECT * FROM warns")
    i=0 
    for warns in mycursor: 
        for j in range(len(warns)):
            e = Entry(warnlist, width=10) 
            e.grid(row=i, column=j) 
            e.insert(END, warns[j])
        i=i+1


def ban_screen():
    global ban_screen
    ban_screen = Tk()
    ban_screen.state('zoomed')
    ban_screen.title("Ban user")
    ban_screen.geometry("1920x1080")
    Label(ban_screen, text="Enter ban details").pack()
    Label(ban_screen, text="").pack()

    global username_ban
    global ban_time
    global ban_reason
    global selected_text
    global cb
    global var
    global lb
    var = StringVar()
    username_ban = StringVar()
    ban_time = IntVar()
    ban_reason = StringVar()
    selected_text = StringVar()
    global username_ban_entry
    global ban_time_entry
    global ban_reason_entry
    allusers = (f"SELECT users.username FROM users")
    mycursor.execute(allusers)
    myresult = mycursor.fetchall()

    Label(ban_screen, text="Username * ").pack()
    data=(myresult)
    
    cb=Combobox(ban_screen, values=data, width=30)
    cb.current(0)
    cb.pack()

    Label(ban_screen, text="").pack()
    Label(ban_screen, text="Time (days) *").pack()
    ban_time_entry = Entry(ban_screen, textvariable=ban_time)
    ban_time_entry.pack()
    Label(ban_screen, text="").pack()
    Label(ban_screen, text="Reason *").pack()
    ban_reason_entry = Entry(ban_screen, textvariable=ban_reason)
    ban_reason_entry.pack()
    Label(ban_screen, text="").pack()
    Button(ban_screen, text="Ban", width=10, height=1, command = ban_user).pack()

def ban_user():
    isint = ban_time_entry.get()
    if isint.isnumeric():
        time_info = int(ban_time_entry.get())
        reason_info = ban_reason_entry.get()
        username_info = cb.get()
        username = (f"SELECT username FROM users WHERE users.username = '{username_info}'")
        mycursor.execute(username)
        myresult = mycursor.fetchall()
        if myresult:
            for i in myresult:
                if username_info in i:
                    Label(ban_screen, text=f"User: {username_info} has been banned", fg="green", font=("calibri", 11)).pack()
                    today = date.today()
                    enddate = today + timedelta(days=int(time_info))
                    sql = f"INSERT INTO bans (username, reason, date, enddate) VALUES ('{username_info}', '{reason_info}', '{today}', '{enddate}')"
                    mycursor.execute(sql) 
        else:
            Label(ban_screen, text=f"User: {username_info} not found ", fg="red", font=("calibri", 11)).pack()
    else:
        Label(ban_screen, text=f"Time must be in integer form. Example: '1'", fg="red", font=("calibri", 11)).pack()



def warn_user():
    willbebanned = False
    reason_info = warn_reason_entry.get()
    username_info = cb2.get()

    x = 0
    timeswarned = (f"SELECT username FROM warns WHERE warns.username = '{username_info}'")
    mycursor.execute(timeswarned)
    myresult2 = mycursor.fetchall()

    if myresult2:
        for i in myresult2:
            x = x + 1
            if x >= 3:
                willbebanned = True

    if willbebanned == False:
        username = (f"SELECT username FROM users WHERE users.username = '{username_info}'")
        mycursor.execute(username)
        myresult = mycursor.fetchall()
    
        if myresult:
            for i in myresult:
                if username_info in i:
                    today = date.today()
                    Label(warn_screen, text=f"User: {username_info} has been warned", fg="green", font=("calibri", 11)).pack()
                    sql = f"INSERT INTO warns (username, reason, date) VALUES ('{username_info}', '{reason_info}', '{today}')"
                    mycursor.execute(sql) 
        else:
            Label(warn_screen, text=f"User: {username_info} not found ", fg="red", font=("calibri", 11)).pack()
    elif willbebanned == True:
        today = date.today()
        enddate = today + timedelta(days=7)
        reason_info = "Too many warnings"
        sql = f"INSERT INTO bans (username, reason, date, enddate) VALUES ('{username_info}', '{reason_info}', '{today}', '{enddate}')"
        mycursor.execute(sql) 
        Label(warn_screen, text=f"User: {username_info} had too many warnings and is now banned for 7 days", fg="green", font=("calibri", 11)).pack()


def warn_screen():
    global warn_screen
    global cb2
    warn_screen = Tk()
    warn_screen.state('zoomed')
    warn_screen.title("Warn user")
    warn_screen.geometry("1920x1080")
    Label(warn_screen, text="Enter warn details").pack()
    Label(warn_screen, text="").pack()

    global username_verify3
    global warn_reason
    username_verify3 = StringVar()
    warn_reason = StringVar()
    global username_warn_entry
    global warn_reason_entry

    allusers = (f"SELECT users.username FROM users")
    mycursor.execute(allusers)
    myresult = mycursor.fetchall()

    Label(warn_screen, text="Username * ").pack()
    data=(myresult)
    
    cb2=Combobox(warn_screen, values=data, width=30)
    cb2.current(0)
    cb2.pack()
    
    Label(warn_screen, text="").pack()
    Label(warn_screen, text="Reason *").pack()
    warn_reason_entry = Entry(warn_screen, textvariable=warn_reason)
    warn_reason_entry.pack()
    Label(warn_screen, text="").pack()
    Button(warn_screen, text="Warn", width=10, height=1, command = warn_user).pack()


def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.state('zoomed')
    main_screen.geometry("1920x1080")
    main_screen.title("Login/Register")
    Label(text="Login/Register", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
    main_screen.mainloop()

main_account_screen()
