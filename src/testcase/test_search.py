# -*- coding:utf-8 -*-

"""
@Time    : 2019-05-29 00:40
@Author  : fenny.ren
@File    : test_search.py
"""

import pytest
import allure

from src.page.App import App

@allure.feature('测试搜索功能')
class TestSearch:

    @classmethod
    def setup_class(cls):
        cls.search_page = App.main().goto_search()


    @allure.story('验证股票未添加状态')
    @pytest.mark.parametrize("key, code", [("招商银行", "SH600036"),
                                           ("平安银行", "SZ000001"),
                                           ("pingan", "SH601318")
                                           ])
    def test_is_selected_stock_hs(self, key, code):
        self.search_page.search(key)
        assert self.search_page.is_selected(code) == False

    # def test_is_selected_stock(self):
    #     self.search_page.search('alibaba')
    #
    # @allure.story('测试添加股票')
    # @pytest.mark.parametrize('key, code', [('招商银行', 'SH600036')])
    # def test_add_stock_hs(self, key, code):
    #     search_page = self.search_page.search(key)
    #     if search_page.is_selected(code):
    #         search_page.click_selected(code)
    #     search_page.click_selected(code)
    #     assert search_page.is_selected(code) == True
    #
    # @allure.story('验证用户未关注的状态')
    # @pytest.mark.parametrize('key,code', [('fenny', 'Fenny')])
    # def test_is_follow_user(self, key, code):
    #     self.search_page.search(key)
    #     assert self.search_page.is_followed(code) == False
