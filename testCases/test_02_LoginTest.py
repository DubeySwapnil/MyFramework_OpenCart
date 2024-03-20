import pytest

from pageObjects.Homepage import Homepage
from pageObjects.LoginPage import LoginPage
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_02_Login:
    baseURL = ReadConfig.getBaseURl()
    logger = LogGen.loggen()
    user= ReadConfig.getusername()
    password=ReadConfig.getpassword()

    @pytest.mark.sanity
    def test_Login(self,setup):
        self.logger.info("******************test_002_LoginTest_starting*********************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp =Homepage(self.driver)
        self.hp.click_my_account()
        self.hp.click_login()
        self.lp=LoginPage(self.driver)
        self.lp.setemail(self.user)
        self.lp.setpass_for_login(self.password)
        self.lp.clickLogin()
        self.target_page=self.lp.isMyAccountExists()
        if self.target_page==True :
            self.driver.close()
            assert True
            self.logger.info("******************test_002_LoginTest_Passed*********************************")
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"//screenshots//"+"test_002_LoginTest.png")
            assert False
            self.logger.info("******************test_002_LoginTest_failed *********************************")
            self.driver.close()

