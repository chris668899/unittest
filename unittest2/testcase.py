###########################################################
#author:sunny, date:3/21/2019
#function:access the test case sequence, and setUp,tearDown
#are accessed by every test case named by test as the header
#sequence follows the number or alphabetA-Z,a-z
###########################################################
#testcase.py

#coding = utf-8
from selenium import webdriver
import  time
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://github.com/sunnie2004")

    def test_title(self):                   ##test the title
        time.sleep(2)
        title1 = self.driver.title
        self.assertEqual(title1,"sunnie2004 · GitHub")

    def test_signin(self):                  ##sign in window
        time.sleep(2)
        self.driver.find_element_by_link_text("Sign in").click()
        time.sleep(2)
        title2 = self.driver.title
        self.assertEqual(title2,"Sign in to GitHub · GitHub")

    def test_signup(self):                  ##sign up window
        time.sleep(2)
        self.driver.find_element_by_link_text("Sign up").click()
        time.sleep(2)
        title3 = self.driver.title
        self.assertEqual(title3,"Join GitHub · GitHub")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()