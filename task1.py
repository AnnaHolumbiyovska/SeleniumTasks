from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager


def test_google_using_chrome():
    chrome_driver = webdriver.Chrome(ChromeDriverManager().install())
    chrome_driver.get("http://google.com")
    chrome_driver.find_element_by_name("q").send_keys("webdriver")
    chrome_driver.find_element_by_name("btnG").click()
    WebDriverWait(chrome_driver, 3).until(ec.title_is("webdriver - Поиск в Google"))
    chrome_driver.quit()


def test_google_using_firefox():
    firefox_driver = webdriver.Firefox()
    firefox_driver.get("http://google.com")
    firefox_driver.find_element_by_name("q").send_keys("webdriver")
    firefox_driver.find_element_by_name("btnG").click()
    WebDriverWait(firefox_driver, 3).until(ec.title_is("webdriver - Поиск в Google"))
    firefox_driver.quit()