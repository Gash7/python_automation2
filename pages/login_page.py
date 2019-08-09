from selenium.webdriver.common.keys import Keys

class Login_Page():
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_name = 'email'
        self.password_textbox_name = 'pass'
        self.login_button_id = 'u_0_a'

    def enter_username(self,username):
        print(username)
        # self.driver.find_element_by_name(self.username_textbox_name).clear()
        self.driver.find_element_by_name( self.username_textbox_name).send_keys(username)

    def enter_password(self,password):

        print(password)
        #self.driver.find_element_by_name(self.password_textbox_name).clear()
        self.driver.find_element_by_name( self.password_textbox_name).send_keys(password)

    def login_button(self):
        click = self.driver.find_element_by_id( self.login_button_id)
        click.send_keys(Keys.RETURN)
