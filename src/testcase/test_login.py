# -*- coding:utf-8 -*-

"""
@Time    : 2019-05-29 00:40
@Author  : fenny.ren
@File    : test_login.py
"""

import pytest
import allure

from src.page.App import App

@allure.feature('测试登录功能')
class TestLogin:

    @classmethod
    def setup_class(cls):
        cls.profile_page = App.main().goto_profile()

    def setup_method(self):
        self.login_page = self.profile_page.goto_login()

    @allure.story('测试非法的手机号验证码登录提示正确')
    @pytest.mark.parametrize('account, passwd, msg', [("156005347600", "111111", "手机号码"),
                                                      ("15600534760", "111111", "密码错误")])
    def test_login_passwd(self, account, passwd, msg):
        self.login_page.login_by_passwd(account, passwd)
        assert msg in self.login_page.get_error_msg()

    def teardown_method(self):
        self.login_page.back()

    @classmethod
    def teardown_class(cls):
        pass

