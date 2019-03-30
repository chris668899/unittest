###########################################################
#author:sunny, date:3/29/2019
#function:use suite to add testcases
###########################################################
#suite.py
#coding = utf-8
from test_pricing import *
from test_header import *
from test_enterprise import *
import unittest

if __name__ == "__main__":
    suite = unittest.TestSuite()

    suite.addTest(Header("test_why"))
    suite.addTest(Header("test_pricing"))
    suite.addTest(Header("test_enterprise"))
    suite.addTest(Header("test_explore"))
    suite.addTest(Header("test_marketplace"))

    suite.addTest(Pricing("test_pricingMenu"))
    suite.addTest(Pricing("test_plan"))
    suite.addTest(Pricing("test_compareplan"))
    suite.addTest(Pricing("test_contact"))
    suite.addTest(Pricing("test_profit"))
    suite.addTest(Pricing("test_education"))

    suite.addTest(Enterprise("test_enterprise"))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)