from selenium import webdriver
from selenium.webdriver.firefox.options import Options as fir_op
from selenium.webdriver.chrome.options import Options as ch_op
from time import sleep


class FacebookLogin():
    def __init__(self, browser="firefox", gui="yes") -> None:
        self.browser = browser
        self.gui = gui
        if self.browser == "chrome":
            if self.gui == "yes":
                self.br = webdriver.Chrome(
                    options=ch_op().add_argument("--headless"))
            else:
                self.br = webdriver.Chrome()
        elif self.browser == "firefox":
            if self.gui == "yes":
                self.br = webdriver.Firefox(
                    options=ch_op().add_argument("--headless"))
            else:
                self.br = webdriver.Firefox()

    def login(self, email, passwd):
        auth = {
            "email": email,
            "passwd": passwd
        }

        self.br.get("https://m.facebook.com/login")

        email_field = self.br.find_element(by="name", value="email")
        passwd_field = self.br.find_element(by="name", value="pass")
        login_butt = self.br.find_element(by="name", value="login")

        email_field.send_keys(email)
        passwd_field.send_keys(passwd)
        login_butt.click()

        sleep(4)

        self.br.get("https://m.facebook.com/")

        if self.br.title == "Facebook":
            print("Success")
        else:
            print("Wrong")

        print(auth)
