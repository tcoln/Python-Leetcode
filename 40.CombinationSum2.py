class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        :note:
            跟上一题类似，子集解是升序解，同时注意list的浅复制；
	    另外每次循环下一层节点的时候，remove已经选用过的节点，例如节点1，同时用set去重重复的节点，例如节点2
        """
        #candidates = [2,5,2,1,2]
        #target = 5
        
        l = len(candidates)
        ans = []
        def InOrder(combi):
            s = 0 if len(combi) < 1 else sum(combi)
            if s == target:
                ans.append(list(combi))
                #print combi, s
                return
            if s < target:
                can = list(candidates)
                for c in combi:
                    can.remove(c)       # remove已选节点保证不二次使用同一个节点
                for num in set(can):    # set保证同一层没有重复的节点
                    preNum = 0 if len(combi) < 1 else combi[-1]
                    if num >= preNum:
                        combi.append(num)
                        InOrder(combi)
                        combi.pop()
                    
        InOrder([])
        return ans
