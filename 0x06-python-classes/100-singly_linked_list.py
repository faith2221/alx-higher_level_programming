#!/usr/bin/python3
"""Defines a node of a singly linked list."""


class Node:
    def __init__(self, data, nextNode=None):
        """Initializes a new node."""
        self.data = data
        self.next_node = nextNode

    @property
    def data(self):
        """Retrieves and returns the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data and raises TypeError if needed."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def nextNode(self):
        """Retrieves and returns the next node in the linked list."""
        return self.__nextNode

    @nextNode.setter
    def nextNode(self, value):
        """Sets the next node and raises TypeError if needed."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("nextNode must be a Node object")
        self.__nextNode = value


class SinglyLinkedList:
    """Defines a linked list."""

    def __init__(self):
        """Initializes an empty singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list."""
        newNode = Node(value)
        if self.head is None or self.head.data >= value:
            newNode.nextNode = self.head
            self.head = newNode

        else:
            curr = self.head
            while curr.nextNode is not None and curr.nextNode.data < value:
                curr = curr.nextNode
            newNode.nextNode = curr.nextNode
            curr.nextNode = newNode

    def __str__(self):
        """Prints the entire list in stdout, one node number by line."""
        res = []
        curr = self.head
        while curr:
            res.append(str(curr.data))
            curr = curr.nextNode
        return "\n".join(res)
