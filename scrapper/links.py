from bs4 import BeautifulSoup

def main():

    contact_list = []

    with open('./temp/webpage.html', 'r', encoding='utf-8', errors='ignore') as html_file:
        content = html_file.read()
        soup = BeautifulSoup(content, 'lxml')
        for link in soup.findAll('a', class_='company-title-link'):
            contact_list.append(link['href'])


    with open('./temp/links.txt', 'a') as links:
        for link in contact_list:
            links.write(link)
            links.write("\n")