#!/usr/bin/python3

class MyList(list):
    """
    MyList class that inherits from list.

    Public instance method:
    - print_sorted(self): prints the list, but sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
