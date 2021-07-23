from selenium import webdriver

class Login:
    textbox_username_id='Email'
    textbox_password_id='Password'
    button_submit_xpath="//div/button[text()='Log in']"
    link_logout_xpath="//li/a[text()='Logout']"

    def __init__(self,driver):
      self.driver=driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickOnLogin(self):
        self.driver.find_element_by_xpath(self.button_submit_xpath).click()

    def clickOnLogout(self):
        self.driver.find_element_by_xpath(self.link_logout_xpath).click()


