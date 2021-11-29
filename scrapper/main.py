import shutil
import singleRun
import os
import urllib.parse
from tqdm import tqdm

def main():
    with open('./scrapper/ToDoList.txt', 'r+', encoding='utf-8', errors='ignore') as links_list:
        categories = links_list.readlines()
        links_list.close()

    while len(categories) > 0:
        category = categories[0]
        category = category.strip().lower().rstrip()
        categoryUrl = urllib.parse.quote(category)
        categoryName = category.replace(' ', '-')
        categoryTextFileUrl = './data/'+categoryName.rstrip()+'.txt'
        categoriesAmount = len(categories)
        del categories[0]
        
        if not os.path.exists('temp'):
            os.mkdir('temp')
        if not os.path.exists('data'):
            os.mkdir('data')
        if os.path.isfile(categoryTextFileUrl):
            continue

        print(f"Categories left {categoriesAmount} - {category}")

        singleRun.main(categoryUrl)

        with open('./scrapper/ToDoList.txt', 'w', encoding='utf-8', errors='ignore') as links_list:
            for element in categories:
                links_list.write(element)
        
        shutil.copy('./temp/emailList.txt', './data')
        os.rename('./data/emailList.txt', categoryTextFileUrl)
        shutil.rmtree('./temp')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        shutil.rmtree('./temp')
        print('Operation interrupted!')