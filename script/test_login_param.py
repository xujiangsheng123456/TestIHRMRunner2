import unittest
import requests
import logging
from parameterized import parameterized
import app
from api.login_api import LoginApi
from utils import assert_common_utils, read_login_data


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login_api = LoginApi()
    def tearDown(self):
        ...
    filename = app.base_path +"/data/login.json"
    @parameterized.expand(read_login_data(filename))
    def test_login_params(self,casename,jsonData,http_code,success,code,message):

        response = self.login_api.login(jsonData, app.HEADERS)
        logging.info("登录结果为:{}".format(response.json()))
        assert_common_utils(self,response,http_code,success,code,message)

