from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os


def add_product(w_driver):
    # product parameters
    status_val = True
    code_val = 12345
    name_val = 'Dog'
    img_name_val = 'dogImg.jpg'
    quantity_val = 100
    gender_val = 'unisex'
    weight_val = 300
    date_valid_from_val = '2017-06-27'
    date_valid_to_val = '2018-06-27'
    keywords_val = "key words"
    short_description_val = "short description"
    description_val = "description"
    attributes_val = "attributes"
    head_title_val = "head title"
    meta_descr_val = "meta description"
    purchase_price_val = 100
    prices_usd_val = 85
    prices_eur_val = 77

    # Go to the Catalog page
    catalog_menu = w_driver.find_element_by_link_text("Catalog")
    catalog_menu.click()

    # Go to the Add New Product page
    new_product = w_driver.find_element_by_link_text("Add New Product")
    new_product.click()

    # Fill fields on General tab
    if status_val:
        enable_button = w_driver.find_element_by_css_selector('label[class="btn btn-default"]')
        enable_button.click()

    code_field = w_driver.find_element_by_css_selector('input[name="code"]')
    code_field.send_keys(code_val)

    name_field = w_driver.find_element_by_css_selector('input[name="name[en]"]')
    name_field.send_keys(name_val)

    quantity_field = w_driver.find_element_by_css_selector('input[name="quantity"]')
    quantity_field.send_keys(quantity_val)

    img_field = w_driver.find_element_by_css_selector('input[name="new_images[]"]')
    img_field.send_keys(os.path.abspath(img_name_val))

    if gender_val == 'male':
        gender = w_driver.find_element_by_css_selector('div[class=form-group] input[value="1-1"]')
    elif gender_val == 'female':
        gender = w_driver.find_element_by_css_selector('div[class=form-group] input[value="1-2"]')
    else:
        gender = w_driver.find_element_by_css_selector('div[class=form-group] input[value="1-3"]')
    gender.click()

    weight_field = w_driver.find_element_by_css_selector('input[class="form-control"][name="weight"]')
    weight_field.clear()
    weight_field.send_keys(weight_val)

    date_valid_from_field = w_driver.find_element_by_css_selector("input[name='date_valid_from']")
    date_valid_from_field.send_keys(date_valid_from_val)
    date_valid_to_field = w_driver.find_element_by_css_selector("input[name='date_valid_to']")
    date_valid_to_field.send_keys(date_valid_to_val)

    # Fill fields on Information tab:
    inform_tab = w_driver.find_element_by_css_selector('ul[class="nav nav-tabs"] a[href="#tab-information"]')
    inform_tab.click()

    manufacturer_field = w_driver.find_element_by_css_selector('select[name="manufacturer_id"] option[value="1"]')
    manufacturer_field.click()

    keywords_field = w_driver.find_element_by_css_selector('input[name="keywords"]')
    keywords_field.send_keys(keywords_val)

    short_description_field = w_driver.find_element_by_css_selector('input[name="short_description[en]"]')
    short_description_field.send_keys(short_description_val)

    description_field = w_driver.find_element_by_css_selector('div[class="row"] div[class="trumbowyg-editor"]')
    description_field.send_keys(description_val)

    attributes_field = w_driver.find_element_by_css_selector('div[class="row"] textarea[name="attributes[en]"]')
    attributes_field.send_keys(attributes_val)

    head_title_field = w_driver.find_element_by_css_selector('input[name="head_title[en]"]')
    head_title_field.send_keys(head_title_val)

    meta_description_field = w_driver.find_element_by_css_selector('input[name="meta_description[en]"]')
    meta_description_field.send_keys(meta_descr_val)

    # Fill fields on Prices tab:
    inform_tab = w_driver.find_element_by_css_selector('ul[class="nav nav-tabs"] a[href="#tab-prices"]')
    inform_tab.click()

    purchase_price_field = w_driver.find_element_by_css_selector('div[class="input-group"] input[name="purchase_price"]')
    purchase_price_field.clear()
    purchase_price_field.send_keys(purchase_price_val)

    purchase_price_currency_code_field = w_driver.find_element_by_css_selector('select[name="purchase_price_currency_code"] option[value="USD"]')
    purchase_price_currency_code_field.click()

    prices_usd_field = w_driver.find_element_by_css_selector('div[class="input-group"] input[name="prices[USD]"]')
    prices_usd_field.clear()
    prices_usd_field.send_keys(prices_usd_val)

    prices_eur_field = w_driver.find_element_by_css_selector('div[class="input-group"] input[name="prices[EUR]"]')
    prices_eur_field.clear()
    prices_eur_field.send_keys(prices_eur_val)

    submit_btn = w_driver.find_element_by_css_selector('p[class="btn-group"] button[type="submit"]')
    submit_btn.click()

    catalog_form = w_driver.find_element_by_css_selector('form[name="catalog_form"]')
    added_product = catalog_form.find_element_by_link_text(name_val)


def test_add_new_item():
    # Credentials
    page_addr = "http://localhost/litecart/admin/"
    user_name = "admin"
    user_password = "admin"

    firefox_driver = webdriver.Firefox()
    firefox_driver.implicitly_wait(5)
    firefox_driver.get(page_addr)
    firefox_driver.find_element_by_name("username").send_keys(user_name)
    firefox_driver.find_element_by_name("password").send_keys(user_password)
    firefox_driver.find_element_by_name("login").submit()
    WebDriverWait(firefox_driver, 3).until(ec.title_is("My Store"))

    add_product(firefox_driver)