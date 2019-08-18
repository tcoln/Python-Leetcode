class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        :note:
            利用栈压入每个单词
        """
        if not s:
            return ''
        #s = "  hello world!  "
        l = len(s)
        word = ''
        stack = []
        for c in s:
            if c == ' ':
                if word:
                    stack.append(word)
                    word = ''
                    continue
            else:
                word += c
        if word:
            stack.append(word)
        ans = ''
        while stack:
            ans += stack.pop() + ' '
        return ans[:-1]
