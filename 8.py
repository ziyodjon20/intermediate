import threading as thr

event = thr.Event()
def jarayon():
    print("Flaskni o'rnatish boshlansinmi?")
    event.wait()
    print("Flaskni o'rnatish boshlandi! ")

t1 = thr.Thread(target=jarayon)
t1.start()

sorov = input("Flaskni o'rnatish boshlansinmi? (ha)")

if sorov == "ha":
    event.set()
