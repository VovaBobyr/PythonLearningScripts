from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")

if os.name == 'nt':
    is_win = True
else:
    is_win = False

if is_win:
    save_path = 'C:/Learning/Python/DBRealtor/TempFiles/'
    chromedriver_path = 'C:/Inst/chromedriver.exe'
else:
    save_path = '/opt/dbrealtor/temp/'
    chromedriver_path = '/usr/bin/chromedriver'

driver = webdriver.Chrome(
    executable_path=chromedriver_path,
    options=chrome_options)

for counter in range(100):
    inputfile = "../WebPages/strana" + str(counter) + '.html'
    link = 'https://www.sreality.cz/hledani/prodej/byty?strana=' + str(counter)
    driver.get(link)
    with open(inputfile, mode="w", encoding="latin_1") as f:
        f.write(driver.page_source)

driver.close()



