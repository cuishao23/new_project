import threading

# 封装 threading.Thread,重写 run 方法
class mythread(threading.Thread):
    def __init__(self,func,args=()):
        super(mythread, self).__init__()
        self.func=func
        self.args=args
    def run(self):
        self.result=self.func(*self.args)
    def get_result(self):
        try:
            return self.result
        except Exception:
            return None