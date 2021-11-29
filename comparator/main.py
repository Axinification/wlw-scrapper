import os

def main():
    directiory = './comparator/data_to_compare'
    directory_checked = "./comparator/data_checked"
    #Open first file
    for filename1 in os.listdir(directiory):
        file1 = os.path.join(directiory,filename1)
        list1 = open(file1, 'r')
        contacts1 = list1.readlines()
        #Open second file
        for filename2 in os.listdir(directiory):
            file2 = os.path.join(directiory,filename2)
            #If file's the same continue
            if file1 == file2:
                continue
            elif filename2 in os.listdir(directory_checked):
                continue
            else:
                #Open files and read lines
                list2 = open(file2, 'r')
                contacts2 = list2.readlines()
                contacts1 = [ x for x in contacts1 if not x in contacts2]

        checkedFile = open(f"{directory_checked}/{filename1}", 'w')
        for contact in contacts1:
            checkedFile.write(contact)
        checkedFile.close()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Operation interrupted!')