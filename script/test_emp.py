import unittest
import logging
import requests

import app
from api.emp_api import EmpApi
from api.login_api import LoginApi
from utils import assert_common_utils


class TestEmp(unittest.TestCase):
    def setUp(self):
        self.login_api = LoginApi()
        self.emp_api = EmpApi()
        self.emp_url = "http://182.92.81.159" + "/api/sys/user"
    def tearDown(self):
        ...
    def test01_test_emp_operation(self):
        response = self.login_api.login({"mobile":"13800000002","password":"123456"}, headers=app.HEADERS)
        result = response.json()
        logging.info("登录后返回的数据{}".format(result))
        token = result.get("data")
        headers = {"Content-Type":"application/json", "Authorization":"Bearer " +token}
        logging.info("登录成功后设置的请求头为: {}".format(headers))
        response = self.emp_api.add_emp("奥特曼100super282129", "17357782683", headers)
        logging.info("添加员工的的结果为{}".format(response.json()))

        add_result = response.json()
        emp_id= add_result.get("data").get("id")
        logging.info("获取员工id为:{}".format(emp_id))
        assert_common_utils(self, response, 200, True, 10000, "操作成功")

        response = self.emp_api.query_emp(emp_id,headers)
        logging.info("查询员工的结果是:{}".format(response.json()))
        assert_common_utils(self, response, 200, True, 10000, "操作成功")
        response =self.emp_api.modify_emp(emp_id,"哈哈活动结束1", headers=headers)
        logging.info("修改员工的结果是:{}".format(response.json()))
        assert_common_utils(self, response, 200, True, 10000, "操作成功")

        response = self.emp_api.delete_emp(emp_id,  headers)
        logging.info("删除员工的结果是:{}".format(response.json()))
        assert_common_utils(self, response, 200, True, 10000, "操作成功")
