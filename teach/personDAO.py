from DBConnection import DBConnection

class PersonDAO:

    def insertPerson(self,personList):
        print('Print from Insert Person')
        dbconnection = DBConnection()
        connection = dbconnection.getConnection()
        cursor = connection.cursor()
        statement = ''' insert into person (first_name,last_name) values (%s,%s) '''
        cursor.execute(statement,personList)
        connection.commit()
        print('Insert Operation Successfully Completed')
        cursor.close()
        connection.close()
    
    def selectPerson(self):
        print('Print from Select Person')
        dbconnection = DBConnection()
        connection = dbconnection.getConnection()
        cursor = connection.cursor()
        statement = ''' select * from person  '''
        cursor.execute(statement)
        result = cursor.fetchall()

        for r in result:
            print(r)

        print('Select Operation Successfully Completed')
        cursor.close()
        connection.close()

#personList = ['Ravi','Kumar']
#persondao = PersonDAO()
#persondao.insertPerson(personList)
#persondao.selectPerson()
