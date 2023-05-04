from DBConnection import DBConnection

class Service:

    def insertService(self):
        print('Print from insert Operation')
        dbconnection = DBConnection()
        connection = dbconnection.getConnection()
        cursor = connection.cursor()
        statement = ''' insert into service (service_name) values ('AC Mechanic')'''
        cursor.execute(statement)
        connection.commit()
        print('Insert Operation Successfully Completed')
        cursor.close()
        connection.close()

service = Service()
service.insertService()
