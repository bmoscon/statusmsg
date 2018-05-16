from statusmsg import decorator, status
from time import sleep

@decorator('running', 'OK', 'ERROR')
def f():
    sleep(2)


@decorator('installing', 'OK', 'FAILED')
def f2():
    sleep(2)
    raise ValueError()


def test():
    sleep(2)
    raise Exception()


if __name__ == '__main__':
    with status('testing', 'PASS', 'FAIL', suppress=True):
        test()

    f()
    try:
        f2()
    except:
        pass
