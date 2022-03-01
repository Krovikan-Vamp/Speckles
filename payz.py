from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import date as dt
from colorama import Fore, Style
import chromedriver_autoinstaller

information = {
    "total": input(f"Enter the {Fore.RED}order amount{Style.RESET_ALL}: "),
    "cardholder": input(f"{Fore.RED}Cardholder{Style.RESET_ALL} name: "),
    "custName": input(f"{Fore.RED}Patient{Style.RESET_ALL} name: "),
    "cardNo": input(f"Card {Fore.RED}number{Style.RESET_ALL}: "),
    "expM": int(input(f"Expiration {Fore.RED}month{Style.RESET_ALL}: ")),
    "expY": int(input(f"Expiration {Fore.RED}year{Style.RESET_ALL}: ")),
    "refNo": dt.today().strftime("%m%d%Y")
}

print(information)


def chrome(pt):
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(service=Service())
    driver.get('https://globalgatewaye4.firstdata.com/')

    # Login and navigate to POS
    driver.find_element(
        by=By.XPATH, value='/html/body/div[1]/div[1]/div/div[2]/div/div/form/fieldset/ul/li[1]/input').send_keys('')
    driver.find_element(
        by=By.XPATH, value='/html/body/div[1]/div[1]/div/div[2]/div/div/form/fieldset/ul/li[2]/input').send_keys('')
    driver.find_element(
        by=By.XPATH, value='/html/body/div[1]/div[1]/div/div[2]/div/div/form/fieldset/div/input').click()
    sleep(2)
    driver.find_element(
        by=By.XPATH, value='/html/body/div[1]/div[1]/div[2]/div[1]/div/div[4]/ul/li[2]/a').click()

    # Enter the information to the form...
    driver.find_element(by=By.XPATH, value='')
    driver.find_element(by=By.XPATH, value='')
    driver.find_element(by=By.XPATH, value='')
    driver.find_element(by=By.XPATH, value='')
    while True:
        pass


chrome(information)
