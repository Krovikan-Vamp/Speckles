from time import sleep
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pyautogui as pag


def fax(patient):
    faxNo = patient["fNumber"].replace('.', '')
    # forms = ', '.join(patient["forms"])
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(service=Service())
    driver.get('https://secure.ipfax.net/')
    sleep(2)
    # Login to the fax service
    driver.find_element(
        by=By.XPATH, value='/html/body/form[1]/div/div[1]/input').send_keys('6233221504')
    driver.find_element(
        by=By.XPATH, value='/html/body/form[1]/div/div[2]/input').send_keys('6233221504')
    driver.find_element(
        by=By.XPATH, value='/html/body/form[1]/div/div[4]/input').click()
    sleep(2)
    driver.find_element(
        by=By.XPATH, value='/html/body/form[1]/div/div[5]/div/input').click()

    #  Fill out the fields
    driver.find_element(
        by=By.XPATH, value='/html/body/form[1]/div/div/div[2]/div[1]/div[1]/div/input').send_keys('Medical Records')
    driver.find_element(
        by=By.XPATH, value='/html/body/form[1]/div/div/div[2]/div[1]/div[2]/div/input').send_keys(f'{patient["ptName"]} -- {patient["forms"]}')
    driver.find_element(
        by=By.XPATH, value='/html/body/form[1]/div/div/div[2]/div[2]/div[1]/div[1]/input').send_keys(faxNo)
    driver.find_element(
        by=By.XPATH, value='/html/body/form[1]/div/div/div[2]/div[2]/div[1]/div[2]/input').click()
    driver.find_element(
        by=By.XPATH, value='/html/body/form[1]/div/div/div[2]/div[2]/div[7]/button').click()
    sleep(1)
    # Choose file with PyAutoGui
    pag.hotkey('ctrl', 'l')
    pag.write('S:\\')
    pag.press('enter')
    sleep(10)

    # Sleep to allow ipfax to process file
    sleep(2)

    # Send the fax
    driver.find_element(
        by=By.XPATH, value='/html/body/form[1]/div/div/div[2]/div[3]/div[1]/input').click()
    sleep(7)
    driver.close()


fax({"ptName": 'Zackery Hatch', 'fNumber': '',
    "forms": ['Faxcover', 'Anticoagulant']})
