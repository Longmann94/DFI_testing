import unittest
import time
import HtmlTestRunner
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


cwd = os.getcwd()+'/results'

print("Please do not use the computer while the tests are running to ensure correct results") 
print("Your test results will be created inside: " + cwd)
print("This test will also create screenshots of each test ran inside the current folder: " + os.getcwd())
#     url = input("Please enter website version to test when you are ready: ")

url = "https://www.dfiinfo.com.au/beta-2-0-3k/"

class Test_setUp_menu_buttons(unittest.TestCase):   
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        
    #@unittest.skip("skip")
  
        
    def test_TC_BigType_01_checkboxClick(self):
        driver = self.driver
        driver.get(url)
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='firsttime']/div[2]/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='wrapper']/div[8]/div/button/div[2]").click()
        driver.find_element_by_id("setupContainer").click()
        driver.find_element_by_xpath("//div[@id='illness-select']/div/a/label").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//div[@id='illness-select']/ul/li[2]/a/label").click()
        driver.find_element_by_xpath("//img[@alt='setup icon']").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//button[@id='setupUp']/div[2]").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//button[@id='setupUp']/div[2]").click()
        driver.find_element_by_xpath("//img[@alt='Seeing clearly']").click()
        driver.find_element_by_xpath("//div[@id='setup2']/ul/div[4]/li/label/span").click()      
        time.sleep(2)
        self.assertTrue(driver.find_element_by_id("bigtype").is_selected())
        driver.save_screenshot('SC_TC_BigType_01_checkboxClick.png')
        
        
              
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDFI_Search']
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=cwd))