###########################################################
#author:sunny, date:3/28/2019
#function:discover method to load test cases
#discover(start_dir, pattern, top_level_dir)
###########################################################
#discover.py
#coding = utf-8

import unittest
import os

case_path = './'

discovery = unittest.defaultTestLoader.discover(case_path,pattern="test_*.py",top_level_dir=None)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()                #run method
    runner.run(discovery)