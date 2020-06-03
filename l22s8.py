from selenium import webdriver
#from selenium.webdriver.common.by import By
import time
import os 

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("p@gmail.com")
    # input4 = browser.find_element_by_id("country")
    # input4.send_keys("Russia")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')  
    input4 = browser.find_element_by_id("file")      
    input4.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
# закрываем браузер после всех манипуляций
    time.sleep(30)
    browser.quit()