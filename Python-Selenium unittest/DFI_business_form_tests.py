import unittest
import time
import random
import string
import HtmlTestRunner
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

cwd = os.getcwd()+'/results' 

url = "https://www.dfiinfo.com.au/beta-2-0-3i/"
business_url = "https://www.dfiinfo.com.au/beta-2-0-3i/login"


class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()


    def test_TC_BusinessFrom_01(self):
        driver = self.driver
        driver.get(business_url)
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("user1")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("pass1")
        driver.find_element_by_id("password").send_keys(Keys.ENTER)
        time.sleep(4)
        driver.find_element_by_name("nf_bizname").click()
        driver.find_element_by_name("nf_bizname").clear()
        driver.find_element_by_name("nf_bizname").send_keys("Long's Lucky PC Store 1994")
        driver.find_element_by_name("nf_bizstreet").click()
        driver.find_element_by_name("nf_bizstreet").clear()
        driver.find_element_by_name("nf_bizstreet").send_keys("199 main street")
        driver.find_element_by_name("nf_bizsuburb").click()
        driver.find_element_by_name("nf_bizsuburb").clear()
        driver.find_element_by_name("nf_bizsuburb").send_keys("mornington")
        driver.find_element_by_id("nf_level").click()
        Select(driver.find_element_by_id("nf_level")).select_by_visible_text("Level 10")
        driver.find_element_by_id("nf_category").click()
        Select(driver.find_element_by_id("nf_category")).select_by_visible_text("Electronics")
        driver.find_element_by_name("nf_shopCentre").click()
        Select(driver.find_element_by_name("nf_shopCentre")).select_by_visible_text("Mornington Central")
        driver.find_element_by_xpath("//form[@id='stageone']/div/div[3]/div[2]/div/a[2]").click() # default time 9am - 5pm
        driver.find_element_by_xpath("//form[@id='stageone']/div/div[4]/div[2]/div/a[2]").click()
        driver.find_element_by_xpath("//form[@id='stageone']/div/div[5]/div[2]/div/a[2]").click()
        driver.find_element_by_xpath("//form[@id='stageone']/div/div[6]/div[2]/div/a[2]").click()
        driver.find_element_by_xpath("//form[@id='stageone']/div/div[7]/div[2]/div/a[2]").click()
        driver.find_element_by_xpath("//form[@id='stageone']/div/div[8]/div[2]/div/a[2]").click()
        driver.find_element_by_xpath("//form[@id='stageone']/div/div[9]/div[2]/div/a[2]").click()
        driver.find_element_by_name("nf_opens_saturday").click()
        Select(driver.find_element_by_name("nf_opens_saturday")).select_by_visible_text("11am")
        driver.find_element_by_name("nf_opens_saturday").click()
        driver.find_element_by_name("nf_closes_saturday").click()
        Select(driver.find_element_by_name("nf_closes_saturday")).select_by_visible_text("4pm")
        driver.find_element_by_name("nf_closes_saturday").click()
        driver.find_element_by_name("nf_opens_sunday").click()
        Select(driver.find_element_by_name("nf_opens_sunday")).select_by_visible_text("11am")
        driver.find_element_by_name("nf_opens_sunday").click()
        driver.find_element_by_name("nf_closes_sunday").click()
        Select(driver.find_element_by_name("nf_closes_sunday")).select_by_visible_text("4pm")
        driver.find_element_by_name("nf_closes_sunday").click()
        driver.find_element_by_id("sbbutton").click()
        time.sleep(4)
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.refresh()
        time.sleep(4)
   
        
        # Checks out details of the business to see if the data is stored correctly
        # Checks basic details
        self.assertEqual(driver.find_element_by_name("nf_bizname").get_attribute('value'), "Long's Lucky PC Store 1994")
        self.assertEqual(driver.find_element_by_name("nf_bizstreet").get_attribute('value'), "199 main street")
        self.assertEqual(driver.find_element_by_name("nf_bizsuburb").get_attribute('value'), "mornington")
        self.assertEqual(driver.find_element_by_name("nf_level").get_attribute('value'), "10") # value is: grd, (1-10), other
        self.assertEqual(driver.find_element_by_name("nf_category").get_attribute('value'), "Electronics")
        self.assertEqual(driver.find_element_by_name("nf_shopCentre").get_attribute('value'), "1") #value is: 1 for Mornington Central, 2 for Frankston Bayside, empty(not in shopping center), 
        
        #checks opening hours
        self.assertEqual(driver.find_element_by_name("nf_opens_monday").get_attribute('value'), "0900") # time is 0000(12am) - 2300(11pm)
        self.assertEqual(driver.find_element_by_name("nf_opens_tuesday").get_attribute('value'), "0900")
        self.assertEqual(driver.find_element_by_name("nf_opens_wednesday").get_attribute('value'), "0900")
        self.assertEqual(driver.find_element_by_name("nf_opens_thursday").get_attribute('value'), "0900")
        self.assertEqual(driver.find_element_by_name("nf_opens_friday").get_attribute('value'), "0900")
        self.assertEqual(driver.find_element_by_name("nf_opens_saturday").get_attribute('value'), "1100")
        self.assertEqual(driver.find_element_by_name("nf_opens_sunday").get_attribute('value'), "1100")
        
        # checks closing hours
        self.assertEqual(driver.find_element_by_name("nf_closes_monday").get_attribute('value'), "1700")
        self.assertEqual(driver.find_element_by_name("nf_closes_tuesday").get_attribute('value'), "1700")
        self.assertEqual(driver.find_element_by_name("nf_closes_wednesday").get_attribute('value'), "1700")
        self.assertEqual(driver.find_element_by_name("nf_closes_thursday").get_attribute('value'), "1700")
        self.assertEqual(driver.find_element_by_name("nf_closes_friday").get_attribute('value'), "1700")
        self.assertEqual(driver.find_element_by_name("nf_closes_saturday").get_attribute('value'), "1600")
        self.assertEqual(driver.find_element_by_name("nf_closes_sunday").get_attribute('value'), "1600")
        
    def test_TC_BusinessFrom_01a(self):
        driver = self.driver
        driver.get(business_url)
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("user1")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("pass1")
        driver.find_element_by_id("password").send_keys(Keys.ENTER)
        time.sleep(4)
        
        # Checks out details of the business to see if the data is stored correctly
        # Checks basic details
        self.assertEqual(driver.find_element_by_name("nf_bizname").get_attribute('value'), "Long's Lucky PC Store 1994")
        self.assertEqual(driver.find_element_by_name("nf_bizstreet").get_attribute('value'), "199 main street")
        self.assertEqual(driver.find_element_by_name("nf_bizsuburb").get_attribute('value'), "mornington")
        self.assertEqual(driver.find_element_by_name("nf_level").get_attribute('value'), "10") # value is: grd, (1-10), other
        self.assertEqual(driver.find_element_by_name("nf_category").get_attribute('value'), "Electronics")
        self.assertEqual(driver.find_element_by_name("nf_shopCentre").get_attribute('value'), "1") #value is: 1 for Mornington Central, 2 for Frankston Bayside, empty(not in shopping center), 
        
        #checks opening hours
        self.assertEqual(driver.find_element_by_name("nf_opens_monday").get_attribute('value'), "0900") # time is 0000(12am) - 2300(11pm)
        self.assertEqual(driver.find_element_by_name("nf_opens_tuesday").get_attribute('value'), "0900")
        self.assertEqual(driver.find_element_by_name("nf_opens_wednesday").get_attribute('value'), "0900")
        self.assertEqual(driver.find_element_by_name("nf_opens_thursday").get_attribute('value'), "0900")
        self.assertEqual(driver.find_element_by_name("nf_opens_friday").get_attribute('value'), "0900")
        self.assertEqual(driver.find_element_by_name("nf_opens_saturday").get_attribute('value'), "1100")
        self.assertEqual(driver.find_element_by_name("nf_opens_sunday").get_attribute('value'), "1100")
        
        # checks closing hours
        self.assertEqual(driver.find_element_by_name("nf_closes_monday").get_attribute('value'), "1700")
        self.assertEqual(driver.find_element_by_name("nf_closes_tuesday").get_attribute('value'), "1700")
        self.assertEqual(driver.find_element_by_name("nf_closes_wednesday").get_attribute('value'), "1700")
        self.assertEqual(driver.find_element_by_name("nf_closes_thursday").get_attribute('value'), "1700")
        self.assertEqual(driver.find_element_by_name("nf_closes_friday").get_attribute('value'), "1700")
        self.assertEqual(driver.find_element_by_name("nf_closes_saturday").get_attribute('value'), "1600")
        self.assertEqual(driver.find_element_by_name("nf_closes_sunday").get_attribute('value'), "1600")
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=cwd))