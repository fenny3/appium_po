# -*- coding:utf-8 -*-

"""
@Time    : 2019-05-28 16:46
@Author  : fenny.ren
@File    : ProfilePage.py
"""
import os

import yaml
from selenium.webdriver.common.by import By

from src.page.BasePage import BasePage
from src.page.LoginPage import LoginPage


class ProfilePage(BasePage):

    def goto_login(self):
        # self.find_by_text(self.element['login']['text']).click()
        self.load_steps('/Users/feeny/Touchpal/appium_po/src/data/ProfilePage.yaml', 'goto_login')
        return LoginPage()

