from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='C:\\Users\\LabInfo\\Documents\\Ferreira\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

try: 
    driver.get("https://the-internet.herokuapp.com/key_presses?")
    elem = driver.find_element(By.ID, "target")
    # alert = driver.find_element(By.ID, 'result')
    elem.send_keys(Keys.F1)
    # if 'You entered: HYPHEN_MINUS' in alert:
    #     print("foi")
    # else:
    #     print("CARALHOOOOOO")
    elem.send_keys(Keys.BACKSPACE)
    print("teste 1 foi!")

    elem.send_keys(Keys.F2)
    elem.send_keys(Keys.ENTER)
    print("teste 2 ok.")

    elem = driver.find_element(By.ID, "target")
    elem.send_keys(Keys.F3)
    elem.send_keys(Keys.DELETE)
    print("N falhou krlh, amem")
except: 
    print("o teste falhou!")


    
