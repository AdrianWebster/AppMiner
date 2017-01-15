import bs4 as bs
import selenium
from  maine import idPuller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options



def test():
    driver = webdriver.Chrome('chromedriver.exe')

    driver.get('http://www.63eregiment.enjin.com/login')
    input('press enter once logged on to continue')
    driver.get('http://www.63eregiment.enjin.com/dashboard/applications/application?app_id=8408129')
    html = driver.page_source


    soup = bs.BeautifulSoup(html, 'lxml')

    ## gets raw html of form
    for div in soup.find_all("div",class_="form-question-body"):
        print (div)

    ## gets raw html data of the other
    for div in soup.find_all("div",class_="app_header_user_details"):
        print (div)

    ## nco and aprooval ifno
    for div in soup.find_all("div", class_="app_header_user_meta"):
        print(div)

    return

test()