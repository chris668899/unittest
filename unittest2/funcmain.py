###########################################################
#author:sunny, date:3/21/2019
#function:test the parameter in main() and effective range
#of the parameters
###########################################################
#funcmain.py

#coding = utf-8
from selenium import webdriver
import  time
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://github.com/sunnie2004")

    def test_repositories(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//nav/a[2]").click()
        time.sleep(2)
        title = self.driver.title
        self.assertEqual(title,"sunnie2004 / Repositories · GitHub")

    def test_projects(self):    #use same parameter to test the range of the parameter#
        time.sleep(2)
        self.driver.find_element_by_xpath("//nav/a[3]").click()
        time.sleep(2)
        title = self.driver.title
        self.assertEqual(title,"sunnie2004 () / Projects · GitHub")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2,exit=False)