from time import sleep
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pyautogui as pag


def fax(patient):
    forms = ', '.join(patient["forms"])
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(service=Service())
    driver.get('https://secure.ipfax.net/')
    # Login to the fax service
    driver.find_element(
        by=By.XPATH, value='/html/body/form[1]/div/div[1]/input').send_keys('6233221504')
    driver.find_element(
        by=By.XPATH, value='/html/body/form[1]/div/div[2]/input').send_keys('6233221504!')
    driver.find_element(
        by=By.XPATH, value='/html/body/form[1]/div/div[4]/input').click()
    driver.find_element(
        by=By.XPATH, value='/html/body/form[1]/div/div[5]/div/input').click()

    #  Fill out the fields
    driver.find_element(
        by=By.XPATH, value='/html/body/form[1]/div/div/div[2]/div[1]/div[1]/div/input').send_keys('Medical Records')
    driver.find_element(
        by=By.XPATH, value='/html/body/form[1]/div/div/div[2]/div[1]/div[2]/div/input').send_keys(f'{patient["ptName"]} -- {forms}')
    driver.find_element(
        by=By.XPATH, value='/html/body/form[1]/div/div/div[2]/div[2]/div[1]/div[1]/input').send_keys(patient['fNumber'])
    driver.find_element(
        by=By.XPATH, value='/html/body/form[1]/div/div/div[2]/div[2]/div[1]/div[2]/input').click()
    driver.find_element(
        by=By.XPATH, value='/html/body/form[1]/div/div/div[2]/div[2]/div[7]/button').click()

    # Choose file with PyAutoGui
    sleep(1)
    pag.hotkey('ctrl', 'l')
    pag.write(f'S:\\')
    pag.press('enter')
    sleep(1)
    pag.press('tab', 4, 0.25)
    pag.press('down')
    pag.press('up')
    pag.press('enter')
    # Sleep to allow ipfax to process file
    sleep(2)

    # Send the fax
    driver.find_element(
        by=By.XPATH, value='/html/body/form[1]/div/div/div[2]/div[3]/div[1]/input').click()
    # sleep(5)
    driver.close()


fax({'fNumber': '6233221504', 'ptName': 'Zackery Hatch',
    'forms': ['A1c Tests', 'faxcover']})
# sleep(5)
# print('Done sleeping!')
# driver.close()
