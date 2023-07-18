from selenium import webdriver
from selenium.webdriver.common.by import By
from Pageobject.LoginPage import Login



class Dashboard_page:

    dash_item="//*[@class='nav-icon fas fa-desktop']"



    def __init__(self,driver):
        self.driver=driver

    def find_dashboard(self):
        self.driver.find_elements(By.XPATH,self.dash_item).click()

   













