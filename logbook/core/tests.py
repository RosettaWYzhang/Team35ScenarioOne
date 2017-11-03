from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class SignUpTestCase(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(SignUpTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(SignUpTestCase, self).tearDown()

    def test1_signup(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/signup')
        #find the form element
        first_name = selenium.find_element_by_id('id_first_name')
        last_name = selenium.find_element_by_id('id_last_name')
        username = selenium.find_element_by_id('id_username')
        email = selenium.find_element_by_id('id_email')
        password1 = selenium.find_element_by_id('id_password1')
        password2 = selenium.find_element_by_id('id_password2')

        submit = selenium.find_element_by_css_selector('button[type=submit]')
        time.sleep(3)

        #Fill the form with data
        username.send_keys('unary1')
        time.sleep(1)
        first_name.send_keys('Yusuf')
        time.sleep(1)
        last_name.send_keys('Unary')
        time.sleep(1)
        email.send_keys('yusuf@qawba.com')
        time.sleep(1)
        password1.send_keys('123456')
        time.sleep(1)
        password2.send_keys('123456')
        time.sleep(1)

        #submitting the form
        submit.send_keys(Keys.RETURN)

        #check the returned result
        #assert 'Check your email' in selenium.page_source
    def test2_signin(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/login')
        #find the form element
        username = selenium.find_element_by_id('id_username')
        password = selenium.find_element_by_id('id_password')
        submit = selenium.find_element_by_css_selector('button[type=submit]')

        #Fill the form with data

        username.send_keys('unary1')
        time.sleep(1)
        password.send_keys('123456')
        time.sleep(1)


        #submitting the form
        submit.send_keys(Keys.RETURN)


'''class LoginTestCase(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(LoginTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(LoginTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/login')
        #find the form element
        username = selenium.find_element_by_id('id_username')
        password = selenium.find_element_by_id('id_password')
        submit = selenium.find_element_by_css_selector('button[type=submit]')

        #Fill the form with data

        username.send_keys('unary1')
        time.sleep(1)
        password.send_keys('123456')
        time.sleep(1)


        #submitting the form
        submit.send_keys(Keys.RETURN)

        #check the returned result
        #assert 'Check your email' in selenium.page_source
'''

'''from selenium import webdriver
import time


driver = webdriver.Firefox()
driver.get('http://127.0.0.1:8000/signup')


driver.find_element_by_id("id_username").send_keys("rosetta1")
driver.find_element_by_id("id_password1").send_keys("ucl393939")
driver.find_element_by_id("id_password2").send_keys("ucl393939")
driver.find_element_by_id("id_email").send_keys("temp@gmail.com")
driver.find_element_by_id("id_first_name").send_keys("wanyue")
driver.find_element_by_id("id_last_name").send_keys("zhang")
driver.find_element_by_css_selector("button[type=submit]").click()
driver.find_element_by_xpath("//a[@href='/accounts/login/?next=/logbook/signup']").click()


#driver.get('http://13.81.216.47:8000/logbook')
d#river.implicitly_wait(30)

#driver.find_element_by_id("id_username").send_keys("temp@gmail.com")
#driver.find_element_by_id("id_password").send_keys("ucl393939")
#driver.find_element_by_css_selector("input[type=submit]").click()
#time.sleep(3)
'''
