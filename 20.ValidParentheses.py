class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        :note:
            用list实现栈，但是list没有top方法，可以用pop和append代替
            合法的字符串在栈里面最终都会被消掉，否则为非法字符串
        """
        #s = "){"

        stack = ['t']
        stackI = 0
        l = len(s)
        ans = True
        for i in range(l):
            top = stack.pop()
            if top == 't':
                stack.append(top)
                stack.append(s[i])
            elif top in '({[':
                if self.match(top, s[i]):
                    continue
                else:
                    stack.append(top)
                    stack.append(s[i])
            else:
                ans = False
                break
            #print stack
        if len(stack) > 1:
            ans = False
        return ans
                
    def match(self, a, b):
        if (a=='(' and b==')') or (a=='[' and b==']') or (a=='{' and b=='}'):
            return True
        else:
            return False
