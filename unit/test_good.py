import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.incremental
class TestUserHandling():
    def test_login(self, browser):
        browser.get("https://stepik.org/lesson/236895/step/1")
    def test_modification(self, browser):
       browser.get("https://stepik.org/lesson/236896/step/1")
    def test_deletion(self, browser):
       browser.get("https://stepik.org/lesson/236897/step/1")


answer = math.log(int(time.time()))
answer_str = str(answer)



text_el = WebDriverWait(browser, 120).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#ember69")))
text_el = browser.find_element_by_css_selector("#ember69")
text_el.send_keys(answer_str)



button = browser.find_element_by_css_selector("button.submit-submission")
button.click()

assert "Correct!" == text_el.text, "NOT CORRECT!"
