from selenium import webdriver
#from selenium.webdriver.common.by import By
import time
try:
    link = "http://suninjuly.github.io/find_xpath_form"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_xpath("//button[@type='submit']")
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button.click()
finally:
# закрываем браузер после всех манипуляций
    time.sleep(30)
    browser.quit()