import json
import time
from secret import url
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def headless():
    options = Options()
    options.headless = True
    return options

def startDriver():
    # Start headless
    driver = webdriver.Firefox(options=headless(),executable_path='/home/skaarfacee/Apps/WebDrivers/geckodriver',timeout=1,service_log_path='logs/geckodriver.log')
    #Start with head
    # driver = webdriver.Firefox(executable_path='/home/skaarfacee/Apps/WebDrivers/geckodriver',timeout=5,service_log_path='logs/geckodriver.log')
    driver.get(url)
    return driver

def shutDown(node):
    node.close()

def scrollToEnd(node):
    node.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    return

def clickLoad(node):
    WebDriverWait(node, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='content-block content-block-full']/a[@id='loadMore']/span[@class='button-lightblue']"))).click()
    return

def getNames(node):
    cart=[]
    for element in node.find_elements_by_xpath("//div[@class='pokemon-info']/h5"):
        cart.append(element.get_attribute("innerHTML"))
    return cart

def getSrc(node):
    cart=[]
    for element in node.find_elements_by_xpath("//figure/a/img"):
        cart.append(element.get_attribute("src"))
    return cart

def makeJson(names,urls):
    return dict(zip(names,urls))

def clearPath(node):
    element = node.find_element_by_xpath("//a[@href='/us/pokemon-tcg/']")
    node.execute_script("arguments[0].style.visibility='hidden'", element)
    element = node.find_element_by_xpath("//li[@class='play']")
    node.execute_script("arguments[0].style.visibility='hidden'", element)
    element = node.find_element_by_xpath("//nav[@class='main']")
    node.execute_script("arguments[0].style.visibility='hidden'", element)

    return

if __name__=='__main__':
    print("RUNNING")
    driver=startDriver()
    clearPath(driver)
    scrollToEnd(driver)
    clickLoad(driver)
    for i in range(0,3):
        time.sleep(1)
        scrollToEnd(driver)
    print("----SCROLL OVER----")
    driver.implicitly_wait(3)
    print("----MAKING JSON----")
    with open("data.json", "w") as outfile:
        json.dump(makeJson(getNames(driver),getSrc(driver)), outfile)
    print("----COMPLETE---")
    shutDown(driver)