from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager


def test_google_using_chrome():
    pageAddr = "http://localhost/litecart/admin/"
    userName = "admin"
    userPassword = "admin"

    chrome_driver = webdriver.Chrome(ChromeDriverManager().install())
    chrome_driver.get(pageAddr)
    chrome_driver.find_element_by_name("username").send_keys(userName)
    chrome_driver.find_element_by_name("password").send_keys(userPassword)
    chrome_driver.find_element_by_name("login").submit()
    WebDriverWait(chrome_driver, 3).until(ec.title_is("My Store"))
    chrome_driver.quit()

