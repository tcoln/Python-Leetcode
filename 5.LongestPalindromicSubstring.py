class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
	:note:
	回文长度有奇数个也有偶数个，奇数个有对称的中心点，偶数个有两个对称中心点，分别统计

	第一轮，分别统计以每个字符为中心点的最长回文长度，这类回文长度都是奇数
	第二轮，分别统计以每个字符为偶数回文长度的左边中心点的最长回文长度，这类回文长度都是偶数
	第二轮统计的时候跟第一轮比较，取更长的那个
	第三轮，遍历寻找最长的回文长度，根据长度及其的奇偶性截取最长回文
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
