# read a common data
import configparser
config = configparser.RawConfigParser() #get one config data
config.read('.\\Configurations\\config.ini')

class readConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('url', 'baseUrlWeb')
        return url

    @staticmethod
    def getEmail():
        email = config.get('user info', 'email')
        return email

    @staticmethod
    def getPassword():
        password = config.get('user info', 'password')
        return password

    @staticmethod
    def getUnregisteredEmail():
        unregistredEmail = config.get('user info', 'unregistredEmail')
        return unregistredEmail
    @staticmethod
    def getrandomPassword():
        randomPassword = config.get('user info', 'randomPassword')
        return randomPassword