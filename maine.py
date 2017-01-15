import bs4 as bs
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def idPuller():
    # parse through the 4 html documents and export data-id to array.
    # ()->(ARRAY)

    temp = []

    ''' # only look at open apps for now
    # APPROVED APPS
    sauce1 = open("HTML/approved.html", encoding='utf8')
    soup1 = bs.BeautifulSoup(sauce1, 'lxml')

    for a in soup1.find_all('a', href=True):
        temp.append( a['href'])

    # ARCHIVED APPS
    sauce2 = open("HTML/archived.html", encoding='utf8')
    soup2 = bs.BeautifulSoup(sauce2, 'lxml')

    for a in soup2.find_all('a', href=True):
        temp.append(a['href'])

    # REJECT4ED APPS
    sauce3 = open("HTML/rejected.html", encoding='utf8')
    soup3 = bs.BeautifulSoup(sauce3, 'lxml')

    for a in soup3.find_all('a', href=True):
        temp.append(a['href'])
    '''

    # OPEN APPS
    sauce4 = open("HTML/open.html", encoding='utf8')
    soup4 = bs.BeautifulSoup(sauce4, 'lxml')

    for a in soup4.find_all('a', href=True):
        temp.append(a['href'])

    return temp


def pull(x):
    temp = []

    # returns an array with all the info provided by the current chrome page
    soup = bs.BeautifulSoup(x, 'lxml')

    # parse each category and append to info
    mydivs = soup.findAll("div", {"class": "form-question-body"})
    soup.find_all('div','class="form-question-body')

    temp.append(name='')
    temp.append(ip='')
    temp.append(appdate='')
    temp.append(status='')
    temp.append(game='')
    temp.append(firstreg='')
    temp.append(why='')
    temp.append(age='')
    temp.append(live='')
    temp.append(software='')
    temp.append(rules='')
    temp.append(events='')
    temp.append(findout='')
    temp.append(fother='')
    temp.append(steam='')
    temp.append(nco='')
    temp.append(acceptdate='')

    return temp


def urlParse(array):
    # go through every applicant via chrome and pull the required info, return a 2d array  of every applicant and their info. [[app1],[app2],[app3]]

    people = []
    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-data-dir=C:\\Users\Adrian\AppData\Local\Google\Chrome\\User Data\Default")  # Path to your chrome profile
    driver = webdriver.Chrome('chromedriver.exe')

    driver.get('http://www.63eregiment.enjin.com/login')
    input('press enter once logged on to continue')

    for applicant in array:
        navTo = 'http://www.63eregiment.enjin.com/' + applicant

        # navigate to page
        driver.get(navTo)

        # pull info into temp array
        html = driver.page_source
        temp = pull(html)

        # # add temp array to main array
        people.append(temp)

    return people


print('Welcome')
input('Press ENTER to begin...')
raws = idPuller()
applicants = urlParse(raws)

for i in range(len(applicants)):
    print(applicants[i])

print('Done')
