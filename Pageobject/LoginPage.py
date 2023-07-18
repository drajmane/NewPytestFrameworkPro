from selenium import  webdriver
from selenium.webdriver.common.by import By


class Login:

    email_id="//input[@id='Email']"
    pass_word_id="//input[@id='Password']"
    login_button_id="//button[@class='button-1 login-button']"
    log_out_button="//a[text()='Logout']"


    def __init__(self,driver):
        self.driver=driver

    def set_username(self,username):
        self.driver.find_element(By.XPATH,self.email_id).clear()
        self.driver.find_element(By.XPATH,self.email_id).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(By.XPATH, self.pass_word_id).clear()
        self.driver.find_element(By.XPATH,self.pass_word_id).send_keys(password)

    def login_button(self):
        self.driver.find_element(By.XPATH,self.login_button_id).click()

    def logout_button(self):
        self.driver.find_element(By.XPATH,self.log_out_button).click()















