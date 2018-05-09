'''
Created on 2 May 2018

@author: layfon
'''
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

def random_char(size=6, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

cwd = os.getcwd()+'/results' 

class Test_business_search(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()


    def test_TC_Search_01(self):
        driver = self.driver
        driver.get("https://www.dfiinfo.com.au/beta-2-0-3b/#bz_0")
        driver.find_element_by_xpath("//div[@id='firsttime']/div[2]/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='wrapper']/div[8]/div[2]/button/div[2]").click()
        driver.find_element_by_id("inputname").click()
        driver.find_element_by_id("inputname").clear()
        driver.find_element_by_id("inputname").send_keys("SilverLake Flowers")
        driver.find_element_by_id("inputsub").click()
        driver.find_element_by_id("inputsub").clear()
        driver.find_element_by_id("inputsub").send_keys("Mornington")
        driver.find_element_by_id("inputsub").send_keys(Keys.ENTER)
        time.sleep(2)
        # self.assertEqual("Frank Classique Bakery", driver.find_element_by_xpath("//div[@id='results']/ul/a[3]/li"))
        driver.save_screenshot('SC_TC_Search_01.png')
        
        
    def test_TC_Search_01a(self):
        driver = self.driver
        driver.get("https://www.dfiinfo.com.au/beta-2-0-3b/#bz_0")
        driver.find_element_by_xpath("//div[@id='firsttime']/div[2]/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='wrapper']/div[8]/div[2]/button/div[2]").click()
        driver.find_element_by_id("inputname").click()
        driver.find_element_by_id("inputname").clear()
        driver.find_element_by_id("inputname").send_keys("Mag")
        driver.find_element_by_id("inputsub").click()
        driver.find_element_by_id("inputsub").clear()
        driver.find_element_by_id("inputsub").send_keys("Morn")
        driver.find_element_by_id("inputsub").send_keys(Keys.ENTER)
        time.sleep(2)
        # self.assertEqual("Frank Classique Bakery", driver.find_element_by_xpath("//div[@id='results']/ul/a[3]/li"))
        driver.save_screenshot('SC_TC_Search_01a.png')
            
        
        
    def test_TC_Search_01b(self):
        driver = self.driver
        driver.get("https://www.dfiinfo.com.au/beta-2-0-3b/#bz_0")
        driver.find_element_by_xpath("//div[@id='firsttime']/div[2]/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='wrapper']/div[8]/div[2]/button/div[2]").click()
        driver.find_element_by_id("inputname").click()
        driver.find_element_by_id("inputname").clear()
        driver.find_element_by_id("inputname").send_keys("Shine Bright")
        driver.find_element_by_id("inputsub").click()
        driver.find_element_by_id("inputsub").clear()
        driver.find_element_by_id("inputsub").send_keys("Morni")
        driver.find_element_by_id("inputsub").send_keys(Keys.ENTER)
        time.sleep(2)
        # self.assertEqual("Frank Classique Bakery", driver.find_element_by_xpath("//div[@id='results']/ul/a[3]/li"))
        driver.save_screenshot('SC_TC_Search_01b.png')
        
        
    def test_TC_Search_01c(self):
        driver = self.driver
        driver.get("https://www.dfiinfo.com.au/beta-2-0-3b/#bz_0")
        driver.find_element_by_xpath("//div[@id='firsttime']/div[2]/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='wrapper']/div[8]/div[2]/button/div[2]").click()
        driver.find_element_by_id("inputname").click()
        driver.find_element_by_id("inputname").clear()
        driver.find_element_by_id("inputname").send_keys("D")
        driver.find_element_by_id("inputsub").click()
        driver.find_element_by_id("inputsub").clear()
        driver.find_element_by_id("inputsub").send_keys("Mornington")
        driver.find_element_by_id("inputsub").send_keys(Keys.ENTER)
        time.sleep(2)
        # self.assertEqual("Frank Classique Bakery", driver.find_element_by_xpath("//div[@id='results']/ul/a[3]/li"))
        driver.save_screenshot('SC_TC_Search_01c.png')
        
        
    def test_TC_Search_01d(self):
        driver = self.driver
        driver.get("https://www.dfiinfo.com.au/beta-2-0-3b/#bz_0")
        driver.find_element_by_xpath("//div[@id='firsttime']/div[2]/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='wrapper']/div[8]/div[2]/button/div[2]").click()
        driver.find_element_by_id("inputname").click()
        driver.find_element_by_id("inputname").clear()
        driver.find_element_by_id("inputname").send_keys("88 Fried Chicken")
        driver.find_element_by_id("inputsub").click()
        driver.find_element_by_id("inputsub").clear()
        driver.find_element_by_id("inputsub").send_keys("mornington")
        driver.find_element_by_id("inputsub").send_keys(Keys.ENTER)
        time.sleep(2)
        # self.assertEqual("Frank Classique Bakery", driver.find_element_by_xpath("//div[@id='results']/ul/a[3]/li"))
        driver.save_screenshot('SC_TC_Search_01d.png')
        
        
    def test_TC_Search_01e(self):
        driver = self.driver
        driver.get("https://www.dfiinfo.com.au/beta-2-0-3b/#bz_0")
        driver.find_element_by_xpath("//div[@id='firsttime']/div[2]/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='wrapper']/div[8]/div[2]/button/div[2]").click()
        driver.find_element_by_id("inputname").click()
        driver.find_element_by_id("inputname").clear()
        driver.find_element_by_id("inputname").send_keys("hElLo HoMe")
        driver.find_element_by_id("inputsub").click()
        driver.find_element_by_id("inputsub").clear()
        driver.find_element_by_id("inputsub").send_keys("MorNInGtoN")
        driver.find_element_by_id("inputsub").send_keys(Keys.ENTER)
        time.sleep(2)
        # self.assertEqual("Frank Classique Bakery", driver.find_element_by_xpath("//div[@id='results']/ul/a[3]/li"))
        driver.save_screenshot('SC_TC_Search_01e.png')
        
        
    def test_TC_Search_01f(self):
        driver = self.driver
        driver.get("https://www.dfiinfo.com.au/beta-2-0-3b/#bz_0")
        driver.find_element_by_xpath("//div[@id='firsttime']/div[2]/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='wrapper']/div[8]/div[2]/button/div[2]").click()
        driver.find_element_by_id("inputname").click()
        driver.find_element_by_id("inputname").clear()
        driver.find_element_by_id("inputname").send_keys(random_char(10))
        driver.find_element_by_id("inputsub").click()
        driver.find_element_by_id("inputsub").clear()
        driver.find_element_by_id("inputsub").send_keys(random_char(10))
        driver.find_element_by_id("inputsub").send_keys(Keys.ENTER)
        time.sleep(2)
        # self.assertEqual("Frank Classique Bakery", driver.find_element_by_xpath("//div[@id='results']/ul/a[3]/li"))
        driver.save_screenshot('SC_TC_Search_01f.png')
        
    # @unittest.skip("skip")    
    def test_TC_Search_01g(self):
        driver = self.driver
        driver.get("https://www.dfiinfo.com.au/beta-2-0-3b/#bz_0")
        driver.find_element_by_xpath("//div[@id='firsttime']/div[2]/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='wrapper']/div[8]/div[2]/button/div[2]").click()
        driver.find_element_by_id("inputname").click()
        driver.find_element_by_id("inputname").clear()
        driver.find_element_by_id("inputname").send_keys(random_char(100))
        driver.find_element_by_id("inputsub").click()
        driver.find_element_by_id("inputsub").clear()
        driver.find_element_by_id("inputsub").send_keys(random_char(100))
        driver.find_element_by_id("inputsub").send_keys(Keys.ENTER)
        time.sleep(2)
        # self.assertEqual("Frank Classique Bakery", driver.find_element_by_xpath("//div[@id='results']/ul/a[3]/li"))
        driver.save_screenshot('SC_TC_Search_01g.png')



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/results'))