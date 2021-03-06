class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        res = []
        n = max(target)
        for i in range(1,n+1):
            res.append("Push")
            if i not in target:
                res.append("Pop")
        
        return res
