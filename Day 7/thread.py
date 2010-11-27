from threading import Thread
import time
#class abc(Thread):
#    def run(self): 

#A = abc()
#A.start()
#B = abc()
#B.start()

class series(Thread):
    def __init__(self,num1,num2):
        Thread.__init__(self)
        self.num1 = num1
        self.num2 = num2
    
    def run(self):
        for i in range(self.num1,self.num2):
            print i,"*"
            time.sleep(1)

A = series(2,15)
B = series(5,8)

A.start()
B.start()
print "hello"
A.join()
print "process A is finished"