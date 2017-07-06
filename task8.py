from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


def test_links():
    page_addr = "http://localhost/litecart/admin/"
    user_name = "admin"
    user_password = "admin"

    firefox_driver = webdriver.Firefox()
    firefox_driver.implicitly_wait(5)
    firefox_driver.get(page_addr)
    firefox_driver.find_element_by_name("username").send_keys(user_name)
    firefox_driver.find_element_by_name("password").send_keys(user_password)
    firefox_driver.find_element_by_name("login").submit()
    WebDriverWait(firefox_driver, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'ul[id="box-apps-menu"]')))

    firefox_driver.find_element_by_link_text('Countries').click()
    firefox_driver.find_element_by_link_text("Add New Country").click()

    ext_links = firefox_driver.find_elements_by_css_selector('i[class="fa fa-external-link"]')
    assert (len(ext_links))

    main_window = firefox_driver.current_window_handle
    count_of_opened_windows = len(firefox_driver.window_handles)

    for ext_link in ext_links:
        opened_windows = firefox_driver.window_handles
        ext_link.click()
        WebDriverWait(firefox_driver, 5).until(ec.new_window_is_opened(opened_windows))
        count_of_opened_windows += 1
        assert (len(firefox_driver.window_handles) == count_of_opened_windows)
        # switch to just opened window
        firefox_driver.switch_to.window(firefox_driver.window_handles[count_of_opened_windows - 1])
        firefox_driver.close()
        count_of_opened_windows -= 1
        assert (len(firefox_driver.window_handles) == count_of_opened_windows)

        firefox_driver.switch_to.window(main_window)

    firefox_driver.quit()