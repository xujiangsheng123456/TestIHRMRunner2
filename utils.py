import json
def assert_common_utils(self,response,http_code,success,code,message):
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))

def read_login_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        jsonData= json.load(f)
        read_list = []
        for login_data in jsonData:
            read_list.append(tuple(login_data.values()))
    return read_list

def read_emp_data(filename,interface_name):
     with open(filename, "r", encoding="utf-8") as f:
         jsonData = json.load(f)
         ret_list = []
         ret_list.append(tuple(jsonData.get(interface_name).values()))
     return ret_list


