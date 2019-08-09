import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pages.login_page import Login_Page
from utils import utils
#D:\Selenium\python_automation2\utils
#D:\Selenium\python_automation2\pages

class Test_Login():
    #Sample automation project
    @pytest.fixture(scope='session')
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        #driver = webdriver.Firefox(executable_path='../drivers/geckodriver.exe')
        # driver = webdriver.Ie(executable_path='../drivers/IEDriverServer.exe')
        # login = Login_Page(driver)
        # login.enter_username('9890449707')
        # login.enter_password('Ashu@022')
        # login.login_button()
        driver.implicitly_wait(10)
        yield

    def test_login(self,test_setup):
        driver.get(utils.URL)
        driver.implicitly_wait(10)
        login = Login_Page(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        driver.implicitly_wait(10)
        login.login_button()
        driver.maximize_window()
        # driver.find_element_by_name('email').send_keys('9890449707')
        # driver.find_element_by_name("pass").send_keys('Ashu@022')
        # driver.find_element_by_id("u_0_a").click()
        #click.send_keys(Keys.RETURN)

    def test_teardown(self):
        driver.set_script_timeout(7)
        time.sleep(5)
        #driver.close()
        #driver.quit()
        print('All sucessfully executed')


if __name__ == '__main__':
    pytest.main()


'''
python -m pytest 
{ Run all test cases persent in the folder }

python -m pytest --html=reports/report1.html
{only for html+css report}

python -m pytest --html=reports/report1.html --self-contained-html
{only for html reports - without css}
'''