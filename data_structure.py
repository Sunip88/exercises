from array import *
import numpy as np
'''
tutorials point -  data structure
'''

def arrays():
    array_1 = array('i', [10, 20, 30, 40, 50])
    for i in array_1:
        print(i)
    print(array_1[1])
    array_1.insert(3, 1)
    print(array_1)
    array_1.remove(10)
    print(array_1.index(30))
    array_1[1] = 110
    print(array_1)


def lists():
    list1 = ['Python', 'Javascript', 1990, 1995]
    list2 = [1, 2, 3, 4, 5, 6, 7, 8]
    print(list1[0], 'list1[0]')
    print(list2[1:5], 'list2[1:5]')
    list1[1] = 'JavaScript'
    print(list1)
    del list2[2]
    print(list2)
    list3 = ['a', 'b']
    list2.append(list3)
    print(list2)
    list2.extend(list3)
    print(list2)
    print(3 in list2)
    print(2 in list2)
    list2.pop()
    print(list2)


def tuples():
    tuple1 = (1, )
    tuple2 = ('Python', 'Javascript', 1990, 1995)
    tuple3 = (1, 2, 3, 4, 5, 6, 7, 8)
    print(tuple2[0])
    print(tuple3[1:5])
    try:
        tuple1[0] = 100
    except TypeError:
        print(tuple1, "tuple is immutable")
    try:
        del tuple1[0]
    except TypeError:
        print(tuple1, "tuple is immutable")
    print(tuple1 + tuple3)


def dictionaries():
    try:
        dict_0 = {[1, 2]: 'a'}
    except TypeError:
        print('key for dictionaries must be a immutable data - strings, numbers, tuple')
    dict_1 = {'Python': 1990, 'JavaScript': 1994}
    print(dict_1['Python'])
    dict_1['JavaScript'] = 1995
    for key, value in dict_1.items():
        print(f"{key} -\t{value}")
    dict_1['newEntry'] = 2019
    print(dict_1)
    del dict_1['newEntry']
    print(dict_1)
    print(dict_1.values())
    print(dict_1.keys())


def matrix():
    array_1 = np.array([[1, 2, 3, 4], [5, 6, 7, 5], [9, 10, 11, 12]])
    print(array_1)
    print(type(array_1))
    print(array_1[0:3, 0:3])
    a = np.array([['Mon', 18, 20, 22, 17], ['Tue', 11, 18, 21, 18],
               ['Wed', 15, 21, 20, 19], ['Thu', 11, 20, 22, 21],
               ['Fri', 18, 17, 23, 22], ['Sat', 12, 22, 20, 18],
               ['Sun', 13, 15, 19, 16]])
    m = np.reshape(a, (7, 5))
    print(m)


def arrays_2d():
    array_2 = [[1, 2, 3, 4], [5, 6, 7], [9, 10, 11, 12]]
    print(array_2)
    array_2.insert(1, ['a', 'b', 'c'])
    print(array_2)


def sets():
    list_1 = ["Mon", "Tue", "Wed", "Fri", "Thu", "Sat", "Sun", "Sun", "Fri", "Mon"]
    week_days = set(list_1)
    print(week_days)
    week_days.add("buu")
    print(week_days)
    week_days.remove("buu")
    print(week_days)


def maps():
    pass


def linked_lists():
    pass


def stacks():
    pass


def queue():
    pass


def dequeue():
    pass

# ...
