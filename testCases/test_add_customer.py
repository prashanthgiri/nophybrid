import random
import string

import pytest
from selenium import webdriver
from testCases.test_login import Test_001_login as tc1
from pageObjects.LoginPage import Login
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
import time

class Test_002_AddCustomer:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickOnLogin()

        self.ac=AddCustomer(self.driver)
        self.ac.clickCustomerOnMenu()
        self.ac.clickCustomerfromList()
        self.ac.clickOnAddNew()
        self.email=random_customer()+"@gmail.com"
        self.ac.setEmailid(self.email)
        self.ac.setPassword("klkoijk")
        self.ac.setFirstName(random_customer())
        self.ac.setLastName("kio")
        self.ac.setGender("Female")

        self.ac.deleteCustomerRole()
        #self.ac.selectCustomerRoles('Registered')
        self.ac.selectCustomerRoles('Vendors')
        self.ac.selectCustomerRoles('Administrators')
        self.ac.selectCustomerRoles('Guests')
        time.sleep(5)
        self.ac.clickSave()

def random_customer(N=8,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(N))