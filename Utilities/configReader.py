from configparser import ConfigParser


# la fonction readConfig permet de lire le continue de ficher "conf.ini"
from configparser import ConfigParser


# la fonction readConfig permet de lire le continue de ficher "conf.ini"
def readConfig(section, key):
    config = ConfigParser()
    config.read("..\\Configuration\\conf.ini")
    return config.get(section, key)
