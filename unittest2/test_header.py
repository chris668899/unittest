###########################################################
# author:sunny, date:3/22/2019
# function:github header content is right or not
###########################################################
# test_header.py
# coding = utf-8

from eleexist import *
from startend import *
import time
import unittest
import os


class Header(EleExist):

    def test_why(self):  ##header
        time.sleep(2)
        textresult = "False"
        if (self.isElementExist("nav>ul>li:nth-child(1)")):

            if (self.isTextExist("nav>ul>li:nth-child(1)", "Why GitHub?")):
                print("good whygithub & Header")
            else:
                print("wrong whygithub")

    def test_enterprise(self):  ##header
        if (self.isElementExist("nav>ul>li:nth-child(2)")):

            if (self.isTextExist("nav>ul>li:nth-child(2)", "Enterprise")):
                print("good Enterprise & Header")
            else:
                print("wrong Enterprise")

    def test_explore(self):  ##header
        if (self.isElementExist("nav>ul>li:nth-child(3)")):

            if (self.isTextExist("nav>ul>li:nth-child(3)", "Explore")):
                print("good Explore & Header")
            else:
                print("wrong Explore")

    def test_marketplace(self):  ##header
        if (self.isElementExist("nav>ul>li:nth-child(4)")):

            if (self.isTextExist("nav>ul>li:nth-child(4)", "Marketplace")):
                print("good Marketplace & Header")
            else:
                print("wrong Marketplace")

    def test_pricing(self):  ##header
        if (self.isElementExist("nav>ul>li:nth-child(5)")):

            if (self.isTextExist("nav>ul>li:nth-child(5)", "Pricing")):
                print("good Pricing & Header")
            else:
                print("wrong Pricing")
