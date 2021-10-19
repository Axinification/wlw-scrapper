from tqdm import tqdm

def main(number_of_contacts):
    barInstance = tqdm(total=number_of_contacts, position=0)
    nones = 0
    with open('./temp/emailList.txt', 'w') as emailList:
        emailList.write('')
        emailList.close()
    with open('./temp/sitesList.txt', 'w') as sitesList:
        sitesList.write('')
        sitesList.close()

    links_list = open('./temp/infos.txt', 'r')
    lines = links_list.readlines()

    for line in lines:
        if line.split()[0] != "None":
            with open('./temp/emailList.txt', 'a') as emailList:
                emailList.write(line.split()[0] + "\n")
                emailList.close()
        elif line.split()[0] == "None" and line.split()[1] != "None":
            with open('./temp/sitesList.txt', 'a') as sitesList:
                sitesList.write(line.split()[1] + "\n")
                sitesList.close()
        else:
            nones+=1
        barInstance.set_description("Sorting data...")
        barInstance.update(1)
    barInstance.close()

    print(f"Number of companies without contact info: {nones}")

if __name__ == "__main__":
    main()

