from selenium import  webdriver
from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self,driver):
        self.driver = driver

        self.login_button_XPATH = "/html/body/div[1]/div/div[1]/header/div/div/a[1]/button"
        self.mobile_number_input_ID = "contact_number"
        self.get_otp_XPATH = "/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/form/div[1]/div/button"
        self.otp_enter_NAME = "postNo.0.otp"
        self.terms_con_ID = "tnc"
        self.proceed_btn_XPATH = "/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/form/div[4]/button"


    def login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_XPATH).click()

    def enter_mubilenum(self,mobilenumber):
        self.driver.find_element(By.XPATH,self.mobile_number_input_ID).clear()
        self.driver.find_element(By.XPATH, self.mobile_number_input_ID).send_keys(mobilenumber)

    def get_otp (self):
        self.driver.find_element(By.XPATH, self.get_otp_XPATH).click()

    def enter_otp(self, enterotp):
        self.driver.find_element(By.XPATH,self.otp_enter_NAME).clear()
        self.driver.find_element(By.XPATH, self.otp_enter_NAME).send_keys(enterotp)

    def terms(self,terms):
        self.driver.find_element(By.XPATH, self.terms_con_ID).click()

    def proceed(self):
        self.driver.find_element(By.XPATH, self.proceed_btn_XPATH).sclick()