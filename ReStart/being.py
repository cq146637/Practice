import multiprocessing


def aaa(child):
        child.send("hello!")




if __name__ == '__main__':
    parent,child = multiprocessing.Pipe()
    a = multiprocessing.Process(target=aaa,args=(child,))
    a.start()
    a.join()
    print(parent.recv())