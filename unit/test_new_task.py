import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()



@pytest.mark.parametrize('ref', ["https://stepik.org/lesson/236895/step/1",
                                   "https://stepik.org/lesson/236896/step/1",
                                   "https://stepik.org/lesson/236897/step/1",
                                   "https://stepik.org/lesson/236898/step/1",
                                   "https://stepik.org/lesson/236899/step/1",
                                   "https://stepik.org/lesson/236903/step/1",
                                   "https://stepik.org/lesson/236904/step/1",
                                   "https://stepik.org/lesson/236905/step/1"])

def test_stepik_link(browser, ref):
    link = f"{ref}/"
    browser.get(link)

    answer = math.log(int(time.time()))
    answer_str = str(answer)

    text_el = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#ember69")))
    text_el.send_keys(answer_str)

    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()

    time.sleep(5)
    assert "Correct!" == text_el.text, "NOT CORRECT!"
