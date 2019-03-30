###########################################################
#author:sunny, date:3/29/2019
#function:check pricing dropdown menu
###########################################################
#test_pricing.py
#coding = utf-8

from eleexist import *
from startend import *
import  time
import unittest
import os

class Pricing(EleExist):
    #@unittest.skip("later")                    #skip decaretor
    def test_pricingMenu(self):                  ##pricing dropmenu
        time.sleep(2)
        textresult = "False"

        if (self.isElementExist("nav>ul>li:nth-child(5)")):
            if (self.isTextExist("nav>ul>li:nth-child(5)", "Pricing")):
                print("good Pricing")
                self.driver.find_element_by_css_selector("nav>ul>li:nth-child(5)").click()  #open the dropdown menu
                time.sleep(2)
                if(self.isTextExist("nav>ul>li:nth-child(5)>details>div>a","Plans")):       #plan dropdown
                    print("plans good")
                else:
                    print("wrong plans")

                if(self.isTextExist("a[href='/pricing#feature-comparison']","Compare plans")):
                    print("compare plans good")
                else:
                    print("wrong compare plans")

                if(self.isTextExist("a[href$='/contact']","Contact Sales")):    #end by $
                    print("contact good")
                else:
                    print("wrong contact")

                if(self.isTextExist("a[href='/nonprofit']","Nonprofit")):
                    print("noprofit good")
                else:
                    print("wrong profit")

                if(self.isTextExist("a[href$='.com']","Education")):
                    print("education good")
                else:
                    print("wrong education")
            else:
                print("wrong Pricing")
        else:
            print("no pricing")
        self.driver.refresh()                                                      #refresh page

    def test_plan(self):                                                           #plan window
        time.sleep(2)
        self.driver.find_element_by_css_selector("nav>ul>li:nth-child(5)").click()  #open the dropdown menu
        self.driver.find_element_by_css_selector("a[href='/pricing']").click() #open plan window
        time.sleep(2)
        title = self.driver.title
        self.assertEqual(title, "Pricing · Plans for every developer · GitHub")    #window title
        self.driver.back()                                                         #back to last page

    def test_compareplan(self):                                                    #compare plan window
        time.sleep(2)
        self.driver.find_element_by_css_selector("nav>ul>li:nth-child(5)").click()  #open the dropdown menu
        self.driver.find_element_by_css_selector("a[href='/pricing#feature-comparison']").click() #open plan window
        time.sleep(2)
        title = self.driver.title
        self.assertEqual(title, "Pricing · Plans for every developer · GitHub")    #window title
        self.driver.back()                                                         #back to last page

    def test_contact(self):                                                         #contact window
        time.sleep(2)
        self.driver.find_element_by_css_selector("nav>ul>li:nth-child(5)").click()  #open the dropdown menu
        self.driver.find_element_by_css_selector("a[href$='/contact']").click()
        time.sleep(2)
        title = self.driver.title
        self.assertEqual(title, "Contact us - GitHub Enterprise")
        self.driver.back()

    def test_profit(self):                                                         #profit window
        time.sleep(2)
        self.driver.find_element_by_css_selector("nav>ul>li:nth-child(5)").click()  #open the dropdown menu
        self.driver.find_element_by_css_selector("a[href='/nonprofit']").click()
        time.sleep(2)
        title = self.driver.title
        self.assertEqual(title, "GitHub for Nonprofits · GitHub")
        self.driver.back()

    def test_education(self):                                                         #profit window
        time.sleep(2)
        self.driver.find_element_by_css_selector("nav>ul>li:nth-child(5)").click()  #open the dropdown menu
        self.driver.find_element_by_css_selector("a[href='\education']").click()
        time.sleep(2)
        title = self.driver.title
        self.assertEqual(title, "Engaged students are the result of using real-world tools - GitHub Education")
        self.driver.back()
