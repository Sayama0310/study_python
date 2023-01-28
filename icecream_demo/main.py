from icecream import ic


def add_two(a: int) -> int:
    print('called')
    return a + 2

if __name__ == '__main__':
    ic(add_two(4))