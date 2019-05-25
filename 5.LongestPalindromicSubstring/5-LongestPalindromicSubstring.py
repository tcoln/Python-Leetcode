class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        maxLens = [] # max palin len with i as center or as left center
        maxIndexLen = (0, 0)
        for i in range(n):
            curLen = 1
            for j in range(min(i, n-i-1)):
                if s[i-j-1] == s[i+j+1]:
                    curLen += 2
                else:
                    break
            maxLens.append(curLen)
            
            curLen = 0
            for j in range(min(i+1, n-i-1)):
                if s[i-j] == s[i+j+1]:
                    curLen += 2
                else:
                    break
            maxLens[i] = curLen if curLen > maxLens[i] else maxLens[i]
        
            maxIndexLen = (i, maxLens[i]) if maxLens[i] > maxIndexLen[1] else maxIndexLen
        print maxLens, maxIndexLen
        if maxIndexLen[1] % 2 == 0:
            return s[maxIndexLen[0]-maxIndexLen[1]/2+1 : maxIndexLen[0]+maxIndexLen[1]/2+1]
        else:
            return s[maxIndexLen[0]-maxIndexLen[1]/2 : maxIndexLen[0]+maxIndexLen[1]/2+1]
