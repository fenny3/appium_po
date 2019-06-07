# -*- coding:utf-8 -*-

"""
@Time    : 2019-05-28 14:17
@Author  : fenny.ren
@File    : Client.py
"""
import yaml
from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class Client:

    driver: WebDriver
    platform: str = 'android'
    
    @classmethod
    def read_yaml(cls, yaml_path):
        with open(yaml_path, 'r') as rf:
            text = rf.read()
            return yaml.load(text)

    @classmethod
    def install_app(cls):
        return cls.init_driver('install_app')

    @classmethod
    def restart_app(cls):
        return cls.init_driver('restart_app')

    @classmethod
    def init_driver(cls, key):
        config = cls.read_yaml('/Users/feeny/Touchpal/appium_po/src/data/driver.yaml')
        cls.platform = config['platform']
        cls.driver = webdriver.Remote(config['server'], config[key]['caps'][cls.platform])
        cls.driver.implicitly_wait(config['implicitly_wait'])
        cls.driver.activate_ime_engine('io.appium.settings/.UnicodeIME')
        return cls.driver
