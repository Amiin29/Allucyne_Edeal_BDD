import time
import allure
from behave import *
from allure_commons.types import AttachmentType
from Feature.Steps.Set_Properties.SetProperty_AddUser import SetProperty_AddUser
from Utilities.readproperty import ReadConfig
from selenium import webdriver
import configparser

config = configparser.RawConfigParser()
BaseUrl = ReadConfig.getURL()


@given(u'launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path='C:\\Users\\Asus\\PycharmProjects\\PythonModelFramework'
                                                      '\\chromedriver.exe')
    context.driver.maximize_window()
    context.driver.get(BaseUrl)


@when(u'CLiquer sur Ajouter un uster saisir username user et password bitnami')
def step_impl(context):
    global login
    Set = SetProperty_AddUser(context.driver)
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    Set.setUsername(username)
    time.sleep(1.0)
    Set.setPassword(password)
    time.sleep(1.0)
    context.driver.save_screenshot(".\\ScreenShots\\" + "Authentification.png")
    allure.attach(context.driver.get_screenshot_as_png(), name="authentification", attachment_type=AttachmentType.PNG)
    Set.clickOnLogin()


@then(u'open home page et cliquer sur administration du site')
def step_impl(context):
    print("dsdsd")
    time.sleep(1.0)
    Set = SetProperty_AddUser(context.driver)
    Set.setMonCompte()
    time.sleep(1.0)
    Set.GoToAdministrationDuSite()
    time.sleep(1.0)


@then(u'Remplir les champs et Cliquer sur le bouton Ajouter un user')
def step_impl(context):
    Set = SetProperty_AddUser(context.driver)
    Set.GoToAjoutUser()
    time.sleep(1.0)
    Set.setIdUsername()
    time.sleep(1.0)
    Set.CreatePassword()
    time.sleep(1.0)
    Set.SetCodeEtudiant()
    time.sleep(1.0)
    Set.setNomMarital()
    time.sleep(1.0)
    Set.setCodeDiplome()
    time.sleep(1.0)
    Set.setFirstName()
    time.sleep(1.0)
    Set.setLastName()
    time.sleep(1.0)
    Set.setEmail()
    time.sleep(1.0)
    Set.ClickSubmit()
    time.sleep(4.0)
    context.driver.save_screenshot(".\\ScreenShots\\" + "AddUser.png")
    allure.attach(context.driver.get_screenshot_as_png(), name="AddUser", attachment_type=AttachmentType.PNG)
