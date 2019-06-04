# -*- coding:utf-8 -*-

"""
@Time    : 2019-05-28 14:17
@Author  : fenny.ren
@File    : AndroidClient.py
"""
import yaml
from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class AndroidClient:

    driver: WebDriver
    
    @classmethod
    def read_yaml(cls, yaml_path):
        with open(yaml_path, 'r') as rf:
            text = rf.read()
            print(text)
            return yaml.load(text)

    @classmethod
    def install_app(cls, yaml_path):
        config = cls.read_yaml(yaml_path)
        cls.driver = webdriver.Remote(config['RemoteUrl'], config['InstallCaps'])
        cls.driver.implicitly_wait(config['IMPLICITLY_WAIT_TIME'])
        # cls.window_size = cls.driver.get_window_size()
        # cls.width = cls.window_size['width']
        # cls.height = cls.window_size['height']
        return cls.driver

    @classmethod
    def restart_app(cls, yaml_path):
        config = cls.read_yaml(yaml_path)
        cls.driver = webdriver.Remote(config['RemoteUrl'], config['RestartCaps'])
        cls.driver.implicitly_wait(config['IMPLICITLY_WAIT_TIME'])
        return cls.driver
