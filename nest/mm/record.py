import os
import threading
import time

import objgraph

report_file = '/tmp/leopard.rep'


class timer(threading.Thread):  # The timer class is derived from the class threading.Thread
    def __init__(self, num, interval, timeout=None):
        threading.Thread.__init__(self)
        self.thread_num = num
        self.timeout = timeout
        self.count = 0
        self.interval = interval
        self.thread_stop = False

    def run(self):  # Overwrite run() method, put what you want the thread do here
        while not self.thread_stop:
            with open(report_file, 'a') as fp:
                fp.write('Thread Object(%d), Time:%s, Count:%d, Pid:%d' %
                         (self.thread_num,
                          time.ctime(),
                          self.count,
                          os.getpid()))
                objgraph.show_growth(4, file=fp)
            time.sleep(self.interval)
            self.verify()

    def verify(self):
        self.count += 1
        if self.timeout and self.count > self.timeout:
            self.stop()

    def stop(self):
        self.thread_stop = True


def show_object(interval=2, times=10):  # Use thread.start_new_thread() to create 2 new threads
    shower = timer(1, interval, times)
    shower.start()
