import unittest
import logging
import requests
import pymysql
import app
from api.emp_api import EmpApi
from api.login_api import LoginApi
from utils import assert_common_utils, read_emp_data
from parameterized import parameterized
filename = app.base_path +"/data/emp.json"

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
        app.HEADERS = {"Content-Type":"application/json", "Authorization":"Bearer " +token}
        logging.info("登录成功后设置的请求头为: {}".format(app.HEADERS))
    @parameterized.expand(read_emp_data(filename,"add_emp"))
    def test02_add_emp(self,username,mobile,http_code,success,code,message):
        response = self.emp_api.add_emp(username, mobile, app.HEADERS)
        logging.info("添加员工的的结果为{}".format(response.json()))

        add_result = response.json()
        app.EMP_ID= add_result.get("data").get("id")
        logging.info("获取员工id为:{}".format(app.EMP_ID))
        assert_common_utils(self, response,http_code,success,code,message)
    @parameterized.expand(read_emp_data(filename,"query_emp"))
    def test03_query_emp(self,http_code,success,code,message):
        response = self.emp_api.query_emp(app.EMP_ID,app.HEADERS)
        logging.info("查询员工的结果是:{}".format(response.json()))
        assert_common_utils(self, response,http_code,success,code,message)

    @parameterized.expand(read_emp_data(filename, "modify_emp"))
    def test04_modify_emp(self,username,http_code,success,code,message):
        response =self.emp_api.modify_emp(app.EMP_ID,username, headers=app.HEADERS)
        logging.info("修改员工的结果是:{}".format(response.json()))
        assert_common_utils(self, response, http_code,success,code,message)


        conn = pymysql.connect(host="182.92.81.159",user="readuser",password="iHRM_user_2019",database="ihrm")
        cursor = conn.cursor()
        sql="select username from bs_user where id ={}".format(app.EMP_ID)
        logging.info("打印sql语句查询的结果为: {}".format(sql))
        cursor.execute(sql)
        result = cursor.fetchone()
        logging.info("执行sql语句查询的结果为:{}".format(result))
        cursor.close()
        conn.close()
        self.assertEqual(username, result[0])

    @parameterized.expand(read_emp_data(filename, "delete_emp"))
    def test05_delete_emp(self,http_code,success,code,message):
        response = self.emp_api.delete_emp(app.EMP_ID,  app.HEADERS)
        logging.info("删除员工的结果是:{}".format(response.json()))
        assert_common_utils(self, response, http_code,success,code,message)
