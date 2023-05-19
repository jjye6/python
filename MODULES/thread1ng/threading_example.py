import threading
import time

def print_square(num):
    print("Square: {}".format(num * num))

def print_cube(num):
    print("Cube: {}".format(num * num * num))

# target = function, args = parameter
t1 = threading.Thread(target=print_square, args=(20,))
t2 = threading.Thread(target=print_cube, args=(10,))

start1 = time.time()
t1.start()
end1 = time.time()
t1.join() # waits

start2 = time.time()
t2.start()
end2 = time.time()
t2.join()

print("First thread:", end1 - start1, "seconds")
print("Second thread:", end2 - start2, "seconds")