# -*- coding:utf-8 -*-

"""
@Time    : 2019-06-04 17:53
@Author  : fenny.ren
@File    : test_quotation.py
"""
import allure
import pytest

from src.page.App import App


@allure.feature('行情模块')
class TestQuotation:

    @classmethod
    def setup_class(cls):
        cls.quotation_page = App.main().goto_quotation()

    @pytest.mark.parametrize('name', ['深证成指'])
    def test_index_price(self, name):
        assert self.quotation_page.get_index_price(name) > 8000
