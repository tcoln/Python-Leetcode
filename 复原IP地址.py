class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        :note:
            #V1
            回溯法遍历子集树，InOrder(s=s, depth=0)，分布切割第1、第1-2、第1-3个字符来生成子树
            当depth==4的时候，判断最后一层s是不是在0-255之间            
            #V2
            回溯法依次取1、2、3个字符来生成下一个byte，当depth==4且ip长度为len(s)+3时候输出结果
            注意byte<=255，且第一个字母为0的时候i<2
        """
        if not s or len(s) == 0 or len(s) > 15:
            return []
        #s = "010010"
        ans = []
        def backTrack(s, start, depth, ip):
            if (depth == 4 and len(ip) == len(s)+3):
                ans.append(ip)
            for i in range(1, 4):
                if start + i <= len(s):
                    byte = s[start:start+i]
                    if (byte[0]=='0' and i < 2) or byte[0] != '0':
                        if byte and int(byte) <= 255:
                            if ip:
                                newIP = ip + '.' + byte
                            else:
                                newIP = byte
                            backTrack(s, start+i, depth+1, newIP)
                        
        backTrack(s, 0, 0, '')
        return ans
