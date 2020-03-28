import unittest
import time

from HTMLTestRunner_PY3 import HTMLTestRunner

import app
from script.test_emp2 import TestEmp
from script.test_login_param import TestLogin

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestEmp))
now_time = time.strftime("%Y%m%d_%H%M%S")
file_path = app.base_path + "/report/ihrm{}.html".format(now_time)
with open(file_path, "wb") as f :
    runner = HTMLTestRunner(f,verbosity=2,description="关于ihrm的报告",title="ihrm执行结果")
    runner.run(suite)