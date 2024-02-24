import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

import unittest

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        self.driver.get("https://pos.uat.eibpl.in")
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/header/div/div/a[1]/button").click()
        self.driver.find_element(By.ID, "contact_number").send_keys('8906209679')
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/form/div[1]/div/button").click()
        self.driver.find_element(By.NAME, "postNo.0.otp").send_keys('123456')
        self.driver.find_element(By.ID, "tnc").click()
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/form/div[4]/button").click()
        private = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/header/div/nav/div/div[1]/div/div/div/div[1]/div[2]/a")
        products = self.driver.find_element(By.XPATH,"/html/body/div/div/div[1]/header/div/nav/div/div[1]/button")
        actions = ActionChains(self.driver)
        actions.move_to_element(products).move_to_element(private).click().perform()
        self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div/div[1]/div[2]/div/div[1]/div/label[2]").click()
        self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/input").send_keys("MH01")
        select_rto = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div[2]/div/div/div/div")
        actions.move_to_element(select_rto).click().perform()
        self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/input").send_keys("honda")
        select_manufacture = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/label")
        actions.move_to_element(select_manufacture).click().perform()
        self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/input").send_keys("city")
        select_model = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/label[2]")
        actions.move_to_element(select_model).click().perform()
        self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/input").send_keys("1.3 exi")
        select_variant = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/label[1]")
        actions.move_to_element(select_variant).click().perform()
        self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/label").click()


    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main()












