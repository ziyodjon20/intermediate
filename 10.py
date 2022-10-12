from pickle import TRUE
import threading


import threading
import time

def birinchi():
    print("1-ishga tushdi")
    time.sleep(3)
    print("1-ishni yakunladi")
def ikkinchi():
    print("2-ishga tushdi")
    time.sleep(4)
    print("2-ishni yakunladi")

t1 = threading.Thread(target = birinchi, daemon=TRUE)
t2 = threading.Thread(target = ikkinchi, daemon = True)

t1.start()
t2.start()