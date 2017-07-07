
class worker:

    def __init__(self,b = 0):
        self.a = b

    def do_work(self):
        print self.a

class child_worker_num1(worker):

    def __init__(self,b):
        worker.__init__(self,b)

    def do_all_work(self):
        self.do_work()




class child_worker_num2:

    C = worker()
    a = C.a
    def __init__(self,b):
        self.C = worker(b)

    def do_all_work(self):
        self.C.do_work()

# A1 = worker()
# A1.do_work()
print ("parent")
A = worker(5)
A.do_work()
print ("child with inheritance")
B = child_worker_num1(6)
B.do_work()
B.do_all_work()
print "val=", B.a
print ("child with delegation")
CC = child_worker_num2(7)
print CC.a
CC.do_all_work()

