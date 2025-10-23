# 补充去重函数（文档要求的核心功能）
def dedupe_list(input_list):
    """移除列表中的重复元素，保持原顺序"""
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# （可选）若之前添加了加法函数，需确保定义正确
def add_two_numbers(a, b):
    """计算两个数的和"""
    return a + b

# 本地运行测试代码
if __name__ == "__main__":
    test_list = [1, 2, 2, 3]
    print(f"去重结果：{dedupe_list(test_list)}")  # 现在可正常调用dedupe_list
    # 若有加法函数，添加测试
    print(f"1+2={add_two_numbers(1, 2)}")