import time
from contextlib import contextmanager

class cm_timer_1:
    def __enter__(self):
        self.start=time.time()
        return self
    def __exit__(self, t,v,tr):
        print("time:",time.time()-self.start)

@contextmanager
def cm_timer_2():
    start=time.time()
    yield
    print("time:",time.time()-start)

if __name__=='__main__':
    from time import sleep
    with cm_timer_1(): sleep(1)
    with cm_timer_2(): sleep(1)
