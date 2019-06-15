class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        :note:
            回溯法中序遍历子集树，本题要点是子集树解空间不能有重复的解。
            所以当添加后面的节点时候必须大于前面的节点，这就使得所有解是升序的。
            例如：candidates = [6,3,2,7]，解分别是6开头的升序解，3开头的升序解，2开头的升序解，7开头的升序解。
            
            编程技巧上，注意list的引用拷贝：b=a，浅拷贝：list(a) or a[:] or copy.copy()，深拷贝：copy.deepcopy()
        """
        #candidates = [6,3,2,7]
        #target = 13
        
        l = len(candidates)
        ans = []
        def InOrder(combi):
            if len(combi) > 0:
                s = sum(combi)
            else:
                s = 0
            if s == target:                
                ans.append(list(combi))
                #print combi, s, ans
                return
            if s < target:
                for i in range(l):
                    num = candidates[i]
                    preNum = 0 if len(combi) < 1 else combi[-1]
                    if num >= preNum:
                        combi.append(num)
                        InOrder(combi)    
                        combi.pop()        
        InOrder([])
        return ans
