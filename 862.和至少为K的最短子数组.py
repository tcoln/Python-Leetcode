from collections import deque
if True:
        A = [-34,37,51,3,-12,-50,51,100,-47,99,34,14,-13,89,31,-14,-44,23,-38,6]
        K = 151
	print A; 
	print K
        ans = float('inf')
        l = len(A)
        preS = [0] * (l+1)
        for i in range(1, l+1): preS[i] = preS[i-1] + A[i-1]
        print preS
        deq = deque()
	for j in range(2, l+1):
		while(deq and preS[j] < preS[deq[-1]]): deq.pop()
		while(deq and preS[j] - preS[deq[0]] >= K):
			i = deq.popleft()
			ans = min(ans, j-i)
		deq.append(j)
	if ans == float('inf'): ans = -1
        print ans
