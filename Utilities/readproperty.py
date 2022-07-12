import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\conf.ini")


class ReadConfig:
    @staticmethod
    def getURL():
        url = config.get("Info", "URL")
        return url

    @staticmethod
    def getUsername():
        username = config.get("Info", "username")
        return username

    @staticmethod
    def getPassword():
        password = config.get("Info", "password")
        return password
