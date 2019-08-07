from collections import OrderedDict
'''
note:
    最重要的是使用有序字典这个数据结构，from collections import OrderedDict
    OrderedDict是一个FIFO的有序字典，左边older，右边new
    od.get(key, -1)
    od.popitem(last=False)
    self.move_to_end(key)
'''
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.lrucache = OrderedDict()
        self.maxcap = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.lrucache:
            self.move_to_end(key)
        return self.lrucache.get(key, -1)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.lrucache[key] = value
        self.move_to_end(key)
        if len(self.lrucache) > self.maxcap:
            self.lrucache.popitem(last=False)

    def move_to_end(self, key):
        val = self.lrucache[key]
        del self.lrucache[key]
        self.lrucache[key] = val

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
