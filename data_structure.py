from array import *
import numpy as np
import collections
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
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}
    print(set1 | set2)
    print(set1 & set2)
    print(set1 - set2)
    print(set1 >= set2)


def maps():
    dict1 = {'day1': 'Mon', 'day2': 'Tue'}
    dict2 = {'day3': 'Wed', 'day1': 'Thu'}
    res = collections.ChainMap(dict1, dict2)
    print(res)
    print(f"Keys = {list(res.keys())}")
    print(f"Values = {list(res.values())}")
    print('elements:')
    for key, val in res.items():
        print('\t{} = {}'.format(key, val))
    print('day3 in res: {}'.format(('day1' in res)))
    print('day4 in res: {}'.format(('day4' in res)))

    res1 = collections.ChainMap(dict1, dict2)
    res2 = collections.ChainMap(dict2, dict1)
    print(res1, res2)
    dict2['day4'] = 'Fri'
    print(res1)


def linked_lists():
    class LinkedList:

        def __init__(self):
            self._first = None
            self._last = None

        def add(self, value, last=True):
            new = Node(value)
            if last:
                if self._first is None:
                    self._first = new
                else:
                    self._last.next = new
                self._last = new
            else:
                temp = None
                if self._last is None:
                    self._last = new
                else:
                    temp = self._first
                self._first = new
                self._first.next = temp

        def first(self):
            return self._first.value

        def last(self):
            return self._last.value

        def get(self, index=0):
            current_index = 0
            current_node = self._first
            while current_index != index:
                if current_node.next is None:
                    raise IndexError()
                current_node = current_node.next
                current_index += 1
            return current_node.value

        def remove(self, last=True):
            if self._first == self._last:
                self._last = self._first = None
            if not last:
                self._first = self._first.next
            else:
                current_node = self._first
                while current_node.next != self._last:
                    current_node = current_node.next
                current_node.next = None
                self._last = current_node

        def __iter__(self):
            current_node = self._first
            while current_node:
                yield current_node.value
                current_node = current_node.next

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    l = LinkedList()
    l.add(1, False)
    l.add(2)
    l.add(3)
    print(l.first())  # 1
    print(l.get())  # 1
    print(l.get(1))  # 2
    print(l.last())  # 3
    print(list(l))
    l.remove()  # -> 1, 2
    print(list(l))
    l.remove(False)  # -> 2
    print(list(l))
    l.add(1)
    print(list(l))
    l.add(3, False)
    print(list(l))


def stacks():
    class Stack:

        def __init__(self):
            self.__stack = []

        def add(self, data_value):
            if data_value not in self.stack:
                self.stack.append(data_value)
                return True
            else:
                return False

        def remove(self):
            if len(self.stack) <= 0:
                return ("No element in stack")
            else:
                return self.stack.pop()

        @property
        def stack(self):
            return self.__stack

    stack_try = Stack()
    stack_try.add("1")
    stack_try.add("2")
    stack_try.add("2")
    print(stack_try.stack)
    print(stack_try.remove())
    print(stack_try.stack)

stacks()


def queue():
    pass


def dequeue():
    pass

# ...
