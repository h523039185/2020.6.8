''''
threading创建线程演示
'''
from threading import Thread
from time import sleep
import os
#线程函数
def music():
    for i in range(3):
        sleep(2)
        print(os.getpid(),"黑色的背后是黎明")
#创建线程对象
t = Thread(target=music)
t.start()#启动线程 执行music

for i in range(4):
    sleep(1)
    print((os.getpid(),"播放：你像窝在被子里的舒服"))

t.join()#回收线程资源