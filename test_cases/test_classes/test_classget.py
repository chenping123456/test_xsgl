#导入两个包
import requests
import unittest
#设计用例：班级查询所有，预期结果：查询成功
class TestClassGte(unittest.TestCase):
    def test_classGet(self):
        url = r'http://127.0.0.1:8000/api/departments/gkl/classes'
        res = requests.get(url)
        print(res.text)
        self.assertEqual(200, res.status_code)

#设计用例：班级查询指定，预期结果：查询成功
class TestClassGte01(unittest.TestCase):
    def test_classGet01(self):
        url = r'http://127.0.0.1:8000/api/departments/gkl/classes/1/'
        res = requests.get(url)
        print(res.text)
        self.assertEqual(200, res.status_code)

#设计用例：班级-列表查询，预期结果：查询成功
class TestClassGte02(unittest.TestCase):
    def test_classGet02(self):
        url = r'http://127.0.0.1:8000/api/departments/gkl/classes/?$cls_id_list=9,10'
        res = requests.get(url)
        print(res.text)
        self.assertEqual(200, res.status_code)

#设计用例：班级-列表查询-组合查询，预期结果：查询成功
class TestClassGte03(unittest.TestCase):
    def test_classGet03(self):
        url = r'http://127.0.0.1:8000/api/departments/gkl/classes/?$cls_id_list=9,10&$master_name_list=Master201,Master202'
        res = requests.get(url)
        print(res.text)
        self.assertEqual(200, res.status_code)

#设计用例：班级-条件查询，预期结果：查询成功
class TestClassGte04(unittest.TestCase):
    def test_classGet04(self):
        url = r'http://127.0.0.1:8000/api/departments/gkl/classes/?cls_name=Test学院6'
        res = requests.get(url)
        print(res.text)
        self.assertEqual(200, res.status_code)

#设计用例：班级-条件查询-组合查询，预期结果：查询成功
class TestClassGte05(unittest.TestCase):
    def test_classGet05(self):
        url = r'http://127.0.0.1:8000/api/departments/gkl/classes/?cls_name=Test学院98&master_name=Master26&slogan=slogan57'
        res = requests.get(url)
        print(res.text)
        self.assertEqual(200, res.status_code)

#设计用例：班级-模糊查询，预期结果：查询成功
class TestClassGte06(unittest.TestCase):
    def test_classGet06(self):
        url = r'http://127.0.0.1:8000/api/departments/test01/classes/?blur=1&cls_name=2020级39'
        res = requests.get(url)
        print(res.text)
        self.assertEqual(200, res.status_code)

#设计用例：班级-模糊查询-组合查询，预期结果：查询成功
class TestClassGte07(unittest.TestCase):
    def test_classGet07(self):
        url = r'http://127.0.0.1:8000/api/departments/gkl/classes/?blur=1&cls_name=Test学院6&master_name=Master73'
        res = requests.get(url)
        print(res.text)
        self.assertEqual(200, res.status_code)

if __name__ == '__main__':
    unittest.main()
