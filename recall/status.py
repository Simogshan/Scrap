import csv
from statusDAO import PersonDAO

class PersonCheck:

    def validateCsv(self):

        file = open('person.csv', mode = 'r')
        personlist = csv.reader(file)

        i = 0 
        for person in personlist:
            if i == 0:
                #sqlstatement = f'insert into person ({person[0]},{person[1]}) values'
                print('--------------------')
                print('Header Row Detected')
                print('--------------------')
            else:
                #print(f'{sqlstatement} ({chr(39)}{person[0]}{chr(39)},{chr(39)}{person[1]}{chr(39)});')
                
                print('--------------------')
                print('Data Row Detected')
                print('--------------------')

            persondao = PersonDAO()

            for name in personlist:
                persondao.insertPerson(name)

            #persondao.selectPerson()
            i += 1
            
            persondao.selectPerson()


personcheck = PersonCheck()
personcheck.validateCsv()
