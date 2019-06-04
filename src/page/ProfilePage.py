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


class ProfilePage(BasePage):
    def __init__(self):
        super(ProfilePage, self).__init__()
        with open(os.path.join(BasePage.element, 'profile_page.yaml'), 'r') as rf:
            self.element: dict = yaml.load(rf.read())

    def goto_login(self):
        from src.page.LoginPage import LoginPage
        self.find_by_text(self.element['login']['text']).click()
        return LoginPage()

