import os

def main():
    directiory = 'data'
    #Open first file
    for filename1 in os.listdir(directiory):
        file1 = os.path.join(directiory,filename1)
        #Open second file
        for filename2 in os.listdir(directiory):
            file2 = os.path.join(directiory,filename2)
            #If file's the same continue
            if file1 == file2:
                continue
            else:
                #Open files and read lines
                list1 = open(file1, 'r')
                contacts1 = list1.readlines()
                list2 = open(file2, 'r')
                contacts2 = list2.readlines()



                #TODO Only check against nest file, should iterate over all contact lists and eliminate duplicants, restructurization required
                checked = [ x for x in contacts1 if not x in contacts2]

                checkedFile = open('./data-checked/'+filename1, 'w')
                for contact in checked:
                    checkedFile.write(contact)
                checkedFile.close()



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Operation interrupted!')