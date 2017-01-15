from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\Adrian\AppData\Local\Google\Chrome\\User Data\Default") #Path to your chrome profile
driver = webdriver.Chrome('chromedriver.exe',chrome_options=options)

driver.get('http://www.63eregiment.enjin.com/dashboard/applications/application?app_id=8417689')

