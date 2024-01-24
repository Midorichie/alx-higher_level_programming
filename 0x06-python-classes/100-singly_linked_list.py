#!/usr/bin/python3
"""100-singly_linked_list.py"""

class Node:
    """It's a class node that contains a data and the next node"""
    def __init__(self, data, next_node=None):
        """the spical method initializes the data and the next_node.

        Args:
            data (int): value of the node.
            next_node (Node): the address of the next node.
        """
        self.data = data
        self.next_node = next_node


    @property
    def data(self):
        """The getter and setter fot data.

        Args:
            value (int): the value to be set for data.
        """
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value


    @property
    def next_node(self):
        """Getter and setter for next_node.

        Args:
            value (Node): the value to be set for next_node.
        """
        return self.__next_node


    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class contains the implementation for singly
    linked list."""
    def __init__(self):
        """it initializes the head.

        Args:
            head: the head of the linked list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """inserts is new_node to the list in increasing order.

        Args:
            new_node: is the newly created node
            temp: holds the self.__head.
        """
        new_node = Node(value)


        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        temp = self.__head
        while temp.next_node is not None and temp.next_node.data < value:
            temp = temp.next_node

        new_node.next_node = temp.next_node
        temp.next_node = new_node


    def __str__(self):
        """returns the list in string format.

        Args:
            result: it is a string that holds the singly linked list
            that will be returned.
            temp: it holds the self.__head.
        """
        result = ""
        temp = self.__head
        while temp:
            result += str(temp.data)
            if temp.next_node:
                result += "\n"
            temp = temp.next_node
        return result
