from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
#from selenium.webdriver.common.by import By
import time
import os 
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # input1 = browser.find_element_by_name("firstname")
    # input1.send_keys("Ivan")
    # input2 = browser.find_element_by_name("lastname")
    # input2.send_keys("Petrov")
    # input3 = browser.find_element_by_name("email")
    # input3.send_keys("p@gmail.com")
    # # input4 = browser.find_element_by_id("country")
    # # input4.send_keys("Russia")
    # current_dir = os.path.abspath(os.path.dirname(__file__))
    # file_path = os.path.join(current_dir, 'file.txt')  
    # input4 = browser.find_element_by_id("file")      
    # input4.send_keys(file_path)
    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()
    button1 = browser.find_element_by_id("book")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button1.click()
    # confirm = browser.switch_to.alert
    # confirm.accept()
    # new_window = browser.window_handles[1]
    # browser.switch_to.window(new_window)
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    button2 = browser.find_element_by_id("solve")
    button2.click()
finally:
# закрываем браузер после всех манипуляций
    time.sleep(30)
    browser.quit()