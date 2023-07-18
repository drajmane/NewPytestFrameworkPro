import time

import pytest
from selenium import webdriver
from Pageobject.LoginPage import Login
from testcases.Confitest import setup

from utilities.Readproperties import Readconfig
from utilities import Excelutility


class Test_login_002_dtt:


    base_url=Readconfig.readappli_url()
    path="C:\\Users\\admin\\OneDrive\\Desktop\\jiratestcases.xlsx"

    @pytest.Mark.skip
    def test_login_page_DTT(self):

        self.driver=webdriver.Edge()
        self.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
        self.driver.implicitly_wait(3)

        self.obj1=Login(self.driver)

        self.rownum=Excelutility.getrowcount(self.path,'Sheet3')
        print("number of rows",self.rownum)
        l_status=[]

        for r in range(5,self.rownum+1):
            self.user=Excelutility.readdata(self.path,'Sheet3',r,1)
            self.password=Excelutility.readdata(self.path,'Sheet3',r,2)
            self.exp=Excelutility.readdata(self.path,'Sheet3',r,3)
            self.driver.implicitly_wait(4)


            self.obj1.set_username(self.user)
            self.obj1.set_password(self.password)

            self.obj1.login_button()
            time.sleep(3)


            act_pagetitle=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_pagetitle==exp_title:
                if self.exp=="pass":
                    self.obj1.logout_button()
                    l_status.append("pass")

                elif self.exp=="fail":
                    self.obj1.logout_button()
                    l_status.append('fail')

            elif act_pagetitle!=exp_title:
                if self.exp=="pass":
                    l_status.append("fail")
                elif self.exp== "fail":
                    l_status.append("pass")



















































