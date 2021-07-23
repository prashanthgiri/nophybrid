import pytest

from pageObjects.SearchCustomerPage import SearchCustomer
from testCases.test_login import Test_001_login as tc1
from pageObjects.LoginPage import Login
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
import time

class Test_003_searchCustomer:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    @pytest.mark.regression
    def test_searchByEmail(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickOnLogin()
        # select customer
        self.ac = AddCustomer(self.driver)
        self.ac.clickCustomerOnMenu()
        self.ac.clickCustomerfromList()

        self.sc=SearchCustomer(self.driver)
        self.sc.searchByEmail("admin@yourStore.com")
