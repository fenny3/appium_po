# -*- coding:utf-8 -*-

"""
@Time    : 2019-05-28 15:06
@Author  : fenny.ren
@File    : LoginPage.py
"""
import os

import yaml
import allure
from selenium.webdriver.common.by import By

from src.page.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self):
        super(LoginPage, self).__init__()
        with open(os.path.join(BasePage.element, 'login_page.yaml'), 'r') as rf:
            self.element: dict = yaml.load(rf.read())

    def login_by_wx(self):
        pass

    def login_by_msg(self):
        pass

    def login_by_passwd(self, account, passed):
        with allure.step('选择手机号及其他方式登录'):
            self.find((By.ID, self.element['other_locator']['id'])).click()
        with allure.step('选择帐号密码登录'):
            self.find((By.ID, self.element['tv_login_with_account']['id'])).click()
        with allure.step('输入用户名'):
            self.find((By.ID, self.element['login_account']['id'])).send_keys(account)
        with allure.step('输入密码'):
            self.find((By.ID, self.element['login_password']['id'])).send_keys(passed)
        with allure.step('点击登录按钮'):
            self.find((By.ID, self.element['button_next']['id'])).click()
        return self

    def login_success_by_passwd(self):
        pass

    def back(self):
        from src.page.ProfilePage import ProfilePage
        self.find((By.XPATH, self.element['close_button']['xpath'])).click()
        return ProfilePage()

    def get_error_msg(self):
        msg = self.find((By.ID, self.element['error_msg']['id'])).text
        self.find_by_text("确定").click()
        return msg