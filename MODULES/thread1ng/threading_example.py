import threading
import time

def print_square(num):
    start1 = time.time()
    print("Square: {}".format(num * num))
    time.sleep(2)
    end1 = time.time()
    print("First thread: {0:.2f} seconds".format(end1 - start1))


def print_cube(num):
    start2 = time.time()
    print("Cube: {}".format(num * num * num))
    time.sleep(1)
    end2 = time.time()
    print("Second thread: {0:.2f} seconds".format(end2 - start2))

# target = function, args = parameter
t1 = threading.Thread(target=print_square, args=(20,))
t2 = threading.Thread(target=print_cube, args=(10,))

t1.start()
t1.join() # waits until the thread is finished
t2.start()
t2.join()

