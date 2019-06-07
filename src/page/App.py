# -*- coding:utf-8 -*-

"""
@Time    : 2019-05-28 14:41
@Author  : fenny.ren
@File    : App.py
"""
import os

from src.page.BasePage import BasePage
from src.page.MainPage import MainPage

routes = os.path.abspath(__file__).split('/')
ROOT = '/'.join(routes[:routes.index('appium_po') + 1])
config = os.path.join(ROOT, 'config')


class App(BasePage):
    @classmethod
    def main(cls):
        cls.get_client().restart_app()
        return MainPage()
