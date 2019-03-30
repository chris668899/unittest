###########################################################
#author:sunny, date:3/24/2019
#function:access the test case sequence, and setUp,tearDown
#are accessed by every test named by test at the beginning
#element exist, and show the right content
###########################################################
#eleexist.py
#coding = utf-8

from selenium import webdriver
import unittest
from selenium.webdriver.support import expected_conditions as EC

class EleExist(unittest.TestCase):

    @classmethod                                     #decorator of unittest
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://github.com/sunnie2004")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def isElementExist(cls,element):
        flag = True
        try:
            cls.driver.find_element_by_css_selector(element)
            return flag

        except:
            flag = False
            return flag

    def isTextExist(cls,element,textexpect):
        textresult = "no"

#            flag1 = EC.text_to_be_present_in_element(locator,text)(driver)
        textresult = cls.driver.find_element_by_css_selector(element).text
        if(textresult == textexpect):
            return True
        else:
            return False