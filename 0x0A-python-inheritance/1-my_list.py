"""
A module containing a class that inherits from list
"""


class MyList(list):
    """
    A class that inherits from list
    """
    def print_sorted(self):
        """
        A method that prints a sorted list
        """
        lst = self.copy()
        lst.sort()
        print(lst)
