# wlw-scrapper
Scrapper for wlw.de

**singleRun.py**
Here we prepare some data for execution, such as region and the amount of pages.
The amount of pages for specific category is calculated by dividing total companies number by 30 as this is the number wlw uses for pagination.
The links.py is used to get that number as well as companies page links for further scrapping
Next getInfo.py is used to get contact info from each page we got from the last step as well as checking if any of the emails aren't on the BannedDomains.txt
Finally infoCounter.py checks lists for duplicates, empty contact infos and splits it into 2 lists

**links.py**
Creates a link list from the links in listing and saves it to links.txt

**getInfo.py**
Used to get contact info from specific company page, also checks is the comapny is not on the banned list

**infoCounter.py**
It counts how many contact there is after checking for empty spots

**main.py**
Chains singleRun.py to run for multiple categories

