class NameRead:

    def readName(self):

        row1 = ['first_name', 'last_name', 'age']
        row2 = ['Ram', 'Raju' ,'19']
        row3 = ['Arjun', 'Ram', '34']
        row4 = ['Indu', 'Mathi', '30']

        rowlist = [row1,row2,row3,row4]

        #print(rowlist)
        
        i = 0
        for r in rowlist:
            if i == 0:
                print('Header row Detected')
            else:
                print('Data row Detected')
            i += 1
            print('----------------------')
            print(r)
            print('----------------------')

nameread = NameRead()
nameread.readName()
