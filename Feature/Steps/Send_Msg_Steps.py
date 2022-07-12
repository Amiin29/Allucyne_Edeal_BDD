import time
import allure
from behave import *
from allure_commons.types import AttachmentType
from Feature.Steps.Set_Properties.SetProperty_SendMsg import SetProperty_SendMsg
from Utilities.readproperty import ReadConfig
from selenium import webdriver
import configparser
config = configparser.RawConfigParser()
BaseUrl = ReadConfig.getURL()


@given(u'lancer le chrome Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path='C:\\Users\\Asus\\PycharmProjects\\PythonModelFramework'
                                                      '\\chromedriver.exe')
    context.driver.maximize_window()
    context.driver.get(BaseUrl)


@when(u'Page d\'accueil s\'affiche et faire le login')
def step_impl(context):
    Set = SetProperty_SendMsg(context.driver)
    time.sleep(1.5)
    Set.setUsername()
    time.sleep(1.5)
    Set.setPassword()
    time.sleep(1.5)


@then(u'Page Home s\'affiche')
def step_impl(context):
    Set = SetProperty_SendMsg(context.driver)
    Set.clickOnLogin()
    time.sleep(1.5)


@then(u'Cliquer sur l\'icone Mon Compte')
def step_impl(context):
    Set = SetProperty_SendMsg(context.driver)
    Set.setMonCompte()
    time.sleep(1.5)


@then(u'Cliquer sur Messages personnels')
def step_impl(context):
    Set = SetProperty_SendMsg(context.driver)
    Set.GoToMessagesPersonnels()
    time.sleep(1.5)


@then(u'Choisir un utilisateur')
def step_impl(context):
    Set = SetProperty_SendMsg(context.driver)
    Set.ClicksurUser()
    time.sleep(1.5)
    Set.SelectUser()
    time.sleep(2.0)


@then(u'Envoie message')
def step_impl(context):
    Set = SetProperty_SendMsg(context.driver)
    Set.WriteMsg()
    time.sleep(2.0)


@then(u'Cliquer sur le bouton Envoie message')
def step_impl(context):
    Set = SetProperty_SendMsg(context.driver)
    Set.ClickSubmit()
    time.sleep(3.0)
