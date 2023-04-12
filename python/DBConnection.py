import mysql.connector

class DBConnection:

    def getConnection(self):

        connection = mysql.connector.connect(user='root',
                                             host='localhost',
                                             database='test',
                                             password='Qwe123!@#')
        return connection
