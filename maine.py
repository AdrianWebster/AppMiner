import bs4 as bs
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def idPuller():
    # parse through the 4 html documents and export data-id to array.
    # ()->(ARRAY)

    temp = []

    '''
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
    sauce4 = open("HTML/quicktest.html", encoding='utf8')
    soup4 = bs.BeautifulSoup(sauce4, 'lxml')

    for a in soup4.find_all('a', href=True):
        temp.append(a['href'])

    return temp

def clean(x):
    applicants = x
    data=[]
    #escapes.append([chr(char) for char in range(1, 32)])

    for i in range(len(applicants)):
            current = applicants[i]
            soup = bs.BeautifulSoup(current, 'lxml')

            #
            #
            # for form in soup.find_all("div", class_="form-question-body"):
            #     form = form.text.strip('\n').strip('  ').strip('%s\n')
            #     temp.append(form)
            #

            temp = []
            for fields in soup.find_all("div", {'class':[' element_username', 'href','app_header_user_ip','input','input-data','app_header_user_status']}):

                fields = fields.text
                temp.append(fields)



            attendance = []
            for check in soup.find_all("div", class_="chk"):
                for box in check:
                    if 'checked' in str(box):
                        if 'Monday' in str(box):
                            attendance.append('Monday')
                        elif 'Tuesday' in str(box):
                            attendance.append('Tuesday')
                        elif 'Wednesday' in str(box):
                            attendance.append('Wednesday')
                        elif 'Thursday' in str(box):
                            attendance.append('Thursday')
                        elif 'Friday' in str(box):
                            attendance.append('Friday')
                        elif 'Saturday' in str(box):
                            attendance.append('Saturday')
                        elif 'Sunday' in str(box):
                            attendance.append('Sunday')
            temp.append(attendance)
            data.append(temp)
            #print (temp)
    return data

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
        html = driver.page_source
        soup = bs.BeautifulSoup(html, 'lxml')

        temp=[]

        ## gets raw html data of the user
        for deets in soup.find_all("div", class_="app_header_user_details"):
            temp.extend(deets)

        ## GETS ATTENDANCE
        for check in soup.find_all("div", class_="chk"):
            for box in check:
                if 'checked="checked"' in str(box):
                    temp.extend(box)

        ## get raw html of form
        for form in soup.find_all("div", class_="form-question-body"):
            temp.extend(form)


        ## nco and aprooval ifno
        for nco in soup.find_all("div", class_="app_header_user_meta"):
            temp.extend(nco)

        # # add temp array to main array
        temp = str(temp)
        people.append(temp)

    return people


print('Welcome')
input('Press ENTER to begin...')
raws = idPuller()
applicants = urlParse(raws)
data = clean(applicants)
for i in range(len(data)):
    print (data[i])


print('Done')
