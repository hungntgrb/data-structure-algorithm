"""Implementing Hash Tables"""
from pprint import pprint as pr
from random import choice


def hash_fn(text, size):
    """Receive a text, return a hash number string"""
    s = 0
    for char in text:
        s += ord(char)
    return str(s % size)


class Node:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"{self.__class__.__name__}({self.data!r})"


class HashTable:
    def __init__(self, buckets=20):
        self.buckets = dict()
        self.size = buckets

    def insert(self, node):
        key = hash_fn(node.data, self.size)
        if key not in self.buckets:
            self.buckets[key] = [node.data]
        else:
            self.buckets.get(key).append(node.data)

    def remove(self, node):
        key = hash_fn(node.data, self.size)
        if key in self.buckets:
            if node.data in self.buckets[key]:
                self.buckets[key].remove(node.data)
            else:
                raise ValueError("No such data!")
        else:
            raise KeyError("No such key!")


if __name__ == '__main__':
    ht1 = HashTable()
    datas = [''.join([choice('qazwsxcderfvbgtyhnmjuiklop')
                      for _ in range(10)]) for _ in range(20)]
    for data in datas:
        ht1.insert(Node(data))

    pr(ht1.buckets)
