import csv

class CheckData:

    def readCsv(self):

        name = open('name.csv', mode = 'r')
        namelist = csv.reader(name)

        i = 0
        for n in namelist:
            if i == 0:
                sqlstatement = f'insert into bio ({n[0]},{n[1]},{n[2]}) values'
                #print('Header Row Detected')
            else:
                print(f'{sqlstatement} ({n[0]},{n[1]},{n[2]});')
                #print('Data Row Detected')
            i += 1
            print('--------------------')
            #print(n)
            print('--------------------')




checkdata = CheckData()
checkdata.readCsv()
