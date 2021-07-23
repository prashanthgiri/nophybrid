import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.ExcelUtils import ExcelReadWriteCount as excutil

class Test_002_login_DDT:
    baseUrl= ReadConfig.getApplicationURL()
    path=".\\TestData\logintestdata.xlsx" # path of excel test data sheet
    rowsize=excutil.rowCount(path,'loginCredentials')
    #print("Total rows in excel sheet:"+rowsize)
    actual_values = []
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("********************Test_002_Login_DDT**************************")
        self.logger.info("********************Verifying Login page**************************")
        self.driver = setup

        for r in range(2,self.rowsize+1):
            self.driver.get(self.baseUrl)
            self.lp = Login(self.driver)
            self.uname=excutil.readExcelData(self.path,'loginCredentials',r,1)
            self.pwd=excutil.readExcelData(self.path, 'loginCredentials', r, 2)
            self.exp=excutil.readExcelData(self.path, 'loginCredentials', r, 3)
            self.lp.setUserName(self.uname)
            self.lp.setPassword(self.pwd)
            self.lp.clickOnLogin()

            act_title = self.driver.title
            if act_title == "Dashboard / nopCommerce administration":
                self.logger.info("********************Verifying login page title after login**************************")
                if self.exp=='pass':
                    self.logger.info("valid test data")
                    self.actual_values.append("pass")
                    excutil.writeExcelData(self.path,'loginCredentials',r,4,'pass')
                    print("login verified")
                    self.lp.clickOnLogout()
                    #self.driver.close()
                elif self.exp=='fail':
                    self.logger.info("invalid test data")
                    self.actual_values.append("fail")
                    excutil.writeExcelData(self.path, 'loginCredentials', r, 4, 'fail')
                    self.lp.clickOnLogout()
                    #self.driver.close()
            elif act_title != "Dashboard / nopCommerce administration":
                self.logger.info("********************Verifying login page title after login**************************")
                if self.exp=='pass':
                    self.logger.info("invalid test data")
                    self.actual_values.append("fail")
                    excutil.writeExcelData(self.path, 'loginCredentials', r, 4, 'fail')
                    #self.driver.close()
                elif self.exp=='fail':
                    self.logger.info("valid test data")
                    self.actual_values.append("pass")
                    excutil.writeExcelData(self.path, 'loginCredentials', r, 4, 'pass')
                    #self.driver.close()

        if 'fail' not in self.actual_values:
            self.logger.info("Data driven test cases are passed")
            excutil.writeExcelData(self.path, 'loginCredentials', r, 5, 'pass')
            self.driver.close()
            assert True
        else:
            self.logger.info("Data driven test cases are failed")
            excutil.writeExcelData(self.path, 'loginCredentials', r, 5, 'fail')
            self.driver.close()
            assert False
        self.logger.info("********* End of Data driven test *********")