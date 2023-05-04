import csv

class PersonRead:

    def insertPerson(self):

        file = open('person.csv', mode = 'r')
        namelist = csv.reader(file)

        i = 0
        for name in namelist:
            if i == 0:
                sqlstatement = f'insert into person ({name[0]},{name[1]}) values'
                #print('Header Row Detected')

            else:
                print(f'{sqlstatement} ({chr(39)}{name[0]}{chr(39)},{chr(39)}{name[1]}{chr(39)});')
                #print('Data Row Detected')
            i += 1



personread = PersonRead()
personread.insertPerson()
