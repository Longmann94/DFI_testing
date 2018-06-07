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
url = input("Please enter website version to test when you are ready: ")
class Test_setUp_menu_buttons(unittest.TestCase):   
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    
    def tearDown(self): 
        self.driver.close()
        
    #@unittest.skip("skip")
    def test_TC_BigType_01_iconClick(self):
        driver = self.driver
        driver.get(url)
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='firsttime']/div[2]/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='wrapper']/div[8]/div/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select").click()
        Select(driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select")).select_by_visible_text("Autism")
        driver.find_element_by_xpath("//img[@alt='setup icon']").click()
        driver.find_element_by_xpath("//img[@alt='Seeing clearly']").click()
        driver.find_element_by_xpath("//img[@alt='I need Bigger Type']").click()
        time.sleep(2)
        
        self.assertTrue(driver.find_element_by_id("bigtype").is_selected())
        driver.save_screenshot('SC_TC_BigType_01_iconClick.png')
        
        
    #@unittest.skip("skip")    
    def test_TC_BigType_01_checkboxClick(self):
        driver = self.driver
        driver.get(url)
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='firsttime']/div[2]/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='wrapper']/div[8]/div/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select").click()
        Select(driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select")).select_by_visible_text("Autism")
        driver.find_element_by_xpath("//img[@alt='setup icon']").click()
        driver.find_element_by_xpath("//img[@alt='Seeing clearly']").click()
        driver.find_element_by_xpath("//div[@id='setup2']/ul/div[4]/li/label/span").click()      
        time.sleep(2)
        self.assertTrue(driver.find_element_by_id("bigtype").is_selected())
        driver.save_screenshot('SC_TC_BigType_01_checkboxClick.png')
        
        
    #@unittest.skip("skip")
    def test_TC_BigType_01_textClick(self):
        driver = self.driver
        driver.get(url)
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='firsttime']/div[2]/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='wrapper']/div[8]/div/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select").click()
        Select(driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select")).select_by_visible_text("Autism")
        driver.find_element_by_xpath("//img[@alt='setup icon']").click()
        driver.find_element_by_xpath("//img[@alt='Seeing clearly']").click()
        driver.find_element_by_xpath("//div[@id='setup2']/ul/div[4]/li/label").click()
        time.sleep(2)
        self.assertTrue(driver.find_element_by_id("bigtype").is_selected())
        driver.save_screenshot('SC_TC_BigType_01_textClick.png')
        
        
    #@unittest.skip("skip")    
    def test_TC_BigType_01_boxAreaClick(self):
        driver = self.driver
        driver.get(url)
        driver.find_element_by_xpath("//div[@id='firsttime']/div[2]/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='wrapper']/div[8]/div/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select").click()
        Select(driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select")).select_by_visible_text("Autism")
        driver.find_element_by_xpath("//img[@alt='setup icon']").click()
        driver.find_element_by_xpath("//img[@alt='Seeing clearly']").click()
        driver.find_element_by_xpath("//div[@id='setup2']/ul/div[4]/li").click()
        time.sleep(2)
        self.assertTrue(driver.find_element_by_id("bigtype").is_selected())
        driver.save_screenshot('SC_TC_BigType_01_boxAreaClick.png')
       
        
    #@unittest.skip("skip")
    def test_TC_BigType_02a(self):
        driver = self.driver
        driver.get(url)
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='firsttime']/div[2]/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='wrapper']/div[8]/div/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select").click()
        Select(driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select")).select_by_visible_text("Autism")
        driver.find_element_by_xpath("//img[@alt='setup icon']").click()
        driver.find_element_by_xpath("//img[@alt='Seeing clearly']").click()
        driver.find_element_by_xpath("//div[@id='setup2']/ul/div[4]/li/label").click()
        driver.find_element_by_xpath("//div[@id='setup2']/ul/div[4]/li").click()
        driver.find_element_by_xpath("//div[@id='setup2']/ul/div[4]/li/label").click()
        driver.find_element_by_xpath("//div[@id='setup2']/ul/div[4]/li/label/span").click()
        driver.find_element_by_xpath("//div[@id='setup2']/ul/div[4]/li/label").click()
        driver.find_element_by_xpath("//img[@alt='I need Bigger Type']").click()
        time.sleep(2)
        self.assertFalse(driver.find_element_by_id("bigtype").is_selected())
        driver.save_screenshot('SC_TC_BigType_02a_unselect.png')
      
        
        
        
        
    #@unittest.skip("skip")     
    def test_TC_BigType_02b(self):
        driver = self.driver
        driver.get(url)
        driver.find_element_by_xpath("//div[@id='firsttime']/div[2]/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='wrapper']/div[8]/div/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select").click()
        Select(driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select")).select_by_visible_text("Autism")
        driver.find_element_by_xpath("//img[@alt='setup icon']").click()
        driver.find_element_by_xpath("//img[@alt='Seeing clearly']").click()
        driver.find_element_by_xpath("//div[@id='setup2']/ul/div[4]/li/label").click()
        driver.find_element_by_xpath("//div[@id='setup2']/ul/div[4]/li").click()
        driver.find_element_by_xpath("//div[@id='setup2']/ul/div[4]/li/label/span").click()
        driver.find_element_by_xpath("//div[@id='setup2']/ul/div[4]/li/label").click()
        driver.find_element_by_xpath("//img[@alt='I need Bigger Type']").click()
        time.sleep(2)
        self.assertTrue(driver.find_element_by_id("bigtype").is_selected())
        driver.save_screenshot('SC_TC_BigType_02b_select.png')  
        
        
    #@unittest.skip("skip")    
    def test_TC_BigType_03(self):
        driver = self.driver
        driver.get(url)
        driver.find_element_by_xpath("//div[@id='firsttime']/div[2]/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='wrapper']/div[8]/div/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select").click()
        Select(driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select")).select_by_visible_text("Autism")
        driver.find_element_by_xpath("//img[@alt='setup icon']").click()
        driver.find_element_by_xpath("//img[@alt='Seeing clearly']").click()
        button = driver.find_element_by_xpath("//img[@alt='I need Bigger Type']")
        ActionChains(driver).move_to_element(button).click_and_hold(button).pause(6).release().perform()  
        time.sleep(2)
        self.assertTrue(driver.find_element_by_id("bigtype").is_selected())
        # assertEqual()
        driver.save_screenshot('SC_TC_BigType_03.png')
        
    #@unittest.skip("skip still working on it, drag mouse over button")    
    def test_TC_BigType_04(self):
        driver = self.driver
        driver.get(url)
        driver.find_element_by_xpath("//div[@id='firsttime']/div[2]/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='wrapper']/div[8]/div/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select").click()
        Select(driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select")).select_by_visible_text("Autism")
        driver.find_element_by_xpath("//img[@alt='setup icon']").click()
        driver.find_element_by_xpath("//img[@alt='Seeing clearly']").click()
        driver.find_element_by_xpath("//img[@alt='I need Bigger Type']")
        button = driver.find_element_by_xpath("//div[@id='setup2']/ul/div[4]/li/label")
        ActionChains(driver).drag_and_drop_by_offset(button, 30, 10).perform()
        time.sleep(2)
        self.assertTrue(driver.find_element_by_id("bigtype").is_selected())
        # assertEqual()
        driver.save_screenshot('SC_TC_BigType_04.png')
        
        
    #@unittest.skip("skip")   
    def test_TC_BigType_05(self):
        driver = self.driver          
        driver.get(url)
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='firsttime']/div[2]/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='wrapper']/div[8]/div/button/div[2]").click()
        driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select").click()
        Select(driver.find_element_by_xpath("//div[@id='setupContainer']/div[2]/select")).select_by_visible_text("Autism")
        driver.find_element_by_xpath("//img[@alt='setup icon']").click()
        driver.find_element_by_xpath("//img[@alt='Seeing clearly']").click()
        driver.find_element_by_xpath("//img[@alt='I need Bigger Type']").click()
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
        driver.save_screenshot('SC_TC_BigType_05.png') 
        
              
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDFI_Search']
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=cwd))
    