from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import clindict
# opening clinrecs
def readclinrec(link):
    driver = webdriver.Chrome()
    driver.get(link)
    wait = WebDriverWait(driver, timeout=6)
    wait.until(lambda _ : driver.find_element(By.CLASS_NAME,'title_content').is_displayed())
    #searching for and making it usable
    content=driver.find_elements(By.CLASS_NAME,'title_content')
    imp=[]
    for line in content:
        imp.append(line.text)
    name=imp[0]
    id=imp[4]
    mcb=sorted(list(set(imp[1].split(', '))))
    #processing mcb 10 designation
    fullmcb=[]
    for i in range(len(mcb)):
        try:
            fullmcb.append(clindict.thisdict[mcb[i]])
        except:
            print(f'mcb-10 designation {mcb[i]} is not in dictionary')
    fullmcb=', '.join(fullmcb)
    csvline=[id,name,link,fullmcb]
    return(csvline)