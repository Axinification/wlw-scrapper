from bs4 import BeautifulSoup
import requests
import time
import links
import getInfo
import infoCounter
from datetime import datetime, timedelta  
from tqdm import tqdm

def main(category):
    url_main = "https://www.wlw.de"
    url_search = "/en/search" #   "/de/suche" change for region
    page_param = "/page/" # 2 or more without param for 1st
    category_param =  "?q="+category
    number_of_contacts = 0
    contacts_per_page = 30

    with open('./temp/links.txt', 'w', encoding='utf-8') as f:
        f.write('')

    webpage = requests.get(url_main+url_search+category_param)
    print(url_main+url_search+category_param)
    time.sleep(2)

    with open('./temp/webpage.html', 'w', encoding='utf-8') as html_file:
        html_file.write('')
        html_file.write(webpage.content.decode('utf-8', 'ignore'))
        html_file.close()

    with open('./temp/webpage.html', 'r', encoding='utf-8') as html_file:
        content = html_file.read()
        soup = BeautifulSoup(content, 'lxml')
        number_of_contacts = soup.find('a', class_='search-tab-link search-tabs-supplier-link active')
        number_of_contacts = number_of_contacts.text.split()[0]
        number_of_contacts = int(number_of_contacts.replace('.',''))
        html_file.close()
        
        links.main()

    number_of_pages = int(number_of_contacts/contacts_per_page) + (number_of_contacts%contacts_per_page>0)

    barInstance = tqdm(total=number_of_pages, position=1)

    for page in range(2,number_of_pages+2):             
        webpage = requests.get(url_main+url_search+page_param+str(page)+category_param)

        with open('./temp/webpage.html', 'w', encoding='utf-8') as html_file:
            html_file.write(webpage.content.decode('utf-8'))
            html_file.close()
        
        links.main()
        barInstance.set_description("Scanning pages for companies... ")
        barInstance.update(1)
        time.sleep(0.5)

    barInstance.close()

    getInfo.main(number_of_contacts)

    infoCounter.main(number_of_contacts)


if __name__ == "__main__":
    main()  
