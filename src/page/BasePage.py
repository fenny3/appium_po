# -*- coding:utf-8 -*-

"""
@Time    : 2019-05-28 14:53
@Author  : fenny.ren
@File    : BasePage.py
"""
import os
import time
import yaml
import allure
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.driver.Client import Client

routes = os.path.abspath(__file__).split('/')
ROOT = '/'.join(routes[:routes.index('appium_po') + 1])

logging.basicConfig(level=logging.INFO,
                    format='[%(levelname)s %(asctime)s %(filename)s %(funcName)s line:%(lineno)d]: %(message)s',
                    datefmt='%y%m%d %H:%M:%S')


class BasePage:

    element = os.path.join(ROOT, 'src', 'element')

    def __init__(self):
        self.driver: WebDriver = self.get_driver()

    @classmethod
    def get_driver(cls):
        return Client.driver

    @classmethod
    def get_client(cls):
        return Client

    def find_by_text(self, text: str) -> WebElement:
        return self.find(By.XPATH, "//*[contains(@text, '%s')]" % text)

    def find(self, by, value) -> WebElement:
        # todo:
        #  需要加上智能查找元素的支持
        #  先黑名单，如果在黑名单中，先处理
        #  黑名单中仍未解决问题，找到页面的最顶层元素进行点击
        #  针对动态变化位置的元素，可以支持查找两三次看看位置是否不变，则稳定
        for i in range(3):
            try:
                element = self.driver.find_element(by, value)
                return element
            except WebDriverException as e:
                self.driver.back()
                if i == 2:
                    logging.info(str(e))
                    raise WebDriverException(e)

    def load_steps(self, path, key, **kwargs):
        with open(path, 'r') as f:
            po_data = yaml.load(f.read())
        po_method = po_data[key]
        if 'elements' in po_data:
            po_elements = po_data['elements']
        for step in po_method:
            logging.info(step)
            if 'element' in step:
                element_dict = po_elements[step['element']][Client.platform]
            else:
                element_dict = {'by': step['by'], 'locator': step['locator']}
            tips = step['tips'] if 'tips' in step else '操作元素：{}'.format(element_dict['locator'])
            if '$' in element_dict['locator']:
                for k, v in kwargs.items():
                    origin: str = element_dict['locator']
                    element_dict['locator'] = origin.replace('$%s' % k, v)
                    logging.info('origin: {}, new: {}'.format(origin, element_dict['locator']))
                    if origin != element_dict['locator']:
                        del kwargs[k]
                    if '$' not in element_dict['locator']:
                        break
            logging.info('元素的定位符是：{}'.format(element_dict['locator']))
            with allure.step(tips):
                if element_dict['by'] == 'text':
                    element: WebElement = self.find_by_text(element_dict['locator'])
                else:
                    element: WebElement = self.find(by=element_dict['by'], value=element_dict['locator'])
                action = str(step['action']).lower()
                if action == 'click':
                    element.click()
                elif action == 'send_keys':
                    for k, v in kwargs.items():
                        origin: str = step['text']
                        new = origin.replace('$%s' % k, v)
                        logging.info('origin: {}, new: {}'.format(origin, new))
                        if origin != new:
                            del kwargs[k]
                            break
                    element.send_keys(new)
                elif action == 'text':
                    return element.text
                elif action == 'get_attribute':
                    return element.get_attribute(step['attribute'])
                else:
                    logging.info('UNKNOW COMMAND %s' % step)

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
