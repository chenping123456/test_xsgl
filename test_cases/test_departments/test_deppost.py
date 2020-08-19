#导入两个包
import requests
import unittest
#设计用例：
class TestDepPost(unittest.TestCase):
    def test_depPost(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        # 设置信息头
        req_head = {"Content-Type": "application/json"}
        # 设置消息体
        req_data = r'{"data": [{"dep_id":"TA01","dep_name":"Python学院3班","master_name":"Test-Master","slogan":"day day up"}]}'
        res = requests.post(url,data=req_data.encode('utf-8'),headers=req_head)
        self.assertEqual(201,res.status_code)

#设计用例：slogan为空的测试用例，测试是否新增成功
class TestDepPost02(unittest.TestCase):
    def test_depPost02(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        # 设置信息头
        req_head = {"Content-Type": "application/json"}
        # 设置消息体
        req_data = r'{"data": [{"dep_id":"TA01","dep_name":"Python学院2班","master_name":"python-Master","slogan":""}]}'
        res = requests.post(url,data=req_data.encode('utf-8'),headers=req_head)
        self.assertEqual(201,res.status_code)

#设计用例：depid必填为空，看是否可以新增成功；预期结果：新增失败
class TestDepPost03(unittest.TestCase):
    def test_depPost03(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        # 设置信息头
        req_head = {"Content-Type": "application/json"}
        # 设置消息体
        req_data = r'{"data": [{"dep_id":"","dep_name":"Python学院3班","master_name":"python-Master","slogan":"好好学习"}]}'
        res = requests.post(url,data=req_data.encode('utf-8'),headers=req_head)
        self.assertEqual(400,res.status_code)

#设计用例：depname必填为空，看是否可以新增成功；预期结果：新增失败
class TestDepPost04(unittest.TestCase):
    def test_depPost04(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        # 设置信息头
        req_head = {"Content-Type": "application/json"}
        # 设置消息体
        req_data = r'{"data": [{"dep_id":"TA003","dep_name":"","master_name":"python-Master","slogan":"好好学习"}]}'
        res = requests.post(url,data=req_data.encode('utf-8'),headers=req_head)
        self.assertEqual(400,res.status_code)

#设计用例：mastername必填为空，看是否可以新增成功；预期结果：新增失败
class TestDepPost05(unittest.TestCase):
    def test_depPost05(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        # 设置信息头
        req_head = {"Content-Type": "application/json"}
        # 设置消息体
        req_data = r'{"data": [{"dep_id":"TA003","dep_name":"测试学院","master_name":"","slogan":"好好学习"}]}'
        res = requests.post(url,data=req_data.encode('utf-8'),headers=req_head)
        self.assertEqual(400,res.status_code)

#设计用例：所有参数取最大值，看是否可以新增成功；预期结果：新增成功
class TestDepPost06(unittest.TestCase):
    def test_depPost06(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        # 设置信息头
        req_head = {"Content-Type": "application/json"}
        # 设置消息体
        req_data = r'{"data": [{"dep_id":"乌乌乌乌000001","dep_name":"乌鲁木齐银川甘肃黄河入海流长江河北拉萨哈","master_name":"乌鲁木齐银川甘肃黄河入海流长江河北拉萨哈","slogan":"乌鲁木齐银川甘肃黄河入海流长江河北拉萨哈乌鲁木齐银川甘肃黄河入海流长江河北拉萨哈乌鲁木齐银川甘肃黄河入海流长江河北拉萨哈乌鲁木齐银川甘肃黄河入海流长江河北拉萨哈乌鲁木齐银川甘肃黄河入海流长江河北拉萨哈"}]}'
        res = requests.post(url,data=req_data.encode('utf-8'),headers=req_head)
        self.assertEqual(201,res.status_code)

#设计用例：所有参数取最小值，看是否可以新增成功；预期结果：新增成功
class TestDepPost07(unittest.TestCase):
    def test_depPost07(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        # 设置信息头
        req_head = {"Content-Type": "application/json"}
        # 设置消息体
        req_data = r'{"data": [{"dep_id":"二","dep_name":"三","master_name":"四","slogan":"五"}]}'
        res = requests.post(url,data=req_data.encode('utf-8'),headers=req_head)
        self.assertEqual(201,res.status_code)

#设计用例：depid参数超过最大值，看是否可以新增成功；预期结果：新增失败。bug：depid超长新增成功
class TestDepPost08(unittest.TestCase):
    def test_depPost08(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        # 设置信息头
        req_head = {"Content-Type": "application/json"}
        # 设置消息体
        req_data = r'{"data": [{"dep_id":"中国是个好地方啊好地方方方方","dep_name":"三","master_name":"四","slogan":"五"}]}'
        res = requests.post(url,data=req_data.encode('utf-8'),headers=req_head)
        self.assertEqual(201,res.status_code)

#设计用例：dename参数超过最大值，看是否可以新增成功；预期结果：新增失败
class TestDepPost09(unittest.TestCase):
    def test_depPost09(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        # 设置信息头
        req_head = {"Content-Type": "application/json"}
        # 设置消息体
        req_data = r'{"data": [{"dep_id":"Java学院","dep_name":"Java院长是院长是院长是院长每天很忙碌很忙碌教学生带学生","master_name":"Java院长","slogan":"五"}]}'
        res = requests.post(url,data=req_data.encode('utf-8'),headers=req_head)
        self.assertEqual(400,res.status_code)

#设计用例：mastername参数超过最大值，看是否可以新增成功；预期结果：新增失败
class TestDepPost10(unittest.TestCase):
    def test_depPost10(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        # 设置信息头
        req_head = {"Content-Type": "application/json"}
        # 设置消息体
        req_data = r'{"data": [{"dep_id":"Java学院","dep_name":"Java院长","master_name":"Java院长院长Java院长院长Java院长院长Java院长院长Java院长院长","slogan":"五"}]}'
        res = requests.post(url,data=req_data.encode('utf-8'),headers=req_head)
        self.assertEqual(400,res.status_code)

#设计用例：slogan参数超过最大值，看是否可以新增成功；预期结果：新增失败
class TestDepPost11(unittest.TestCase):
    def test_depPost11(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        # 设置信息头
        req_head = {"Content-Type": "application/json"}
        # 设置消息体
        req_data = r'{"data": [{"dep_id":"Java学院","dep_name":"Java学院","master_name":"Java院长","slogan":"江南柳叶小未成阴人为丝轻那忍折莺嫌枝嫩不胜吟留著待春深十四五，闲抱琵琶寻阶上簸钱阶下走恁时相见早留心何况到如今江南柳叶小未成阴人为丝轻那忍折莺嫌枝嫩不胜吟留著待春深十四五，闲抱琵琶寻阶上簸钱阶下走恁时相见早留心何况到如今江南柳叶小未成阴人为丝轻那忍折莺嫌枝嫩不胜吟留著待春深十四五，闲抱琵琶寻阶上簸钱阶下走恁时相见早留心何况到如今江南柳叶小未成阴人为丝轻那忍折莺嫌枝嫩不胜吟留著待春深十四五，闲抱琵琶寻阶上簸钱阶下走恁时相见早留心何况到如今"}]}'
        res = requests.post(url,data=req_data.encode('utf-8'),headers=req_head)
        self.assertEqual(400,res.status_code)

#设计用例：depid前后加上#，看是否可以新增成功；预期结果：新增失败。bug:depid前后加特殊符号新增成功
class TestDepPost12(unittest.TestCase):
    def test_depPost12(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        # 设置信息头
        req_head = {"Content-Type": "application/json"}
        # 设置消息体
        req_data = r'{"data": [{"dep_id":"#Java学院#","dep_name":"Java学院附中","master_name":"Java院长","slogan":"江南柳叶小未成阴人为丝轻那忍折莺嫌枝嫩不胜吟留著待春"}]}'
        res = requests.post(url,data=req_data.encode('utf-8'),headers=req_head)
        self.assertEqual(400,res.status_code)

#设计用例：depid前后加上@，看是否可以新增成功；预期结果：新增失败 bug:depid前后加特殊符号新增成功
class TestDepPost13(unittest.TestCase):
    def test_depPost13(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        # 设置信息头
        req_head = {"Content-Type": "application/json"}
        # 设置消息体
        req_data = r'{"data": [{"dep_id":"@Test学院@","dep_name":"Test学院附中","master_name":"Test院长","slogan":"闲抱琵琶寻阶上簸钱阶下走恁时相见早留心何"}]}'
        res = requests.post(url,data=req_data.encode('utf-8'),headers=req_head)
        self.assertEqual(400,res.status_code)

#设计用例：depid前后加上%，看是否可以新增成功；预期结果：新增失败 bug:depid前后加特殊符号新增成功
class TestDepPost14(unittest.TestCase):
    def test_depPost14(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        # 设置信息头
        req_head = {"Content-Type": "application/json"}
        # 设置消息体
        req_data = r'{"data": [{"dep_id":"%Test学院1号院%","dep_name":"Test学院附中","master_name":"Test副院长","slogan":"相见早留心何"}]}'
        res = requests.post(url,data=req_data.encode('utf-8'),headers=req_head)
        self.assertEqual(400,res.status_code)

#设计用例：depid前后加上&，看是否可以新增成功；预期结果：新增失败 bug:depid前后加特殊符号新增成功
class TestDepPost15(unittest.TestCase):
    def test_depPost15(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        # 设置信息头
        req_head = {"Content-Type": "application/json"}
        # 设置消息体
        req_data = r'{"data": [{"dep_id":"&Python学院1号院&","dep_name":"Python学院附中","master_name":"Python副院长","slogan":"下课了"}]}'
        res = requests.post(url,data=req_data.encode('utf-8'),headers=req_head)
        self.assertEqual(400,res.status_code)

if __name__ == '__main__':
    unittest.main()