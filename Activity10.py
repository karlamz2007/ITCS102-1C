from getpass import getpass 

user = "K4rlAmz"
password = "pass99word11"

login_user = input ("Enter your username : ")
loging_password = getpass ("Enter your password : ")

if (login_user == user) and (loging_password == password) :
    print ("Access Granted !! Login Successfull")
else :
    print("Access Denied , Incorrect password or username")
