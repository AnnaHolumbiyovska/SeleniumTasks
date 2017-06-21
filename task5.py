from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.firefox import GeckoDriverManager
import time


def test_page():
    page_addr = "http://localhost/litecart"

    firefox_driver = webdriver.Firefox()
    firefox_driver.implicitly_wait(5)
    firefox_driver.get(page_addr)
    WebDriverWait(firefox_driver, 3).until(ec.title_is("My Store | Online Store"))

    # Find Campaign Products
    campaign_products = firefox_driver.find_element_by_xpath("(//*[@id='box-campaign-products'])")
    # Find all items in Campaign Products section
    products = campaign_products.find_elements_by_xpath(".//a[@class='link']")

    # Check properties on the main page
    # TODO

    # Select first product in Campaigns section
    products[0].click()

    # Check properties on the full page
    f_page_title_val = firefox_driver.find_element_by_xpath("(//h1[@class='title'])").text
    f_page_price = firefox_driver.find_element_by_xpath("(//*[@class='price-wrapper'])")
    f_page_regular_price = f_page_price.find_element_by_xpath("(//*[@class='regular-price'])")
    f_page_regular_price_val = f_page_regular_price.text
    f_page_regular_price_color_val = f_page_regular_price.value_of_css_property('color')
    f_page_regular_price_text_decoration_val = f_page_regular_price.value_of_css_property('text-decoration')
    f_page_campaign_price = f_page_price.find_element_by_xpath("(//*[@class='campaign-price'])")
    f_page_campaign_price_val = f_page_campaign_price.text
    f_page_campaign_price_color_val = f_page_campaign_price.value_of_css_property('color')
    f_page_campaign_price_font_weight_val = f_page_campaign_price.value_of_css_property('font-weight')

    # Verification
    # TODO

    time.sleep(2)
    firefox_driver.quit()