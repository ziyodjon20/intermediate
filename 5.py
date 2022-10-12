import threading
def func():
    for x in range(10):
        print("Assalomu ")
def func2():
    for x in range(10):
       print("alaykum ")
def func3():
    for x in range(10):
        print("hammaga")
# func()
# func2()
t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func2)
t3 = threading.Thread(target=func3)


t1.start()
t2.start()
t3.start()