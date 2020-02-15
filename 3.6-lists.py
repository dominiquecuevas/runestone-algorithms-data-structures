def test1():
    """
    concat is O(k) of the size of the list being added.
    with the slowest ms
    ~ 1.110386264999761 milliseconds
    """
    l = []
    for i in range(1000):
        l = l +[i]

def test2():
    """
    append is O(n) and the 2nd slowest tested 0.19723322299978463 milliseconds
    """
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    """
    list comprehension test is faster than a for loop with append.
    0.09918235900113359 milliseconds
    """
    l = [i for i in range(1000)]

def test4():
    """
    list constructor test with range is the fastest
    """
    l = list(range(1000))

if __name__ == "__main__":
    from timeit import Timer

    t1 = Timer("test1()", "from __main__ import test1")
    print("concat ",t1.timeit(number=1000), "milliseconds")
    t2 = Timer("test2()", "from __main__ import test2")
    print("append ",t2.timeit(number=1000), "milliseconds")
    t3 = Timer("test3()", "from __main__ import test3")
    print("comprehension ",t3.timeit(number=1000), "milliseconds")
    t4 = Timer("test4()", "from __main__ import test4")
    print("list range ",t4.timeit(number=1000), "milliseconds")