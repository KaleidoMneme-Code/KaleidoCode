import Thread
import time

def Test():
    while not test.Stopped():
        print(1)

test = Thread.Create_Thread(Test)
test.Stop()
print(test.Stopped())
test.Begin()
print(test.Stopped())

# test.start()
# time.sleep(5)
# test.Stop()
