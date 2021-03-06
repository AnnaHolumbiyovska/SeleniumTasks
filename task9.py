from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import time


class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        print(by, value)

    def after_find(self, by, value, driver):
        print(by, value)

    def on_exception(self, exception, driver):
        print(exception)
        driver.get_screenshot_as_file('img' + str(round(time.time() * 1000)) + '.png')


def test_menu():
    page_addr = "http://localhost/litecart/admin/"
    user_name = "admin"
    user_password = "admin"

    firefox_driver = EventFiringWebDriver(webdriver.Firefox(), MyListener())
    firefox_driver.implicitly_wait(2)
    firefox_driver.get(page_addr)
    firefox_driver.find_element_by_name("username").send_keys(user_name)
    firefox_driver.find_element_by_name("password").send_keys(user_password)
    firefox_driver.find_element_by_name("login").submit()
    WebDriverWait(firefox_driver, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'ul[id="box-apps-menu"]')))

    links = firefox_driver.find_elements_by_css_selector("li[id='app-']")
    assert len(links)
    for i in range(len(links)):
        links = firefox_driver.find_elements_by_css_selector("li[id='app-']")
        links[i].click()
        WebDriverWait(firefox_driver, 3).until(ec.staleness_of(links[i]))

        try:
            is_sub_menu_present = WebDriverWait(firefox_driver, 0.5).until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'li[id^="doc-"]')))
        except:
            is_sub_menu_present = False

        if is_sub_menu_present:
            sublinks = firefox_driver.find_elements_by_css_selector(".docs li")

            if len(sublinks):
                for s in range(len(sublinks)):
                    sublinks = firefox_driver.find_elements_by_css_selector(".docs li")
                    sublinks[s].click()
                    WebDriverWait(firefox_driver, 3).until(ec.staleness_of(sublinks[s]))
                    assert len(firefox_driver.find_elements_by_tag_name('h1')) == 1
            else:
                assert len(firefox_driver.find_elements_by_tag_name("h1")) == 1
    firefox_driver.quit()