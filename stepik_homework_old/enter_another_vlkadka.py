from selenium import webdriver
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)
window_before = browser.window_handles[0]
button = browser.find_element_by_tag_name("button")
button.click()

window_after = browser.window_handles[1]
browser.switch_to_window(window_after)


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


x_element = browser.find_element_by_css_selector("span#input_value")
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_id('answer')
input1.send_keys(y)
button = browser.find_element_by_css_selector("button.btn")
button.click()