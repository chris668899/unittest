###########################################################
#author:sunny, date:3/24/2019
#function:access the test case sequence, and setUp,tearDown
#are accessed by every test named by test at the beginning
###########################################################
#startend.py
#coding = utf-8

from selenium import webdriver
import  time
import unittest

class StartEnd(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://github.com/sunnie2004")


    def tearDown(self):
        self.driver.quit()