import configparser
import os

config= configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+"//configurations//config.ini")

class ReadConfig:
    @staticmethod
    def getBaseURl():
        url= config.get('commoninfo','baseURL')
        return url

    @staticmethod
    def getusername():
        username= config.get('commoninfo','username')
        return username

    @staticmethod
    def getpassword():
        password= config.get('commoninfo','password')
        return password