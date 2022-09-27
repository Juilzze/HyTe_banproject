# HyTe_banproject

**HyTe_banproject**

Hello, this is my school project which is simple ban control software made with Python (Tkinter) and MySQL. To setup this software you'll have to follow these simple steps. Lets begin!

<h2>1.1</h2>

**You have to download these softwares to your computer:**
  
  XAMPP control panel: https://www.apachefriends.org/
  
  HeidiSQL: https://www.heidisql.com/download.php
  
  Python: https://www.python.org/downloads/

<h2>1.2</h2>

Now when you have donwloaded following softwares, lets setup XAMPP control panel!
Open "xampp-windows-x64-8.1.6-0-VS16-installer" follow its instructions. When it asks which components you want to donwload, choose all of them. Press next and begin the download.

<h2>1.3</h2>

After XAMPP Control Panel have been succesfully installed you should see this screen:

Press start on MySQL And Apache

![alt text](https://i.imgur.com/pI2MXzR.png)

After MySQL and Apache is succesfully started then open HeidiSQL, go to step 2.1
(If MySQL or Apache servers started properly skip part 1.4)

<h2>1.4</h2>
Fix solution for server starting problems

- Run XAMPP Control Panel as adminstrator and then start MySQL and Apache
If it still didnt work, press config and choose "Apache (httpd.conf)"

![alt text](https://i.imgur.com/o3Q3DrB.png)

Press (CTRL + H) and change default port from 80 to 3344
![alt text](https://i.imgur.com/ONPWuxE.png)
If you cannot edit the file you must use adminstrator permissions.
Now Your servers should work

<h2>2.1</h2>

Connect to your database with HeidiSQL. Press "New", select library: "libmysql.dll", press open:

![alt text](https://i.imgur.com/Eejp9cH.png)
![alt text](https://i.imgur.com/fTovEb5.png)

Press "Query" and copy bansql.sql file from this reporisity. Paste it to Query and press F9 to run it, now your database is done. You will see the tables after you have restarted HeidiSQL.
![alt text](https://i.imgur.com/mtuFFfr.png)

These tables should show up after you reopened HeidiSQL

![alt text](https://i.imgur.com/Ie2XBuO.png)

<h2>3.1</h2>

**Next lets connect python code to MySQL!**
Open CMD and Run these commands:

pip3 install mysql-connector

pip3 install mysql-connector-python==8.0.29

pip install pymysql

pip install mysql

after you have succesfully ran these commands, you'll have to create user for your sql server.

<h2>3.2</h2>

Open this web url on your browser: http://localhost/phpmyadmin/ (NOTE: if you did step 1.4 the url is http://localhost:4433/phpmyadmin/)
This kind of view should pop up. Next you'll have to press users and create user for your database, since we don't want to use default root user. Then press "Add user account"
![alt text](https://i.imgur.com/MLzKpbA.png)

Create username and password for your account (You should write them down). On "Hostname" choose "localhost"
![alt text](https://i.imgur.com/vPgPAE5.png)
Enable all permissions for your user. After that press create button on left bottom corner.
![alt text](https://i.imgur.com/Gwe3Tbn.png)

<h2>3.3</h2>

Open your python idle software and create new file.

Copy this text to your python file to see if mysql connection works. Change "YourUserName" to username and "YourPassWord" to password which you chose on step 3.2

```import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="YourUserName",
    password="YourPassWord",
    database="bans_2022"
)
print(mydb)
```

Run your code, it should look like this

![alt text](https://i.imgur.com/tYsgOFy.png)

After this code works, the connection between Python and MySQL is working. Now you might want use my Python code on this (sqlpython.py on this reporisity) or create your own. Now youre basicly done and project is fully set up! 
