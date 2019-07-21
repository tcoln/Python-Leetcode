class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        :note:
            递归的生成
            给G(n)阶格雷码每个元素二进制形式前面添加0；、
            设G(n)集合的倒序（镜像）为R(n)，给R(n)每个元素二进制形式前面添加1；
            G(n+1) = G(n) + R(n)拼接两个集合即可得到下一阶格雷码。
        """
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        ans = [0, 1]
        for i in range(2, n+1):
            l = len(ans)
            reverse = []
            for j in range(l-1, -1, -1):
                reverse.append(ans[j]+pow(2,i-1))
            ans.extend(reverse)
            #print reverse, ans
        return ans
        
