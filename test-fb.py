from facebook import *


browser = FacebookLogin()
email = input("Enter Your Email : ")
passwd = input("Enter Your Password : ")
browser.login(email, passwd)
