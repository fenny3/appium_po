# -*- coding:utf-8 -*-

"""
@Time    : 2019-05-28 15:06
@Author  : fenny.ren
@File    : SearchPage.py
"""
import os
import logging

import yaml
from selenium.webdriver.common.by import By

from src.page.BasePage import BasePage


class SearchPage(BasePage):

    def search(self, key):
        self.load_steps('/Users/feeny/Touchpal/appium_po/src/data/SearchPage.yaml', 'search', search_text=key)
        # self.find((By.CLASS_NAME, self.element['input']['class'])).send_keys(key)
        return self

    def click_selected(self, key):
        # self.find((By.XPATH, self.element['select_button']['xpath'].format(key))).click()
        self.load_steps('/Users/feeny/Touchpal/appium_po/src/data/SearchPage.yaml', 'click_selected', stock_code=key)
        return self

    def is_selected(self, key):
        # resource_id = self.find((By.XPATH, self.element['select_button']['xpath'].format(key))).get_attribute('resourceId')
        resource_id = self.load_steps('/Users/feeny/Touchpal/appium_po/src/data/SearchPage.yaml', 'is_selected', stock_code=key)
        logging.info(resource_id)
        return "followed_btn" in resource_id

    def cancel(self):
        self.find_by_text("取消").click()

    def is_followed(self, key):
        # resource_id = self.find((By.XPATH, self.element['follow_button']['xpath'].format(key))).get_attribute('resourceId')
        resource_id = self.load_steps('/Users/feeny/Touchpal/appium_po/src/data/SearchPage.yaml', 'is_followed', follow_button=key)
        print(resource_id)
        return "followed_btn" in resource_id