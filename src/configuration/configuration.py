import os
from configparser import ConfigParser


class Configuration:

    @staticmethod
    def getSection(section):

        #Create confituration partser object
        configParser = ConfigParser()

        #Read configuration file
        configParser.read(os.path.dirname(__file__) + "/config")

        #Return section values
        return(dict(configParser.items(section)))