# -*- coding:utf-8 -*-

"""
@Time    : 2019-05-28 15:06
@Author  : fenny.ren
@File    : LoginPage.py
"""
import os
import logging

import yaml
import allure
from selenium.webdriver.common.by import By

from src.page.BasePage import BasePage


class LoginPage(BasePage):

    def login_by_wx(self):
        pass

    def login_by_msg(self):
        pass

    def login_by_passwd(self, account, passwd):
        #### todo： yaml中增加注释，在loadyaml中增加allure step

        self.load_steps('/Users/feeny/Touchpal/appium_po/src/data/LoginPage.yaml', 'login_by_passwd', account=account, passwd=passwd)

        # with allure.step('选择手机号及其他方式登录'):
        #     self.find((By.ID, self.element['other_locator']['id'])).click()
        # with allure.step('选择帐号密码登录'):
        #     self.find((By.ID, self.element['tv_login_with_account']['id'])).click()
        # with allure.step('输入用户名'):
        #     self.find((By.ID, self.element['login_account']['id'])).send_keys(account)
        # with allure.step('输入密码'):
        #     self.find((By.ID, self.element['login_password']['id'])).send_keys(passed)
        # with allure.step('点击登录按钮'):
        #     self.find((By.ID, self.element['button_next']['id'])).click()
        return self

    def login_success_by_passwd(self):
        pass

    def back(self):
        # self.find((By.XPATH, self.element['close_button']['xpath'])).click()
        from src.page.ProfilePage import ProfilePage
        self.load_steps('/Users/feeny/Touchpal/appium_po/src/data/LoginPage.yaml', 'back')
        return ProfilePage()

    def get_error_msg(self):
        # msg = self.find((By.ID, self.element['error_msg']['id'])).text
        msg = self.load_steps('/Users/feeny/Touchpal/appium_po/src/data/LoginPage.yaml', 'get_error_msg')
        logging.info('msg is: {}'.format(msg))
        self.find_by_text("确定").click()
        return msg