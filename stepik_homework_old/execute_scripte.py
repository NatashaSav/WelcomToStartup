from selenium import webdriver
browser = webdriver.Chrome()
# 1variant
# browser.execute_script("alert('Robots at work');")
# browser.execute_script("document.title='Script executing';")
# browser.execute_script('document.title="Script executing";')
browser.execute_script("document.title='Script executing';alert('Robots at work');")