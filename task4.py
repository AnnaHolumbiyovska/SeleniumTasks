from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.firefox import GeckoDriverManager

def test_menu():
    pageAddr = "http://localhost/litecart/admin/"
    userName = "admin"
    userPassword = "admin"

    firefox_driver = webdriver.Firefox()
    firefox_driver.implicitly_wait(5)
    firefox_driver.get(pageAddr)
    firefox_driver.find_element_by_name("username").send_keys(userName)
    firefox_driver.find_element_by_name("password").send_keys(userPassword)
    firefox_driver.find_element_by_name("login").submit()
    WebDriverWait(firefox_driver, 3).until(ec.title_is("My Store"))

    links = firefox_driver.find_elements_by_css_selector("li[id='app-']")
    for i in range(len(links)):
        links = firefox_driver.find_elements_by_css_selector("li[id='app-']")
        links[i].click()

        sublinks = firefox_driver.find_elements_by_css_selector(".docs li")
        if len(sublinks) != []:
            for s in range(len(sublinks)):
                sublinks[s].click()
                assert len(firefox_driver.find_elements_by_tag_name('h1')) == 1
        else:
            assert len(firefox_driver.find_elements_by_tag_name("h1")) == 1
    firefox_driver.quit()