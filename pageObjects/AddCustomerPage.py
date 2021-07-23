from selenium import webdriver

class AddCustomer:
    role_list = []
    link_customeronmenu_xpath="//a[@href='#']/i/following-sibling::p[contains(text(),'Customers')]"
    link_customerlist_xpath='//a[@href="/Admin/Customer/List"]/i/following-sibling::p[contains(text(),"Customers")]'
    link_addnew_xpath="//a[@class='btn btn-primary']"
    email_id="//div/input[@id='Email']"
    password_id="//div/input[@id='Password']"
    firstName_id="//div/input[@id='FirstName']"
    lastName_id="//div/input[@id='LastName']"
    gender_xpath="//div/input[@id='Gender_"
    gender="']"
    genderFemale_id="Gender_Female"
    dateofbirth_id="//span/input[@id='DateOfBirth']"
    companyname_xpath="//div/input[@id='Company']"
    istaxexempt_xpath="//div/input[@id='IsTaxExempt']"
    clickNewsLetter_xpath="//div[@class='input-group-append']/div/div[@class='k-widget k-multiselect k-multiselect-clearable']/div[@role='listbox']"
    selectNewsLetter1_xpath="//ul/li[text()='Your store name']"
    selectNewsLetter2_xpath="//ul/li[text()='Test store 2']"
    deleteRegistered_xpath="//li/span[text()='Registered']/following-sibling::span[@title='delete']"
    multiselectCustomerRoles_xpath="//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    listAdministrator_xpath="//ul[@id='SelectedCustomerRoleIds_listbox']/li[text()='Administrators']"
    listCustomerRoles1_xpath="//ul[@id='SelectedCustomerRoleIds_listbox']/li[text()='"
    listCustomerRoles2_xpath="']"
    listForumModerator_xpath="//ul[@id='SelectedCustomerRoleIds_listbox']/li[text()='Forum Moderators']"
    listGuest_xpath="//ul[@id='SelectedCustomerRoleIds_listbox']/li[text()='Guests']"
    listRegistered_xpath="//ul[@id='SelectedCustomerRoleIds_listbox']/li[text()='Registered']"
    listVendors_xpath="//ul[@id='SelectedCustomerRoleIds_listbox']/li[text()='Vendors']"
    button_save_xpath="//div/button[@name='save']"

    def __init__(self,driver):
      self.driver=driver

    def clickCustomerOnMenu(self):
        self.driver.find_element_by_xpath(self.link_customeronmenu_xpath).click()

    def clickCustomerfromList(self):
        self.driver.find_element_by_xpath(self.link_customerlist_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.link_addnew_xpath).click()

    def setEmailid(self,email):
        self.driver.find_element_by_xpath(self.email_id).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.password_id).send_keys(password)

    def setFirstName(self,fname):
        self.driver.find_element_by_xpath(self.firstName_id).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element_by_xpath(self.lastName_id).send_keys(lname)

    def setGender(self,gendertype):
        self.driver.find_element_by_xpath(self.gender_xpath+gendertype+self.gender).click()

    def setDOB(self,dob):
        self.driver.find_element_by_xpath(self.dateofbirth_id).send_keys(dob)

    def setCompanyName(self,companyname):
        self.driver.find_element_by_xpath(self.companyname_xpath).send_keys(companyname)

    def deleteCustomerRole(self):
        self.driver.find_element_by_xpath(self.deleteRegistered_xpath).click()

    def selectCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.multiselectCustomerRoles_xpath).click()

        self.listitem=self.driver.find_element_by_xpath(self.listCustomerRoles1_xpath+role+self.listCustomerRoles2_xpath)
        self.driver.execute_script("arguments[0].click();",self.listitem)
        self.role_list.append(role)



    def clickSave(self):
        if 'Guests' in self.role_list:
            if 'Registered' in self.role_list:
                self.driver.find_element_by_xpath(self.button_save_xpath).click()
                msg = self.driver.find_element_by_tag_name("body").text
                if "The customer cannot be in both 'Guests' and 'Registered' customer roles" in msg:
                    assert True
                else:
                    assert False
            else:
                self.driver.find_element_by_xpath(self.button_save_xpath).click()
                msg = self.driver.find_element_by_tag_name("body").text
                if 'The new customer has been added successfully.' in msg:
                    assert True
                else:
                    assert False
        else:
            self.driver.find_element_by_xpath(self.button_save_xpath).click()
            msg = self.driver.find_element_by_tag_name("body").text
            if 'The new customer has been added successfully.' in msg:
                assert True
            else:
                assert False






