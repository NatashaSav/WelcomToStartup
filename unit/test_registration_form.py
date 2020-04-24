import unittest

from selenium import webdriver
import time

class Test_Form_Registration(unittest.TestCase):

   def test_field_form1(self):
       link = "http://suninjuly.github.io/registration1.html"
       browser = webdriver.Chrome()
       browser.get(link)
       input1 = browser.find_element_by_css_selector(".first_block input.form-control.first")
       input1.send_keys("Ivan")
       input2 = browser.find_element_by_css_selector(".first_block input.form-control.second")
       input2.send_keys("Petrov")
       input3 = browser.find_element_by_css_selector(".first_block input.form-control.third")
       input3.send_keys("IvanPetrov@mail.ru")
       button = browser.find_element_by_css_selector("button.btn")
       button.click()

       time.sleep(8)

       welcome_text_elt = browser.find_element_by_tag_name('h1')
       welcome_text = welcome_text_elt.text
       assert "Congratulations! You have successfully registered!" == welcome_text
       self.assertEqual('', '', 'Latin letters must be entered in the field')
       self.assertEqual('', '', 'Latin letters must be entered in the field')
       self.assertEqual('', '', 'Latin letters must be entered in the field')
       self.assertEqual('Congratulations! You have successfully registered!','Congratulations! You have successfully registered!', 'Please fill out this field.')

   def test_field_form2(self):
       link = "http://suninjuly.github.io/registration2.html"
       browser = webdriver.Chrome()
       browser.get(link)

       input1 = browser.find_element_by_css_selector(".first_block input.form-control.first")
       input1.send_keys("Ivan")
       input2 = browser.find_element_by_css_selector(".first_block input.form-control.second")
       input2.send_keys("Petrov")
       input3 = browser.find_element_by_css_selector(".first_block input.form-control.third")
       input3.send_keys("IvanPetrov@mail.ru")
       button = browser.find_element_by_css_selector("button.btn")
       button.click()

       time.sleep(8)

       welcome_text_elt = browser.find_element_by_tag_name('h1')
       welcome_text = welcome_text_elt.text
       assert "Congratulations! You have successfully registered!" == welcome_text
       self.assertEqual('', '', 'Latin letters must be entered in the field')
       self.assertEqual('', '', 'Latin letters must be entered in the field')
       self.assertEqual('', '', 'Latin letters must be entered in the field')
       self.assertEqual('Congratulations! You have successfully registered!',
                        'Congratulations! You have successfully registered!', 'Please fill out this field.')


time.sleep(8)

if __name__ == '__main__':
    unittest.main()


