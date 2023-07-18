from selenium import webdriver
from Pageobject.LoginPage import Login
from Pageobject.AddcustomerPOM import Addcust
from testcases.Confitest import setup

from utilities.Readproperties import Readconfig


import pytest



class Test_login:

    base_url="https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username="admin@yourstore.com"
    password="admin"
    dob='10-05-97'

    @pytest.mark.sanity
    def test_addcustomer(self):
        self.driver=webdriver.Edge()
        self.driver.maximize_window()
        self.driver.get(self.base_url)

        self.ob1=Login(self.driver)
        self.ob1.set_username(self.username)
        self.ob1.set_password(self.password)
        self.ob1.login_button()

        self.driver.implicitly_wait(5)
        self.ob2=Addcust(self.driver)
        self.ob2.clickoncustmenu()
        self.ob2.clickcystsubmenu()
        self.ob2.click_addcust()
        self.ob2.email_id("drajmane11@gmail.com")
        self.ob2.set_password("admin123")
        self.ob2.set_fname("Dhanraj")
        self.ob2.set_lname("rajmane")
        self.ob2.selectradio_butto()
        self.ob2.seledob(self.dob)
        # self.ob2.compp_name("capge")
        self.ob2.save_button()

        self.driver.close()



















