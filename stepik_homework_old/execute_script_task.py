from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_css_selector("span#input_value")
x = x_element.text
y = calc(x)

browser.execute_script("window.scrollBy(0, 150);")

input1 = browser.find_element_by_id('answer')
input1.send_keys(y)

c_box = browser.find_element_by_id('robotCheckbox')
c_box.click()

r_but = browser.find_element_by_id('robotsRule')
r_but.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()