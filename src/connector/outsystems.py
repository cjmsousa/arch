from sqlserver import SqlServer
import pandas 
from configuration import Configuration

class OutSystems:

    def __init__(self, platformName):
        
        #Get configuration values
        configurationValues = Configuration.getSection(platformName)

        #Create database connection
        self.databaseConnection = SqlServer(configurationValues["database-host"],
                                configurationValues["database-name"],
                                configurationValues["database-user"],
                                configurationValues["database-password"])

    def getApplications(self):
        
        #Get list of OutSystems applications
        applicationList = self.databaseConnection.query('SELECT * FROM ossys_application;')

        print(applicationList)
    
