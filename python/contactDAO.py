from DBConnection import DBConnection

class ContactDAO:

    def insertContactNumber(self,numIn):
        print ('Print from Contact Insert')
        dbconnection = DBConnection()
        connection = dbconnection.getConnection()
        cursor = connection.cursor()
        statement = ''' insert into contact (mobile_number) values (%(phoneNumber)s)'''
        cursor.execute(statement,numIn)
        connection.commit()
        print ('Contact Insert Operation Successfully Done')
        cursor.close()
        connection.close()


