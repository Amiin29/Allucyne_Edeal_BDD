import configparser
from selenium.webdriver.common.by import By
config = configparser.RawConfigParser()
config.read(".\\Configuration\\conf.ini")


class SetProperty_SendMsg:
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

    def GoToMessagesPersonnels(self):
        self.driver.find_element(By.XPATH, config.get("Info", "Message_personels_XPATH")).click()

    def ClicksurUser(self):
        self.driver.find_element(By.XPATH, config.get("Info", "click_1_XPATH")).click()

    def SelectUser(self):
        self.driver.find_element(By.XPATH, config.get("Info", "click_2_XPATH")).click()

    def WriteMsg(self):
        self.driver.find_element(By.XPATH,
                                 "//div[@class='position-relative']//textarea[@placeholder='Écrire un message']").send_keys(
            "Hellooooo Amin from script automated ")

    def ClickSubmit(self):
        self.driver.find_element(By.XPATH, "(//button[@aria-label='Envoyer message personnel'])[1]").click()
