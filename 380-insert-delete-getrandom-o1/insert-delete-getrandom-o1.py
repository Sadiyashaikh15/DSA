import random

class RandomizedSet(object):

    def __init__(self):
        self.arr = []       # list to store values
        self.pos = {}       # hashmap: value -> index in arr

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            return False
        self.pos[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            return False

        idx = self.pos[val]
        last_val = self.arr[-1]

        # Move last element into idx (works even when last_val == val)
        self.arr[idx] = last_val
        self.pos[last_val] = idx

        # Pop last and remove mapping for val
        self.arr.pop()
        del self.pos[val]

        # IMPORTANT: return True to indicate success
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.arr)
