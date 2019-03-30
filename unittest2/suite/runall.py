#################################################################################
#author:sunny, date:3/30/2019
#function: use testloader to create suite by 2 ways:loadTestsFromTestCase(classname),
#loadTestsFromName(" module name.class name.method name")
###################################################################################
#run_all.py
#coding = utf-8
from test_pricing import *
from test_header import *
from test_enterprise import *
import unittest

if __name__ == "__main__":
    suite = unittest.TestSuite()
    #######################################
    #classname way to load test
    ######################################
    # suite.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Pricing),
    #                 unittest.defaultTestLoader.loadTestsFromTestCase(Header),
    #                 unittest.defaultTestLoader.loadTestsFromTestCase?(Enterprise)])
    #
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    #######################################
    # module.class.method way to load test
    ######################################
    suite.addTests([unittest.defaultTestLoader.loadTestsFromName("test_pricing.Pricing.test_compareplan"),
                    unittest.defaultTestLoader.loadTestsFromName("test_pricing.Pricing.test_contact"),
                    unittest.defaultTestLoader.loadTestsFromName("test_pricing.Pricing.test_pricingMenu"),
                    unittest.defaultTestLoader.loadTestsFromName("test_pricing.Pricing.test_profit"),
                    unittest.defaultTestLoader.loadTestsFromName("test_pricing.Pricing.test_plan"),
                    unittest.defaultTestLoader.loadTestsFromName("test_pricing.Pricing.test_education"),

                    unittest.defaultTestLoader.loadTestsFromName("test_header.Header.test_why"),
                    unittest.defaultTestLoader.loadTestsFromName("test_header.Header.test_enterprise"),
                    unittest.defaultTestLoader.loadTestsFromName("test_header.Header.test_pricing"),
                    unittest.defaultTestLoader.loadTestsFromName("test_header.Header.test_marketplace"),
                    unittest.defaultTestLoader.loadTestsFromName("test_header.Header.test_explore"),

                    unittest.defaultTestLoader.loadTestsFromName("test_enterprise.Enterprise.test_enterprise")
                    ])
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)