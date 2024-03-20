import time

import pytest

from pageObjects.Homepage import Homepage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccount import MyAccount
from utilities import XLUtils
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_LoginbyDT:
    baseurl=ReadConfig.getBaseURl()
    logger=LogGen.loggen()

    path=os.path.abspath(os.curdir)+"//testdata//OpenCart.xlsx"

    @pytest.mark.DDT
    def test_login_ddt(self,setup):
        list_status=[]
        self.driver=setup
        self.driver.get(self.baseurl)
        self.rows=XLUtils.getRowCount(self.path,"Sheet1")

        self.hp=Homepage(self.driver)
        self.lp=LoginPage(self.driver)
        self.ma=MyAccount(self.driver)

        for row in range(2,self.rows+1):
            self.hp.click_my_account()
            self.hp.click_login()

            self.email=XLUtils.readData(self.path,"Sheet1",row,1)
            self.password=XLUtils.readData(self.path,"Sheet1",row,2)
            self.expected=XLUtils.readData(self.path,"Sheet1",row,3)

            self.lp.setemail(self.email)
            self.lp.setpass_for_login(self.password)
            self.lp.clickLogin()
            time.sleep(2)
            self.actual= self.lp.isMyAccountExists()

            if self.expected=="Valid":
                if self.actual==True:
                    list_status.append("Pass")
                    self.ma.clickLogout()
                else:
                    list_status.append("Fail")
            elif self.expected=="Invalid":
                if self.actual==True:
                    list_status.append("Fail")
                    self.ma.clickLogout()
                else:
                    list_status.append("Pass")
        self.driver.close()
        print(list_status)
        if "Fail" not in list_status:
            assert True

        else:
            assert False


