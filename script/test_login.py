import unittest
import requests
import logging

import app
from api.login_api import LoginApi
from utils import assert_common_utils
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login_api = LoginApi()
    def tearDown(self):
        ...
    def test01_login_success(self):
        jsonData = {"mobile": "13800000002", "password": "123456"}
        response = self.login_api.login(jsonData, app.HEADERS)
        logging.info("登录结果为:{}".format(response.json()))
        assert_common_utils(self,response,200,True,10000,"操作成功")
    def test02_mobile_not_exists(self):
        jsonData = {"mobile": "13900000002", "password": "123456"}
        response = self.login_api.login(jsonData, app.HEADERS)
        logging.info("登录结果为:{}".format(response.json()))
        assert_common_utils(self,response,200,False,20001,"用户名或密码错误")
    def test03_password_is_error(self):
        jsonData = {"mobile": "13800000002", "password": "12345"}
        response = self.login_api.login(jsonData, app.HEADERS)
        logging.info("登录结果为:{}".format(response.json()))
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    def test04_mobile_has_english(self):
        jsonData = {"mobile": "138aV000002", "password": "123456"}
        response = self.login_api.login(jsonData, app.HEADERS)
        logging.info("登录结果为:{}".format(response.json()))
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    def test05_mobile_has_special(self):
        jsonData = {"mobile": "138%#000002", "password": "123456"}
        response = self.login_api.login(jsonData, app.HEADERS)
        logging.info("登录结果为:{}".format(response.json()))
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    def test06_mobile_is_empty(self):
        jsonData = {"mobile": "", "password": "123456"}
        response = self.login_api.login(jsonData, app.HEADERS)
        logging.info("登录结果为:{}".format(response.json()))
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    def test07_password_is_empty(self):
        jsonData = {"mobile": "13800000002", "password": ""}
        response = self.login_api.login(jsonData, app.HEADERS)
        logging.info("登录结果为:{}".format(response.json()))
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    def test08_more_params(self):
        jsonData = {"mobile": "13800000002", "password": "123456","sign":"123"}
        response = self.login_api.login(jsonData, app.HEADERS)
        logging.info("登录结果为:{}".format(response.json()))
        assert_common_utils(self,response,200,True,10000,"操作成功")
    def test09_less_mobile(self):
        jsonData = {"password": "123456"}
        response = self.login_api.login(jsonData, app.HEADERS)
        logging.info("登录结果为:{}".format(response.json()))
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    def test10_less_password(self):
        jsonData = {"password": "123456"}
        response = self.login_api.login(jsonData, app.HEADERS)
        logging.info("登录结果为:{}".format(response.json()))
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    def test11_none_params(self):
        jsonData = None
        response = self.login_api.login(jsonData, app.HEADERS)
        logging.info("登录结果为:{}".format(response.json()))
        assert_common_utils(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试")
    def test12_params_is_error(self):
        jsonData = {"mole": "13800000002", "password": "123456"}
        response = self.login_api.login(jsonData, app.HEADERS)
        logging.info("登录结果为:{}".format(response.json()))
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
