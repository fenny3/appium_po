# -*- coding:utf-8 -*-

"""
@Time    : 2019-05-29 00:40
@Author  : fenny.ren
@File    : test_selected.py
"""

import pytest
import allure

from src.page.App import App


@allure.feature('测试自选股')
class TestSelected:

    @classmethod
    def setup_class(cls):
        cls.selected_page = App.main().goto_selected()

    @allure.story('测试股票价格')
    def test_price(self):
        assert self.selected_page.goto_hs().get_price_by_name('科大讯飞') == 28.83


