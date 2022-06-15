from facebook import *


browser = Facebook()

email = input("Enter Your Email : ")
passwd = input("Enter Your Password : ")

browser.login(email, passwd)

# 5 Functions Works For Now :
# .login(email, pass)
# .go_to_profile() ==> go to your main profile page
# .sync_fb_info() ==> collect your info in a dict
# .extract_prof_intro_sec(filename="outfile.html") ==> the html of the intro page of your profile
# .extract_info_to(filneame="fb_info.json")
