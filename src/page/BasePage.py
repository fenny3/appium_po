# -*- coding:utf-8 -*-

"""
@Time    : 2019-05-28 14:53
@Author  : fenny.ren
@File    : BasePage.py
"""
import os
import time

from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


routes = os.path.abspath(__file__).split('/')
ROOT = '/'.join(routes[:routes.index('appium_po') + 1])


class BasePage:

    element = os.path.join(ROOT, 'src', 'element')

    def __init__(self):
        from src.page.App import App
        self.driver = App.get_driver(key='Android')

    def find(self, kv: tuple) -> WebElement:
        return self.driver.find_element(*kv)

    def find_by_text(self, text: str) -> WebElement:
        return self.find((By.XPATH, "//*[contains(@text, '%s')]" % text))

    def wait_element_displayed(self, kv, wait: int=10, message: str='') -> WebElement or bool:
        max_time = time.time() + wait
        while time.time() < max_time:
            try:
                return self.find(kv)
            except WebDriverException:
                pass
            time.sleep(0.2)
        raise NoSuchElementException(message)

    def whether_element_displayed(self, kv, wait: int=10, message: str='') -> WebElement or bool:
        max_time = time.time() + wait
        try:
            while time.time() < max_time:
                try:
                    return self.find(kv)
                except WebDriverException:
                    pass
                time.sleep(0.2)
            raise NoSuchElementException(message)
        except:
            return False

    def whether_element_displayed_by_text(self, text, wait: int=10, message: str='') -> WebElement or bool:
        max_time = time.time() + wait
        try:
            while time.time() < max_time:
                try:
                    return self.find_by_text(text)
                except WebDriverException:
                    pass
                time.sleep(0.2)
            raise NoSuchElementException(message)
        except:
            return False

    # def wait_element_present1(self, kv, wait: int=10, fre: float=0.5) -> WebElement:
    #     element = WebDriverWait(self.driver, wait, poll_frequency=fre, ).until(lambda x: getattr(x, function_name)(value))
    #     print(element)
    #     return element
    #
    # def wait_element_present2(self, by: str, value: str, wait: int=10, fre: float=0.5) -> WebElement:
    #     # by_str = MobileBy.XPATH
    #     if by == 'xpath':
    #         by_str = MobileBy.XPATH
    #     elif by == 'accessibility_id':
    #         by_str = MobileBy.ACCESSIBILITY_ID
    #     elif by == 'class_name':
    #         by_str = MobileBy.CLASS_NAME
    #     else:
    #         raise Exception('by is error')
    #     element = WebDriverWait(self.driver, wait, poll_frequency=fre
    #                             ).until(EC.presence_of_element_located
    #                                                       ((by_str, value)))
    #     print(element)
    #     return element
