# -*- coding:utf-8 -*-

"""
@Time    : 2019-06-04 17:38
@Author  : fenny.ren
@File    : QuotationPage.py
"""
import os

import yaml
from selenium.webdriver.common.by import By

from src.page.BasePage import BasePage


class QuotationPage(BasePage):

    def get_index_price(self, index_name):
        return float(self.load_steps('/Users/feeny/Touchpal/appium_po/src/data/QuotationPage.yaml', 'get_index_price', index_name=index_name))
        # return float(self.find((By.XPATH, self.element['index_price']['xpath'] % index_name)).text)