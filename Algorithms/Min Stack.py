class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        _min = x
        if len(self.stack) > 0 and self.stack[-1]['min'] <  _min:
            _min = self.stack[-1]['min']       
            
        self.stack.append({'n':x,'min':_min})
                
        
            
        
    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]['n']

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1]['min']


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()lize your data structure here.
      
