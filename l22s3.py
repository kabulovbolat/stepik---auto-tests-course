from selenium import webdriver
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By
import time
import math

def calc(x,y):
    return str(int(x)+int(y))

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    z = calc(x,y)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)
   # input1 = browser.find_element_by_id("answer")
    #input1.send_keys(y)
    #option1 = browser.find_element_by_id("robotCheckbox")
    #option1.click()
    #option2 = browser.find_element_by_id("robotsRule")
    #option2.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()