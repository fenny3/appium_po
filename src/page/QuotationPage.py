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
    def __init__(self):
        super(QuotationPage, self).__init__()
        with open(os.path.join(BasePage.element, 'quotation_page.yaml'), 'r') as rf:
            self.element: dict = yaml.load(rf.read())

    def get_index_price(self, index_name):
        return float(self.find((By.XPATH, self.element['index_price']['xpath'] % index_name)).text)