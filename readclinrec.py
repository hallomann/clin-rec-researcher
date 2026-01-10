from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import clindict
import re
from adtodict import adtodict


# opening clinrecs
def readclinrec(link):
    driver = webdriver.Chrome()
    driver.get(link)
    wait = WebDriverWait(driver, timeout=6)
    wait.until(
        lambda _: driver.find_element(By.CLASS_NAME, "title_content").is_displayed()
    )
    # searching for and making it usable
    content = driver.find_elements(By.CLASS_NAME, "title_content")
    imp = []
    for line in content:
        imp.append(line.text)
    name = imp[0]
    id = imp[4]
    mcb = sorted(list(set(imp[1].split(", "))))
    #taking codes from body just in case (here'll be labs too)
    content=driver.find_elements(By.ID,'content') 
    imp=[]
    for line in content:
        imp.append(line.text)
    mcbi=re.sub('– |–|- |-','', imp[6]).split('\n')
    for i in range(len(mcbi)):
        mcbi[i]=mcbi[i].strip('.;')
        string=mcbi[i].split(' ')
        string[0]=string[0].replace('А','A').replace('В','B').replace('С','C').replace('Е','E').replace('Н','H').replace('К','K').replace('М','M').replace('О','O').replace('Р','P').replace('Т','T')
        mcbi[i]=' '.join(string)
    # processing mcb 10 designation
    fullmcb = []
    for i in range(len(mcb)):
        try:
            fullmcb.append(clindict.thisdict[mcb[i]])
        except:
            try:
                match = [s for s in mcbi if s.startswith(mcb[i])]
                adtodict(match[0])
                fullmcb.append(match[0])
            except:
                print(f'mcb-10 designation {mcb[i]} is not in dictionary')
    csvline = [id, name, link, fullmcb]
    return csvline
