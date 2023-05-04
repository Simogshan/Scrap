import csv
from personDAO import PersonDAO

class PersonHelper:

    def readCsvFile(self):
        file = open('person.csv', mode = 'r')
        csvfile = csv.reader(file)
        return csvfile

    def insertCsvFile(self):
        
        persondao = PersonDAO()

        personCsvList = self.readCsvFile()

        for csvlist in personCsvList:
            persondao.insertPerson(csvlist)
        persondao.selectPerson()


personhelper = PersonHelper()
personhelper.insertCsvFile()




