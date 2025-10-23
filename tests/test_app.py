# 新增：将项目根目录添加到Python搜索路径
import sys
import os
# 获取当前测试文件的目录（tests/）
test_dir = os.path.dirname(os.path.abspath(__file__))
# 项目根目录 = tests/ 的上一级目录
project_root = os.path.dirname(test_dir)
# 将根目录添加到Python路径
sys.path.append(project_root)

# 之后再导入app模块
# 无需手动加路径，直接导入
from app.app import dedupe_list, add_two_numbers
# 测试代码不变...

# 以下是原测试代码
def test_dedupe_basic():
    assert dedupe_list([1, 2, 2, 3]) == [1, 2, 3]

def test_dedupe_empty():
    assert dedupe_list([]) == []

def test_add_two_numbers():
    assert add_two_numbers(1, 2) == 3