from selenium import webdriver
import time
from main import submit

stad = submit()


# find the amount of houses
def aantal_woningen_zoekopdracht(stad, minprijs, maxprijs):
    CHROME_DRIVER_PATH = "C:\Develpment\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    driver.get(f'https://www.pararius.nl/huurwoningen/{stad}/{minprijs}-{maxprijs}')
    get_number_of_woningen = driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div[2]/div/div[1]/span')
    aantal_woningen = int(get_number_of_woningen.text)
    print(aantal_woningen)
    return aantal_woningen
