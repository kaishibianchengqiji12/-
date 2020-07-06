# -*- coding: utf-8 -*-
import random
from xpinyin import Pinyin
import requests
import re
import threading
import time


class TestThread(threading.Thread):

    def __init__(self, x):
        super(TestThread, self).__init__()
        self.x = x

    def run(self):
        time.sleep(self.x)
        print(str(self.x))

    def result(self):
        return self.x


t1 = TestThread(1)
t2 = TestThread(3)
t1.start()
t2.start()
t1.join()  # 等待线程结束
t2.join()
print(t1.name)
print(t2.name)
print(t1.result(), t2.result())
print(t1.is_alive())
