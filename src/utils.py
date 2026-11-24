"""一些简单的小工具函数。"""


def add(a: float, b: float) -> float:
    """返回两数之和。"""
    return a + b


def mean(values: list[float]) -> float:
    """返回平均值；空列表返回 0。"""
    if not values:
        return 0.0
    return sum(values) / len(values)
