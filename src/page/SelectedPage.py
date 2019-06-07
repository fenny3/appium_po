# -*- coding:utf-8 -*-

"""
@Time    : 2019-05-28 15:06
@Author  : fenny.ren
@File    : SelectedPage.py
"""
import os

import yaml
from selenium.webdriver.common.by import By

from src.page.BasePage import BasePage


class SelectedPage(BasePage):
    def goto_hs(self):
        self.find_by_text('沪深').click()
        return self

    # def add_default(self):
    #     default_add = self.whether_element_displayed_by_text(self.element['default_add']['text'], wait=1)
    #     if default_add:
    #         default_add.click()
    #     return self

    def get_price_by_name(self, name):
        # price = self.find((By.XPATH, self.element['stock_price']['xpath'] % name)).text
        price = self.load_steps('/Users/feeny/Touchpal/appium_po/src/data/SelectedPage.yaml', 'get_price_by_name', stock_name=name)
        print(price)
        return float(price)
