from selenium.webdriver.common.by import By


class AccountRegistrationpage:
    txtfield_f_name = "firstname"
    txtfield_l_name = "lastname"
    txtfield_email_name = "email"
    txtfield_phone_name = "telephone"
    txtfield_confpass_name = "confirm"
    txtfield_password_name = "password"
    checkbox_agreepolicy_name = "agree"
    radiobtn_subscribe_name = "newsletter"
    checkbox_policy_xpath = "//input[@name='agree']"
    button_continue_xpath = "//input[@value='Continue']"
    bodytext_confirmation_xpath = "//div[@id='content']/h1"

    def __init__(self, driver):
        self.driver = driver

    def setfirstname(self, fname):
        self.driver.find_element(By.NAME, self.txtfield_f_name).send_keys(fname)

    def setlastname(self, lname):
        self.driver.find_element(By.NAME, self.txtfield_l_name).send_keys(lname)

    def setemail(self, email):
        self.driver.find_element(By.NAME, self.txtfield_email_name).send_keys(email)

    def settelephone(self, telephone):
        self.driver.find_element(By.NAME,self.txtfield_phone_name).send_keys(telephone)

    def setPasseord(self, password):
        self.driver.find_element(By.NAME,self.txtfield_password_name).send_keys(password)

    def setConfirmpassword(self, confirmpassword):
        self.driver.find_element(By.NAME,self.txtfield_confpass_name).send_keys(confirmpassword)

    def clickYestoAgreePolicy(self):
        self.driver.find_element(By.NAME,self.checkbox_agreepolicy_name).click()

    def NoToNewsletter(self):
        self.driver.find_element(By.NAME,self.radiobtn_subscribe_name).click()

    def ClickonContinue(self):
        self.driver.find_element(By.XPATH,self.button_continue_xpath).click()

    def confirm_accountRegistration(self):
        try:
            return self.driver.find_element(By.XPATH,self.bodytext_confirmation_xpath).text
        except:
            None