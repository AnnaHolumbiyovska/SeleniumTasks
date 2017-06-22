from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def test_page_using_chrome():
    chrome_driver = webdriver.Chrome(ChromeDriverManager().install())
    page_test(chrome_driver)


def test_page_using_firefox():
    firefox_driver = webdriver.Firefox()
    page_test(firefox_driver)


def test_page_using_ie():
    ie_driver = webdriver.Ie(IEDriverManager().install())
    page_test(ie_driver)


def page_test(w_driver):
    page_addr = "http://localhost/litecart"

    w_driver.implicitly_wait(5)
    w_driver.get(page_addr)
    WebDriverWait(w_driver, 3).until(ec.title_is("My Store | Online Store"))

    # Find Campaign Products
    campaign_products = w_driver.find_element_by_xpath("(//*[@id='box-campaign-products'])")
    # Find all items in Campaign Products section
    products = campaign_products.find_elements_by_xpath(".//a[@class='link']")

    # Check properties of the first product on the main page
    m_page_title_val = products[0].find_element_by_xpath("(//*[@class='name'])").text
    m_page_price = products[0].find_element_by_xpath("(//*[@class='price-wrapper'])")
    m_page_regular_price = m_page_price.find_element_by_xpath("(//s[@class='regular-price'])")
    m_page_regular_price_val = m_page_regular_price.text
    m_page_regular_price_color_val = m_page_regular_price.value_of_css_property('color')
    m_page_regular_price_text_decoration_val = m_page_regular_price.value_of_css_property('text-decoration')
    m_page_campaign_price = m_page_price.find_element_by_xpath("(//*[@class='campaign-price'])")
    m_page_campaign_price_val = m_page_campaign_price.text
    m_page_campaign_price_color_val = m_page_campaign_price.value_of_css_property('color')
    m_page_campaign_price_font_weight_val = m_page_campaign_price.value_of_css_property('font-weight')

    # Select first product in Campaigns section
    products[0].click()

    # Check properties on the full page
    f_page_title_val = w_driver.find_element_by_xpath("(//h1[@class='title'])").text
    f_page_price = w_driver.find_element_by_xpath("(//*[@class='price-wrapper'])")
    f_page_regular_price = f_page_price.find_element_by_xpath("(//*[@class='regular-price'])")
    f_page_regular_price_val = f_page_regular_price.text
    f_page_regular_price_color_val = f_page_regular_price.value_of_css_property('color')
    f_page_regular_price_text_decoration_val = f_page_regular_price.value_of_css_property('text-decoration')
    f_page_campaign_price = f_page_price.find_element_by_xpath("(//*[@class='campaign-price'])")
    f_page_campaign_price_val = f_page_campaign_price.text
    f_page_campaign_price_color_val = f_page_campaign_price.value_of_css_property('color')
    f_page_campaign_price_font_weight_val = f_page_campaign_price.value_of_css_property('font-weight')

    # Verifications
    assert (m_page_title_val == f_page_title_val)
    assert (m_page_regular_price_val == f_page_regular_price_val)
    assert (m_page_regular_price_color_val == f_page_regular_price_color_val)
    assert (m_page_regular_price_text_decoration_val == f_page_regular_price_text_decoration_val)
    assert (m_page_campaign_price_val == f_page_campaign_price_val)
    assert (m_page_campaign_price_color_val == f_page_campaign_price_color_val)
    assert (m_page_campaign_price_font_weight_val == f_page_campaign_price_font_weight_val)

    w_driver.quit()