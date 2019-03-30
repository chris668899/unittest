###########################################################
#author:sunny, date:3/30/2019
#function:check explore header link
###########################################################
#test_enterprise.py
#coding = utf-8

from selenium import webdriver
import  time
import unittest
import os
from eleexist import *
from startend import *

class Enterprise(EleExist):

    def test_enterprise(self):                  ##enterprise link
        time.sleep(2)
        if(self.isElementExist("nav>ul>li:nth-child(2)")):
            self.driver.find_element_by_css_selector("nav>ul>li:nth-child(2)").click()  # open the link
            time.sleep(2)
            title = self.driver.title
            self.assertEqual(title, "Enterprise · A smarter way to work together · GitHub")    #check window title
            self.driver.back()
        else:
            print("can not find enterprise header!")