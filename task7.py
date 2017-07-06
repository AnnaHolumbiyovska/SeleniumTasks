from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


def test_cart_operations():
    page_addr = "http://localhost/litecart/"
    main_page_title = "My Store | Online Store"
    number_of_iteration = 3
    firefox_driver = webdriver.Firefox()
    firefox_driver.implicitly_wait(5)

    for i in range(number_of_iteration):
        firefox_driver.get(page_addr)
        WebDriverWait(firefox_driver, 3).until(ec.title_is(main_page_title))
        quantity_of_items = int(firefox_driver.find_element_by_xpath("(//span[@class='quantity'])").text) + 1

        # find Campaign Products
        campaign_products = firefox_driver.find_element_by_xpath("(//*[@id='box-campaign-products'])")
        # find all items in Campaign Products section
        products = campaign_products.find_elements_by_xpath("//a[@class='link']")
        # select first product in Campaigns section
        products[0].click()

        # go to the full page
        full_page_link = firefox_driver.find_element_by_link_text("View full page")
        full_page_link.click()

        WebDriverWait(firefox_driver, 3).until(ec.title_is("Yellow Duck | Subcategory | Rubber Ducks | My Store"))
        # select at least two different items
        if i == 1:
            size = firefox_driver.find_element_by_css_selector('select[class ="form-control"] option[value="Small"]')
        else:
            size = firefox_driver.find_element_by_css_selector('select[class ="form-control"] option[value="Medium"]')
        size.click()

        add_to_cart_btn = firefox_driver.find_element_by_xpath("//button[@name='add_cart_product']")
        add_to_cart_btn.click()

        WebDriverWait(firefox_driver, 2).until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, 'span[class="quantity"]'), str(quantity_of_items)))

    # open the Cart
    cart_btn = firefox_driver.find_element_by_xpath("//div[@id='cart']")
    cart_btn.click()

    # remove items one by one
    item_table = firefox_driver.find_element_by_css_selector('table[class="items table table-striped data-table"]')
    remove_btns = item_table.find_elements_by_css_selector('button[name="remove_cart_item"]')

    while len(remove_btns) > 0:
        remove_btns[0].click()
        WebDriverWait(firefox_driver, 3).until(ec.staleness_of(remove_btns[0]))
        remove_btns = firefox_driver.find_elements_by_css_selector('button[name="remove_cart_item"]')

    assert(firefox_driver.find_element_by_xpath("//em").text == "There are no items in your cart.")
    firefox_driver.quit()