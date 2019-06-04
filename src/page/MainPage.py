# -*- coding:utf-8 -*-

"""
@Time    : 2019-05-28 14:15
@Author  : fenny.ren
@File    : MainPage.py
"""
import os

import yaml
from selenium.webdriver.common.by import By

from src.page.BasePage import BasePage
from src.page.SearchPage import SearchPage
from src.page.SelectedPage import SelectedPage


class MainPage(BasePage):

    def __init__(self):
        super(MainPage, self).__init__()
        with open(os.path.join(BasePage.element, 'main_page.yaml'), 'r') as rf:
            self.element: dict = yaml.load(rf.read())

    def goto_selected(self):
        self.find_by_text(self.element['selected']['text']).click()
        return SelectedPage()

    def goto_profile(self):
        from src.page.ProfilePage import ProfilePage
        self.find((By.ID, self.element['profile']['id'])).click()
        return ProfilePage()
    
    def goto_search(self):
        self.find((By.ID, self.element['search']['id'])).click()
        return SearchPage()