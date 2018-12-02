import pyodbc
import pandas

class SqlServer:

    def __init__(self, databaseHost, databaseName, databaseUser, databasePassword):
        
        #Debug connection
        print("Connecting to SqlServer on [%s] to database [%s] with user [%s]" %(databaseHost, databaseName, databaseUser))

        self.databaseConnection = {}
        #Set database connection
        #self.databaseConnection  = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
        #                                    "Server=" + databaseHost + ";"
        #                                    "Database=" + databaseName + ";"
        #                                    "uid=" + databaseUser + ";"
        #                                    "pwd=" + databasePassword + ";")

    def query(self, query):

        #Debug query
        print("Executing query [%s] on connection [%s] " %(query, self.databaseConnection))

        #Run query
        dataFrame = {}
        #dataFrame = pandas.read_sql(query, self.databaseConnection)

        #Return result
        return (dataFrame)