from datetime import datetime
import inspect
import executing


class ToyIceCreamDebugger:

    def __init__(self):
        self.prefix = 'toy ic| '
        self.outputFunction = print

    def __call__(self, *args):
        callFrame = inspect.currentframe().f_back
        out = self._format(callFrame, *args)
        self.outputFunction(out)

        if not args:  # E.g. ic().
            passthrough = None
        elif len(args) == 1:  # E.g. ic(1).
            passthrough = args[0]
        else:  # E.g. ic(1, 2, 3).
            passthrough = args

        return passthrough

    def _format(self, callFrame, *args):
        prefix = self.prefix
        callNode = executing.Source.executing(callFrame).node
        if callNode is None:
            raise Exception()

        if not args:  # E.g. ic().
            time = str(datetime.now())
            out = prefix + time
        else:
            out = prefix + str(list(zip(callNode.args, args)))

        return out


toy_ic = ToyIceCreamDebugger()

if __name__ == '__main__':

    def add_two(a: int) -> int:
        toy_ic()
        return a + 2

    x = toy_ic(add_two(4), 7)
    print(x)
