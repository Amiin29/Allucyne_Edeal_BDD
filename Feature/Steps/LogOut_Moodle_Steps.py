import time
import allure
from behave import *
from Utilities.readproperty import ReadConfig
from selenium import webdriver
from Feature.Steps.Set_Properties.SetProperty_LogOut_Moodle import SetProperty_LogOut_Moodle

import configparser
config = configparser.RawConfigParser()
BaseUrl = ReadConfig.getURL()


@given(u'Je suis dans la page moodle')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path='C:\\Users\\Asus\\PycharmProjects\\PythonModelFramework'
                                                      '\\chromedriver.exe')
    context.driver.maximize_window()
    context.driver.get(BaseUrl)
    Set = SetProperty_LogOut_Moodle(context.driver)
    time.sleep(1.5)
    Set.setUsername()
    time.sleep(1.5)
    Set.setPassword()
    time.sleep(1.5)
    Set.clickOnLogin()
    time.sleep(1.5)


@when(u'CLiquer sur Déconnexion')
def step_impl(context):
    Set = SetProperty_LogOut_Moodle(context.driver)
    Set.setMonCompte()
    time.sleep(1.5)
    Set.clickOnLogOut()
    time.sleep(1.5)


@then(u'Session actuelle est fermée et la page d\'accueil s\'affiche')
def step_impl(context):
    time.sleep(3.0)
