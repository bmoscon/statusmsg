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

    with status("testing", 'OK', 'FAIL', progress=500) as progress_bar:
        counter = 0
        for i in range(500):
            counter = i - 10
            progress_bar.update()
            sleep(0.01)
            #if i == 350:
            #    raise ValueError