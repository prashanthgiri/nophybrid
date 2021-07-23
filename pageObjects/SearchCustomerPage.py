from selenium import webdriver
class SearchCustomer:
    textbox_SearchEmail_id = "SearchEmail"
    textbox_SearchFirstName_id = "SearchFirstName"
    btn_searchcustomers_id = "search-customers"
    table_xpath="//table[@id='customers-grid']"
    table_rows_xpath="//table[@id='customers-grid']/tbody/tr"
    table_emailcol1_xpath="//table[@id='customers-grid']/thead/following-sibling::tbody/tr["
    table_emailcol2_xpath="]/td[2]"
    table_namecol1_xpath="//table[@id='customers-grid']/thead/following-sibling::tbody/tr/td["
    table_namecol2_xpath="]"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element_by_id(self.textbox_SearchEmail_id).send_keys(email)

    def setName(self,fname):
        self.driver.find_element_by_id(self.textbox_SearchFirstName_id).send_keys(fname)

    def clickOnSearch(self):
        self.driver.find_element_by_id(self.btn_searchcustomers_id).click()

    def tableRowCount(self):
        return len(self.driver.find_elements_by_xpath(self.table_rows_xpath))

    def searchByEmail(self,email):
        flag=False
        self.setEmail(email)
        self.clickOnSearch()
        for r in range(1,self.tableRowCount()+1):
            table=self.driver.find_element_by_xpath(self.table_xpath)
            email_id=table.find_element_by_xpath("//table[@id='customers-grid']/thead/following-sibling::tbody/tr["+str(r)+"]/td[2]").text
            print(email_id)
            if email_id==email:
                assert True
            else:
                assert False

    def searchByName(self,name):
        self.setName(name)
        self.clickOnSearch()
        self.tableRowCount()
        for r in range(1, self.tableRowCount() + 1):
            name_id = self.driver.find_element_by_xpath(self.table_namecol1_xpath +str(r)+ self.table_namecol2_xpath).text
            if name_id == name:
                assert True
            else:
                assert False






