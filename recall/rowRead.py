class RowRead:

    def readRow(self):

        row1 = ['first_name', 'last_name', 'age']
        row2 = ['Anbu', 'Nattu', '43']
        row3 = ['Raju', 'Bhai', '34']
        row4 = ['Abarna', 'Ramya', '30']

        rowlist = [row1, row2, row3, row4]

        print(type(rowlist))
        print(tuple(rowlist))
        #print(rowlist)

       #i = 0 
        #for r in rowlist:
            #if i == 0:
                #print('Header row Detected')
            #else:
                #print('Data row Detected')
            #i += 1

            #print('--------------------------')
            #print(r)
            #print('--------------------------')


rowread = RowRead()
rowread.readRow()
