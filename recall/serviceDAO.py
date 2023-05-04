from DBConnection import DBConnection

class ServiceDAO:

    def insertService(self,serviceList):
        print ('Print from Insert Operation')
        dbconnection = DBConnection()
        connection = dbconnection.getConnection()
        cursor = connection.cursor()
        statement = ''' insert into service (service_name) values (%s)'''
        cursor.execute(statement,serviceList)
        connection.commit()
        print ('Insert Operation successfully Completed')
        cursor.close()
        connection.close()
        
    def selectService(self):
        print ('Print from Select Operation')
        dbconnection = DBConnection()
        connection = dbconnection.getConnection()
        cursor = connection.cursor()
        statement = ''' select * from  service'''
        cursor.execute(statement)
        result = cursor.fetchall()
        
        for r in result:
            print(r)

        cursor.close()
        connection.close()


#serviceList = ['Bike Mechanic']
#servicedao = ServiceDAO()
#servicedao.insertService(serviceList)
#servicedao.selectService()
