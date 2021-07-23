import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_login:
    baseUrl= ReadConfig.getApplicationURL()
    username= ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()
    @pytest.mark.sanity
    def test_homepageTitle(self,setup):
        self.logger.info("********************Test_001_Login**************************")
        self.logger.info("********************Verifying Home Page Title**************************")
        self.driver= setup
        self.driver.get(self.baseUrl)
        act_Title=self.driver.title
        self.driver.close()
        if act_Title=='Your store. Login':
            self.logger.info("********************Home Page Title is passed**************************")
            assert True
        else:
            self.logger.info("********************Home Page Title is failed**************************")
            assert False
    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("********************Test_001_Login**************************")
        self.logger.info("********************Verifying Login page**************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickOnLogin()
        act_title=self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("********************Verifying login page title after login**************************")
            #self.driver.close()
            self.logger.info("********************login is sucessful **************************")
            assert True
        else:
            self.driver.save_screenshot(".\\ScreenShots\\"+"test_login.png")
            #self.driver.close()
            self.logger.info("********************login is failed**************************")
            assert False