########################################################################################
#author:sunny, date:3/30/2019
#function: test report output by html page,open the report.html by browser to get result
########################################################################################
#reporthtml.py
#coding = utf-8
from test_pricing import *
from test_header import *
from test_enterprise import *
import os
import unittest
import HTMLTestRunner

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Header("test_why"))
    suite.addTest(Pricing("test_pricingMenu"))
    suite.addTest(Pricing("test_plan"))
    suite.addTest(Pricing("test_compareplan"))
    suite.addTest(Pricing("test_profit"))
    suite.addTest(Pricing("test_education"))

    Report = "C:\\Users\\a\\PycharmProjects\\unittest2\\HTMLReport.html"

    f = open(Report, "wb")     #w--/n to /r/n; wb-byte way write file
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="github test:", description="header part test:")

    runner.run(suite)

    f.close()