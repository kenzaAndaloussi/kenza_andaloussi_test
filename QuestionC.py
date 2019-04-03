import datetime
import pytz


"""
This class is a node in a double linked list. 
It is defined by a key, data and an expiry date in the form of a datetime object
"""
class Node:
    def __init__(self, key=None, data=None, expiryDate=None, next=None, prev=None):
        self.key = key
        self.data = data
        self.expiryDate = expiryDate
        self.next = next
        self.prev = prev


"""
LRUCache is a class that implements an LRU cache with time expiration by using a double linked list as a queue 
to keep track of the order of least recently used nodes.

This module has some missing functionality, it is not a network aware, it needs also Geo distributed methods.

"""
class LRUCache:

    # Constructor
    def __init__(self, capacity: int, localTimezone, is_dst):
        self.dictionary = dict()
        self.total = 0
        self.capacity = capacity
        self.localTimezone = pytz.timezone(localTimezone)
        self.is_dst = is_dst
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.prev = self.tail
        self.tail.next = self.head

    # This function removes the key value pair and inserts it at the back of the queue as the most recently used item
    def get(self, key: int) -> int:
        if key in self.dictionary:
            node = self.dictionary[key]

            # Remove before adding it back to the queue
            self._removeNode(node)

            # If it's past the expiry date, don't readd it, just return -1
            if (node.expiryDate):
                # always work in UTC to keep expiry dates consistent
                if (pytz.utc.localize(datetime.datetime.utcnow()) >= node.expiryDate):
                    del self.dictionary[node.key]  # remove it from the hashtable
                    return -1

            # add to back of the queue
            self._addNode(node)
            return node.data
        return -1

    def _removeFromCache(self):
        for key in self.dictionary:
            node = self.dictionary[key]

            # if past expiry date, remove it from queue and dictionary
            if (node.expiryDate):
                # Always work in UTC to keep times consistent.
                if (pytz.utc.localize(datetime.datetime.utcnow()) >= node.expiryDate):
                    self._removeNode(node)
                    del self.dictionary[node.key]

    # This function adds a key value pair to the back of the queue as the most recently used item
    def put(self, key: int, value: int, expiryDateString) -> None:
        if key in self.dictionary:
            self._removeNode(self.dictionary[key])

        time = datetime.datetime.strptime(expiryDateString,
                                           "%Y-%m-%d %H:%M:%S")
        localTime = self.localTimezone.localize(time,
                                                is_dst=self.is_dst)  # convert to local timezone with specified daylight savings option
        expiryDate = localTime.astimezone(pytz.utc)  # convert to UTC since all times are kept internally as UTC
        node = Node(key, value, expiryDate)
        self._addNode(node)
        self.dictionary[key] = node

        # if the dictionary is beyond capacity after adding a new node, remove the node at the top of the queue from the queue and dictionary
        if len(self.dictionary) > self.capacity:
            node = self.head.prev
            self._removeNode(node)
            del self.dictionary[node.key]

    # This function removes a node from the linked list
    def _removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # This function adds a node to the linked list
    def _addNode(self, node):
    # Wire the node being inserted
        node.prev = self.tail
        node.next = self.tail.next
        self.tail.next = node
        node.next.prev = node

    # This function moves to the head of the linked list
    def _moveToHead(self, node):
        self._removeNode(node)
        self._addNode(node)
