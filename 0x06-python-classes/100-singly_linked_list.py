#!/usr/bin/python3
"""
Module for a Node of a singly linked list
"""


class Node:
    """
    Defining a node for a singly linked list
    """

    def __init__(self, data, next_node=None):
        """
        Initializing an instance of the Node class

        Args:
            data (int): data present in a node
            next_node (instance): Defaults to None

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieving the data value

        Returns:
            int: data present in node

        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setting the data value

        Args:
            value (int): the value set to data

        Raises:
            TypeError: if data is not an integer

        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Retrieving the next_node value

        Returns:
            instance: the next node

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setting the next_node value

        Args:
            value (instance): an instance of the Node class

        Raises:
            TypeError: if thr next_node is not a node object

        """
        if isinstance(value, Node) is False and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


"""
Method for a singly linked list
"""


class SinglyLinkedList:
    """
    Defining a singly linked list
    """

    def __init__(self):
        """
        Initializing an instance of the Singly Linked List
        """

        self.head = []

    def sorted_insert(self, value):
        """
        Sorting the Singly linked list in ascending order

        Args:
            value (int): value to be added to the list

        """
        obj = Node(value)
        self.head.append(obj.data)
        self.head.sort()

    def __str__(self):
        """
        Implementing the print() function into the Singly Linked List class

        Returns:
            str: the sorted linked list
        """
        stdout = ""
        count = 0
        for num in self.head:
            if count == len(self.head) - 1:
                stdout += str(num)
            else:
                stdout += str(num)
                stdout += '\n'
            count += 1
        return stdout
