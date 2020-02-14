import unittest
import api
from api.api_employee import ApiEmployee
from tools.assert_common import assert_common


class TestEmployee(unittest.TestCase):
    # 1. 初始化方法
    @classmethod
    def setUpClass(cls) -> None:
        # 获取ApiEmployee对象
        cls.api = ApiEmployee()

    # 2. 新增员工 接口测试方法
    def test01_post(self, username="tonew1-1004", mobile="17010331120", worNumber="10233402"):
        # 调用新增员工接口
        r = self.api.api_post_employee(username, mobile, worNumber)
        # 断言
        assert_common(self, r)
        print("新增员工结果：", r.json())
        # 提取 user_id
        api.user_id = r.json().get("data").get("id")
        print("员工user_id值为：", api.user_id)

    # 3. 更新员工 接口测试方法
    def test02_put(self):
        pass

    # 4. 查询员工 接口测试方法
    def test03_get(self):
        pass

    # 5. 删除员工 接口测试方法
    def test04_delete(self):
        # 调用删除员工接口
        r = self.api.api_delete_employee()
        print("删除结果为：", r.json())
        # 断言
        assert_common(self, r)
