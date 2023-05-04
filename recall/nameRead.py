import csv

class NameRead:

    def readCsv(self):

        name = open('name.csv', mode = 'r')
        namelist = csv.reader(name)
        return namelist

    def checkCsv(self):

        namelist = self.readCsv()

        i = 0
        for name in namelist:
            if i == 0:
                print('Header Row Detected')
            else:
                print('Data Row Detected')
            i += 1

            print ('---------------------')
            print (type(name))
            print ('---------------------')
            print (name)
            print ('---------------------')
            print (tuple(name))

nameread = NameRead()
nameread.checkCsv()
