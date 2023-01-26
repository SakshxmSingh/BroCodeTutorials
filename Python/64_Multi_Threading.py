# thread = a flow of execution. Like a separated order of instructions
#          However each thread takes a turn running to achieve concurrency
#          GIL = (global interpreter lock),
#          allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of its time waiting for internal events (CPU intensive)
#             Use multiprocessing
#
# io bound  = program/task spends most of its time waiting for external events (user input, web scraping)
#             use multithreading

import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drank coffee")

def study():
    time.sleep(5)
    print("You finished studying")

def leave():
    time.sleep(6)
    print("You left the home")


x = threading.Thread(target=eat_breakfast, args=())       # creating a different thread for target function
x.start()                                                 # activating the thread
y = threading.Thread(target=drink_coffee, args=())
y.start()
z = threading.Thread(target=study, args=())
z.start()
w = threading.Thread(target=leave, args=())
w.start()
#                                       # for running different functions concurrently, for e.g. time in these functions


#eat_breakfast()
#drink_coffee()
#study()

print(threading.active_count())                     # displays the no of threads working in the background
print(threading.enumerate())                        # lists all the threads running
print(time.process_time())                          # tells the time taken to complete the calling thread


x.join()                                            # for syncing the main thread to another thread, in this case: x
y.join()
z.join()
w.join()

print(threading.active_count())
print(threading.enumerate())
print(time.process_time())
