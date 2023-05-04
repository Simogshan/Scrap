import csv

class PersonCheck:

    def readCsv(self):

        file = open('person.csv', mode = 'r')
        csvfile = csv.reader(file)
        return csvfile

    def validateFile(self):

        personlist = self.readCsv()

        i = 0 
        for person in personlist:
            if i == 0:
                sqlstatement = f'insert into person ({person[0]},{person[1]}) values'
                print('--------------------')
                print('Header Row Detected')
                print('--------------------')
            else:
                print(f'{sqlstatement} ({chr(39)}{person[0]}{chr(39)},{chr(39)}{person[1]}{chr(39)});')
                
                print('--------------------')
                print('Data Row Detected')
                print('--------------------')
            i += 1



personcheck = PersonCheck()
personcheck.validateFile()

