import csv
from serviceDAO import ServiceDAO

class ServiceHelper:

    def readCsvFile(self):
        file = open('service.csv', mode ='r')
        csvfile = csv.reader(file)
        return csvfile

    def insertCsvFile(self):

        servicedao = ServiceDAO()
        csvlist = self.readCsvFile()

        for l in csvlist:
            servicedao.insertService(l)

        servicedao.selectService()

    def printCsvFile(self):
        self.insertCsvFile()


servicehelper = ServiceHelper()
servicehelper.printCsvFile()
