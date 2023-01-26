# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks(high cpu usage)
#                   multithreading  = better for i/o bound tasks(waiting around)

from multiprocessing import Process, cpu_count

def counter(num):
    count = 0
    while count < num:
        count += 1


def main():

    print(cpu_count())

    a = Process(target=counter, args=(125000000,))                 # assigning a core to run a particular function
    b = Process(target=counter, args=(125000000,))                 # assigning a second core
    c = Process(target=counter, args=(125000000,))
    d = Process(target=counter, args=(125000000,))


    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    print("Finished")


if __name__ == '__main__':
    main()
