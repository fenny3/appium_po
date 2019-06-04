# -*- coding:utf-8 -*-

"""
@Time    : 2019-05-28 15:06
@Author  : fenny.ren
@File    : SearchPage.py
"""
import os

import yaml
from selenium.webdriver.common.by import By

from src.page.BasePage import BasePage


class SearchPage(BasePage):
    def __init__(self):
        super(SearchPage, self).__init__()
        with open(os.path.join(BasePage.element, 'search_page.yaml'), 'r') as rf:
            self.element: dict = yaml.load(rf.read())

    def search(self, key):
        self.find((By.CLASS_NAME, self.element['input']['class'])).send_keys(key)
        return self

    def click_selected(self, key):
        self.find((By.XPATH, self.element['select_button']['xpath'].format(key))).click()
        return self

    def is_selected(self, key):
        resource_id = self.find((By.XPATH, self.element['select_button']['xpath'].format(key))).get_attribute('resourceId')
        print(resource_id)
        return "followed_btn" in resource_id

    def cancel(self):
        self.find_by_text("取消").click()

    def search_by_user(self, key):
        pass

    def is_followed(self):
        pass