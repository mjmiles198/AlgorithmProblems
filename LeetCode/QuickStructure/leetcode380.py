from random import choice
class RandomizedSet(object):

    def __init__(self):
        self.dict={}
        self.list=[]

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            return False
        self.dict[val]=len(self.list)
        self.list.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            return False
        last_element,idx=self.list[-1],self.dict[val]
        self.list[idx],self.dict[last_element]=last_element,idx
        self.list.pop()
        del self.dict[val]
        return True
        

    def getRandom(self):
        """
        :rtype: int
        """
        return choice(self.list)
