import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

#Чтобы запустить все тесты, не имеющие заданную маркировку, можно использовать инверсию.
# Для запуска всех тестов, не отмеченных как smoke, нужно выполнить команду: pytest -v -s -m "not smoke" unit/fixut/test_fixture8.py
#Запуск тестов с маркировкой smoke--- pytest -v -s -m smoke unit/fixut/test_fixture8.py
# Для запуска тестов с разными метками можно использовать логическое ИЛИ.
# Запустим smoke и regression-тесты: pytest -s -v -m "smoke or regression" test_fixture8.py
