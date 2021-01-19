"""Threading practice
"""
import threading
import time

def foo(number: int):
    # create lock instance
    # 針對 multi thread，每個 thread 在同時進行時，如果針對某些不能同時操作的事情時 e.g database寫入、寫入同一個檔案
    # 則需要加入 lock來確保每次只有一個 thread 在操作，而不是多個 thread同時操作
    lock = threading.Lock()
    # acquire lock control
    lock.acquire()
    # logic
    for i in range(number): print(i)
    print('finished foo() logic')
    # release lock control
    lock.release()

"""
regular 
"""
sample_thread = threading.Thread(target=foo, args=10)
# run threading
sample_thread.start()
# wait thread until end
# 主要針對某些需要等待 thread 跑完才能執行的邏輯
sample_thread.join()
# after thread finished, continous run later logic
print('Done.')


""" 
multi threading 
"""
threads = []
for i in range(5):
    threads.append(threading.Thread(target=foo, args=10))
    threads[i].start()

for i in range(5):
    threads[i].join()

# after thread finished, continous run later logic
print('Done.')


"""
defined custom Thread class
"""
class Worker(threading.Thread):
    def __init__(self, tag: int):
        threading.Thread.__init__(self)
        self.tag = tag

    def run(self):
        print(f"Worker # {self.tag} is running.")
        foo(self.tag)
        time.sleep(1)

for i in range(3):
    worker = Worker(i)
    worker.start()
    worker.join()

# after thread finished, continous run later logic
print('Done.')
