import unittest
import time
import HtmlTestRunner
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


cwd = os.getcwd()+'/results' 

class Test_setUp_menu_buttons(unittest.TestCase):   
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    
    def tearDown(self):
        self.driver.close()
        
    #@unittest.skip("skip")
    def test_TC_Walking_01_iconClick(self):
        driver = self.driver
        driver.get("https://www.dfiinfo.com.au/beta-2-0-3d/")
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='firsttime']/div[2]/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='wrapper']/div[8]/div/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select").click()
        Select(driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select")).select_by_visible_text("Epilepsy")
        driver.find_element_by_xpath("//img[@alt='setup icon']").click()
        driver.find_element_by_xpath("//img[@alt='Walking']").click()
        driver.find_element_by_xpath("//img[@alt='Using a Cane']").click()
        driver.find_element_by_xpath("//img[@alt='Using a Walker']").click()
        driver.find_element_by_xpath("//img[@alt='Wheelchair']").click()
        
        time.sleep(2)
        
        self.assertTrue(driver.find_element_by_id("walk").is_selected())
        self.assertTrue(driver.find_element_by_id("walker").is_selected())
        self.assertTrue(driver.find_element_by_id("wchair").is_selected())
        self.assertTrue(driver.find_element_by_id("cane").is_selected())

        driver.save_screenshot('SC_TC_Walking_01_iconClick.png')
        
        
    #@unittest.skip("skip")    
    def test_TC_Walking_01_checkboxClick(self):
        driver = self.driver
        driver.get("https://www.dfiinfo.com.au/beta-2-0-3d/")
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='firsttime']/div[2]/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='wrapper']/div[8]/div/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select").click()
        Select(driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select")).select_by_visible_text("Epilepsy")
        driver.find_element_by_xpath("//img[@alt='setup icon']").click()
        driver.find_element_by_xpath("//div[@id='setup2']/ul/div[11]/li/label/span").click() 
        driver.find_element_by_xpath("//img[@alt='Using a Cane']").click()
        driver.find_element_by_xpath("//img[@alt='Using a Walker']").click()
        driver.find_element_by_xpath("//img[@alt='Wheelchair']").click()
        
        time.sleep(2)
        
        self.assertTrue(driver.find_element_by_id("walk").is_selected())
        self.assertTrue(driver.find_element_by_id("walker").is_selected())
        self.assertTrue(driver.find_element_by_id("wchair").is_selected())
        self.assertTrue(driver.find_element_by_id("cane").is_selected())     
       
        driver.save_screenshot('SC_TC_Walking_01_checkboxClick.png')
        
        
    #@unittest.skip("skip")
    def test_TC_Walking_01_textClick(self):
        driver = self.driver
        driver.get("https://www.dfiinfo.com.au/beta-2-0-3d/")
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='firsttime']/div[2]/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='wrapper']/div[8]/div/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select").click()
        Select(driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select")).select_by_visible_text("Epilepsy")
        driver.find_element_by_xpath("//img[@alt='setup icon']").click()
        driver.find_element_by_xpath("//div[@id='setup2']/ul/div[11]/li/label").click()
        driver.find_element_by_xpath("//img[@alt='Using a Cane']").click()
        driver.find_element_by_xpath("//img[@alt='Using a Walker']").click()
        driver.find_element_by_xpath("//img[@alt='Wheelchair']").click()
        
        time.sleep(2)
        
        self.assertTrue(driver.find_element_by_id("walk").is_selected())
        self.assertTrue(driver.find_element_by_id("walker").is_selected())
        self.assertTrue(driver.find_element_by_id("wchair").is_selected())
        self.assertTrue(driver.find_element_by_id("cane").is_selected())
        driver.save_screenshot('SC_TC_Walking_01_textClick.png')
        
        
    #@unittest.skip("skip")    
    def test_TC_Walking_01_boxAreaClick(self):
        driver = self.driver
        driver.get("https://www.dfiinfo.com.au/beta-2-0-3d/")
        driver.find_element_by_xpath("//div[@id='firsttime']/div[2]/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='wrapper']/div[8]/div/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select").click()
        Select(driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select")).select_by_visible_text("Epilepsy")
        driver.find_element_by_xpath("//img[@alt='setup icon']").click()
        driver.find_element_by_xpath("//div[@id='setup2']/ul/div[11]/li").click()
        driver.find_element_by_xpath("//img[@alt='Using a Cane']").click()
        driver.find_element_by_xpath("//img[@alt='Using a Walker']").click()
        driver.find_element_by_xpath("//img[@alt='Wheelchair']").click()
        
        time.sleep(2)
        
        self.assertTrue(driver.find_element_by_id("walk").is_selected())
        self.assertTrue(driver.find_element_by_id("walker").is_selected())
        self.assertTrue(driver.find_element_by_id("wchair").is_selected())
        self.assertTrue(driver.find_element_by_id("cane").is_selected())
        driver.save_screenshot('SC_TC_Walking_01_textClick.png')
        
        
    #@unittest.skip("skip")   
    def test_TC_Walking_05(self):
        driver = self.driver          
        driver.get("https://www.dfiinfo.com.au/beta-2-0-3d/")
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='firsttime']/div[2]/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='wrapper']/div[8]/div/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select").click()
        Select(driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select")).select_by_visible_text("Epilepsy")
        driver.find_element_by_xpath("//img[@alt='setup icon']").click()
        driver.find_element_by_xpath("//img[@alt='Walking']").click()
        driver.find_element_by_xpath("//img[@alt='Using a Cane']").click()
        driver.find_element_by_xpath("//img[@alt='Using a Walker']").click()
        driver.find_element_by_xpath("//img[@alt='Wheelchair']").click()
        driver.find_element_by_xpath("//div[@id='setupContainer']/div/button/div[2]").click()
        time.sleep(2)
        driver.find_element_by_id("inputname").click()
        driver.find_element_by_id("inputname").clear()
        driver.find_element_by_id("inputname").send_keys("TEST")
        driver.find_element_by_id("inputsub").click()
        driver.find_element_by_id("inputsub").clear()
        driver.find_element_by_id("inputsub").send_keys("Mornington")
        driver.find_element_by_id("inputsub").send_keys(Keys.ENTER)
        time.sleep(2)
        # assertEqual()
        driver.save_screenshot('SC_TC_Walking_05.png') 
        
              
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDFI_Search']
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=cwd))