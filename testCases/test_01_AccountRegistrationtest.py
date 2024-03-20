import pytest

from pageObjects.Homepage import Homepage
from pageObjects.AccountRegistrationpage import AccountRegistrationpage
from utilities.randomstring import random_String_Generator
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_01_AccountReg:

    baseURL=ReadConfig.getBaseURl()
    print(baseURL)
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_account_reg(self,setup):
        self.logger.info("******************test_001_AccountRegistration is started************************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.logger.info("----------------------Launching application--------------------")
        self.hp=Homepage(self.driver)
        self.hp.click_my_account()
        self.hp.click_register()
        self.logger.info("-----------------------Registering new user--------------------")
        self.reg= AccountRegistrationpage(self.driver)
        self.reg.setfirstname("John")
        self.reg.setlastname("Smith")
        self.email=random_String_Generator()+'@gmail.com'
        self.reg.setemail(self.email)
        self.reg.settelephone("1234567890")
        self.reg.setPasseord("Dadabhai24!")
        self.reg.setConfirmpassword("Dadabhai24!")
        self.reg.clickYestoAgreePolicy()
        self.reg.NoToNewsletter()
        self.reg.ClickonContinue()

        self.value= self.reg.confirm_accountRegistration()
        if self.value == "Your Account Has Been Created!":
            self.logger.info("-----------------------Registering new user flow finsihed successfully--------------------")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"//screenshots//" + "test_account_reg.png")
            self.logger.error("-----------------------Registering new user flow failed--------------------")
            self.driver.close()
            assert False

        self.logger.info("******************test_001_AccountRegistration is ended************************")
