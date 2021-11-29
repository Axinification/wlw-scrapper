from bs4 import BeautifulSoup
import requests
import time
from tqdm import tqdm

def main(number_of_contacts):
    email=''
    website=''
    barInstance = tqdm(total=number_of_contacts, position=0)

    ban_list = open('./scrapper/BannedDomains.txt', 'r')
    bans = ban_list.readlines()

    
    with open('./temp/infos.txt', 'w') as infos:
        infos.write('')
        infos.close()

    links_list = open('./temp/links.txt', 'r')
    lines = links_list.readlines()

    for link in lines:
        full_link = "https://www.wlw.de"+link.strip()
        companypage = requests.get(full_link)

        with open('./temp/companypage.html', 'w', encoding='utf-8', errors='ignore') as html_file:
            html_file.write('')
            html_file.write(companypage.content.decode('utf-8'))
            html_file.close()

        with open('./temp/companypage.html', 'r', encoding='utf-8', errors='ignore') as html_file:
            content = html_file.read()
            soup = BeautifulSoup(content, 'lxml')
            email = soup.find('a', id='location-and-contact__email').span.text if soup.find('a', id='location-and-contact__email') else "None"
            website = soup.find('a', id='location-and-contact__website').contents[-1].strip() if soup.find('a', id='location-and-contact__website') else "None"
            html_file.close()
        
        for ban in bans:
            if ban in email:
                continue

        with open('./temp/infos.txt', 'a') as infos:
            infos.write(email+' '+website+' '+'\n')
            infos.close()

        barInstance.set_description("Scanning pages for info... ")
        barInstance.update(1)
        time.sleep(0.5)
    barInstance.close()


if __name__ == "__main__":
    main()