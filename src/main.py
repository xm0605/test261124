"""程序入口：打印问候语并跑一个小计算。"""

from utils import add


def greet(name: str) -> str:
    return f"Hello, {name}!"


def main() -> None:
    print(greet("test261124"))
    print(f"2 + 3 = {add(2, 3)}")


if __name__ == "__main__":
    main()
