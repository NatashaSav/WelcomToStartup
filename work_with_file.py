import os
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

input1 = browser.find_element_by_name('firstname')
input1.send_keys("Nata")
input2 = browser.find_element_by_name('lastname')
input2.send_keys("Savchenko")
input3 = browser.find_element_by_name('email')
input3.send_keys("NataSavch67")


current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
element = browser.find_element_by_css_selector("input#file")
element.send_keys(file_path)
# print(file_path)
button = browser.find_element_by_css_selector("button.btn")
button.click()
button