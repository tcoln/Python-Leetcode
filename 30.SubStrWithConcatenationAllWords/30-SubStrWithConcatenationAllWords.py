ass Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        :note:
            —— 关键信息word长度都一样，用字典存储每个word可使用个数（存量），提升性能
            1、循环遍历字符串s每个位置i，判断n个word是否有存量，没有结束循环，有的话存量-1
            注意：每次循环的时候字典要恢复原始存量
        """
        #s = "wordgoodgoodgoodbestword"
        #words = ["word","good","best","word"]

        ls = len(s)
        wNum = len(words)
        lws = 0 # all words len
        lw = 0  # singel word len
        for w in words:
            lw = len(w)
            lws += lw            
        if lws == 0 or lws > ls:
            return []        
        
        ans = []
        for i in range(0, ls-lws+1):
            isMatch = True
            wdict = {}
            for w in words:
                n = wdict.get(w, 0)
                wdict[w] = 1 if n == 0 else n+1
            #print wdict
            for j in range(wNum):
                key =  s[i+j*lw : i+(j+1)*lw]
                n = wdict.get(key, 0)
                if n > 0:
                    wdict[key] = n-1
                else:
                    isMatch = False
                    break
            if isMatch:
                ans.append(i)
        return ans
