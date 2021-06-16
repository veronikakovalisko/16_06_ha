'''Task 1
Extend UnorderedList
Implement append, index, pop, insert methods for UnorderedList.
Also implement a slice method, which will take two parameters `start` and `stop`,
and return a copy of the list starting at the position and going up to but not including the stop position.'''
from typing import Any, List
class UnorderedList:
    def __init__(self):
        self.__list = []
    def append(self, data: Any)-> bool:
        self.__list.append(data)
        return True
    def index(self, elem):
        if elem in self.__list:
            return self.__list.index(elem)
    def pop(self) -> Any:
        if self.__list:
            return self.__list.pop()
        raise IndexError
    def insert(self, data, indx: int):
        return self.__list.insert(data, indx)
    def slice(self, start: int, stop: int)-> List:
        return self.__list[start-1:stop-1]

l = UnorderedList()
l.append(4)
l.append(5)
l.append(6)
print(l.slice(1, 2))
'''Task 2
Implement a stack using a singly linked list.'''
from typing import Any


class Stack:
    def __init__(self, size=10):
        self.__stack = []
        self.size = size

    def empty(self) -> bool:
        return not bool(self.__stack)

    def peek(self) -> Any:
        if not self.empty:
            return self.__stack[-1]

    def pop(self) -> Any:
        if not self.empty:
            return self.__stack.pop()
        raise IndexError

    def push(self, elem: Any) -> bool:
        if len(self.__stack) == self.size:
            return False
        self.__stack.append(elem)
        return True

    def search_and_extract(self, data: Any):
        stack2 = self.__class__(self.size)
        while not self.empty:
            x = self.pop()
            if x == data:
                break
            else:
                stack2.push()
        while not stack2.empty:
            y = stack2.pop()
            self.push(y)
        return x == data

    def __repr__(self):
        return str(self.__stack)

'''Task 3
Implement a queue using a singly linked list.'''

class Queue:
    def __init__(self):
        self.__queue=[]
    def enqueue(self, data: Any)-> Any:
        return self.__queue.append(data)
    def dequeue(self):
        return self.__queue.pop(len(self.__queue)-1)
    def is_empty(self)-> bool:
        return not bool(self.__queue)
    def size(self)-> int:
        return len(self.__queue)

q = Queue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(4)
print(q.is_empty())
print(q.size())
q.dequeue()
print(q.size())


