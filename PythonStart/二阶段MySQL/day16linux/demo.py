import threading
import time
def func():
    time.sleep(3)
    print('我是子线程')

if __name__ == '__main__':
    print('start')
    t = threading.Thread(target=func)
    t.start()
    #time.sleep(4)
    print('end')
