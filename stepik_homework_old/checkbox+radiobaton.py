import math
from selenium import webdriver


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


x_element = browser.find_element_by_css_selector(".form-group #input_value")
#- подбираем селектор для нахождения элемента, который содержит значение x на странице
x = x_element.text
#- получаем текстовое значение этого элемента
y = calc(x)
#- подставляем значение x в функцию calc()

input = browser.find_element_by_id('answer')
input.send_keys(y)

c_box = browser.find_element_by_id('robotCheckbox')
c_box.click()

r_but = browser.find_element_by_id('robotsRule')
r_but.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()
