from selenium.webdriver.common.by import By


class Homepage:
    link_myaccountpath_xpath = "//*[@id='top-links']/ul/li[2]/a/span[1]"
    link_register_linktext = "Register"
    link_login_linktext = "Login"

    def __init__(self, driver):
        self.driver = driver

    def click_my_account(self):
        self.driver.find_element(By.XPATH, self.link_myaccountpath_xpath).click()

    def click_register(self):
        self.driver.find_element(By.LINK_TEXT, self.link_register_linktext).click()

    def click_login(self):
        self.driver.find_element(By.LINK_TEXT, self.link_login_linktext).click()
