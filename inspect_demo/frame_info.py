import inspect
import pprint
from icecream import ic


def some_function_c():
    # 呼び出し元のスタックフレームの「Frame Object」
    current_frame = inspect.currentframe()
    ic(current_frame)
    
    # 呼び出し元のスタックフレームの「FrameInfoオブジェクト」のリスト
    stack = inspect.stack()
    ic(stack)
    
    # 現在のフレームと、現在処理中の例外が発生したフレームとの間のスタックの「FrameInfoオブジェクト」のリスト。
    # リストの最初のエントリは呼び出し元を表し、最後のエントリは例外が発生した場所を表します。
    trace = inspect.trace()
    ic(trace)
    
    current_frame_info = inspect.getframeinfo(current_frame)
    pprint.pp(current_frame_info.code_context)
    
    outer_frame_info = inspect.getouterframes(current_frame)
    ic(outer_frame_info)


def some_function_b():
    some_function_c()


def some_function_a():
    some_function_b()


if __name__ == '__main__':
    some_function_a()
