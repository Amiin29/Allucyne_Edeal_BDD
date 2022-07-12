import configparser
from selenium.webdriver.common.by import By
config = configparser.RawConfigParser()
config.read(".\\Configuration\\conf.ini")


class SetProperty_LogOut_Moodle:
    def __init__(self, driver):
        self.driver = driver

    def setUsername(self):
        self.driver.find_element(By.XPATH, "(//input[@id='username'])[1]").send_keys("user")

    def setPassword(self):
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("bitnami")

    def clickOnLogin(self):
        self.driver.find_element(By.XPATH, "//button[@id='loginbtn']").click()

    def setMonCompte(self):
        self.driver.find_element(By.XPATH, config.get("Info", "custom_card_account")).click()

    def clickOnLogOut(self):
        self.driver.find_element(By.XPATH, "//div[@id='mm-0']//li[9]//a[1]").click()