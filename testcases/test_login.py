from selenium import webdriver
from Pageobject.LoginPage import Login
from testcases.Confitest import setup

from utilities.Readproperties import Readconfig


import pytest



class Test_login:

    base_url="https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username="admin@yourstore.com"
    password="admin"
    # base_url=Readconfig.readappli_url()
    # username=Readconfig.readusername()
    # password=Readconfig.readpassword()

    @pytest.mark.sanity
    def test_homepagetitle(self):
        self.driver=webdriver.Edge()
        # self.driver=setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(3)
        act_title=self.driver.title


        if act_title=="Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepagetitle.png")
            assert False
            self.driver.close()


    @pytest.mark.regression
    def test_login_page(self):
        self.driver=webdriver.Edge()
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(3)

        self.obj1=Login(self.driver)

        self.obj1.set_username(self.username)
        self.obj1.set_password(self.password)
        self.obj1.login_button()
        act_pagetitle=self.driver.title


        if act_pagetitle=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login_page.png")
            assert False

    @pytest.mark.sanity
    def test_logout(self):
        self.driver=webdriver.Edge()
        self.driver.get(self.base_url)

        self.obj1=Login(self.driver)
        self.obj1.set_username(self.username)
        self.obj1.set_password(self.password)
        self.obj1.login_button()
        self.driver.implicitly_wait(5)
        self.obj1.logout_button()
        self.driver.close()












































