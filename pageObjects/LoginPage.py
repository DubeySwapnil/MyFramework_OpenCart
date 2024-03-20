from selenium.webdriver.common.by import By


class LoginPage:
    textbox_email_xpath = "//input[@id='input-email']"
    textbox_password_xpath = "//input[@id='input-password']"
    button_login_xpath = "//input[@value='Login']"
    msg_loginconfirmation_xpath = "//div[@id='content']/h2[1]"

    def __init__(self, driver):
        self.driver = driver

    def setemail(self, email):
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(email)

    def setpass_for_login(self, pwd):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def isMyAccountExists(self):
        try:
            return self.driver.find_element(By.XPATH,self.msg_loginconfirmation_xpath).is_displayed()
        except:
            return None

