import configparser
from selenium.webdriver.common.by import By
config = configparser.RawConfigParser()
config.read(".\\Configuration\\conf.ini")


class SetProperty_AddUser:
    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, driver):
        self.driver.find_element(By.XPATH, "(//input[@id='username'])[1]").send_keys("user")

    def setPassword(self, driver):
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("bitnami")

    def clickOnLogin(self):
        self.driver.find_element(By.XPATH, "//button[@id='loginbtn']").click()

    def setMonCompte(self):
        self.driver.find_element(By.XPATH, config.get("Info", "custom_card_account")).click()

    def GoToAdministrationDuSite(self):
        self.driver.find_element(By.XPATH, config.get("Info", "Administration_du_site")).click()

    def GoToAjoutUser(self):
        self.driver.find_element(By.XPATH, config.get("Info", "Ajouter_utilisateur")).click()

    def setIdUsername(self):
        self.driver.find_element(By.ID, "id_username").send_keys("amin29")

    def CreatePassword(self):
        self.driver.find_element(By.XPATH, config.get("Info", "Id_password")).click()

    def SetCodeEtudiant(self):
        self.driver.find_element(By.XPATH, config.get("Info", "Code_etudiant")).send_keys("KFKD6")

    def setNomMarital(self):
        self.driver.find_element(By.XPATH, config.get("Info", "Nom_marital")).send_keys("MDJS")

    def setCodeDiplome(self):
        self.driver.find_element(By.XPATH, config.get("Info", "Code_diplome")).send_keys("MDJS")

    def setFirstName(self):
        self.driver.find_element(By.ID, "id_firstname").send_keys("Amin")

    def setLastName(self):
        self.driver.find_element(By.ID, "id_lastname").send_keys("Miladi")

    def setEmail(self):
        self.driver.find_element(By.ID, "id_email").send_keys("amin29.miladi@gmail.com")

    def ClickSubmit(self):
        self.driver.find_element(By.ID, "id_submitbutton").click()
