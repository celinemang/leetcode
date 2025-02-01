class TimeMap(object):
    
    
    def __init__(self):
        self.d = collections.defaultdict(list)
        
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.d[key].append((timestamp, value))

        """
        foo:(1, bar),(4, bar2)
        """
    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        values = self.d[key]
        if not values:
            return ''
        left, right = 0 , len(values)-1
        while left<right:
            mid = (left+right+1)/2
            pre_time, value = values[mid]
            if pre_time > timestamp:
                right = mid -1
            else:
                left = mid

        return values[left][1] if values[left][0]<=timestamp else ''
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)