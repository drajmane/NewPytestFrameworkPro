import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Addcust:

    cust_menu="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p"
    cust_sub_menu="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    add_new="//a[@class='btn btn-primary']"
    emaill_id="//input[@id='Email']"
    pass_word="//input[@id='Password']"
    first_name="//input[@id='FirstName']"
    last_name="//input[@id='LastName']"
    gende_id="//input[@id='Gender_Male']"
    dob_id="//input[@id='DateOfBirth']"
    compp_name="//input[@id='Company']"
    admin_stratire="//li[contains(text(),'Administrators')]"
    drop_vendor="//select[@id='VendorId']//option[@value='2']"
    last_checkbox="//input[@id='Active']"
    sub_mitbutton="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def clickoncustmenu(self):
        self.driver.find_element(By.XPATH,self.cust_menu).click()

    def clickcystsubmenu(self):
        self.driver.find_element(By.XPATH,self.cust_sub_menu).click()

    def click_addcust(self):
        self.driver.find_element(By.XPATH,self.add_new).click()

    def email_id(self,email):
        self.driver.find_element(By.XPATH,self.emaill_id).send_keys(email)

    def set_password(self,password):
        self.driver.find_element(By.XPATH,self.pass_word).send_keys(password)

    def set_fname(self,fname):
        self.driver.find_element(By.XPATH,self.first_name).send_keys(fname)

    def set_lname(self,lname):
        self.driver.find_element(By.XPATH,self.last_name).send_keys(lname)

    def selectradio_butto(self):
        self.driver.find_element(By.XPATH,self.gende_id).click()

    def seledob(self,dob):
        self.driver.find_element(By.XPATH,self.dob_id).send_keys(dob)

    def comp_name(self,compname):
        self.driver.find_element(By.XPATH,self.compp_name).send_keys(compname)


    def save_button(self):
        self.driver.find_element(By.XPATH,self.sub_mitbutton).click()




















