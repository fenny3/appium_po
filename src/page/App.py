# -*- coding:utf-8 -*-

"""
@Time    : 2019-05-28 14:41
@Author  : fenny.ren
@File    : App.py
"""
import os

from appium.webdriver.webdriver import WebDriver
from src.driver.AndroidClient import AndroidClient
from src.page.MainPage import MainPage

routes = os.path.abspath(__file__).split('/')
ROOT = '/'.join(routes[:routes.index('appium_po') + 1])
config = os.path.join(ROOT, 'config')


class App(object):
    driver: WebDriver = WebDriver

    @classmethod
    def main(cls, key='Android'):
        if key == 'Android':
            client = AndroidClient
        else:
            raise Exception('暂时没有定义其他driver，仅支持Android')
        client.restart_app(os.path.join(config, 'config.yaml'))
        return MainPage()

    @classmethod
    def get_driver(cls, key='Android'):
        if key == 'Android':
            cls.driver = AndroidClient.driver
        else:
            raise Exception('暂时没有定义其他driver，仅支持Android')
        return cls.driver
