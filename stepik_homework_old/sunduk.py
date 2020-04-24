import math
from selenium import webdriver


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


x_element = browser.find_element_by_css_selector("img#treasure")
x = x_element.get_attribute('valuex')
y = calc(x)

input = browser.find_element_by_css_selector("#answer")
input.send_keys(y)

c_box = browser.find_element_by_id('robotCheckbox')
c_box.click()

r_but = browser.find_element_by_id('robotsRule')
r_but.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()
