import heapq

class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        :note:
            贪心算法+最大堆优先队列heapq，O(N^2)时间过不了
            先根据deadline排序，依次选择deadline最小的课程，如果不满足要求，且已选课程中最大时长大于当前课程时长，则替替换掉已选课程中的最大时长课程
        """
        #courses = [[1,2],[2,3]]
        #courses = [[100,2],[32,50]]
        
        N = len(courses)
        curTime = 0
        selectedC = []              # 已选课程的时长t及其deadline元组(-t, d), 
        heapq.heapify(selectedC)    # push的-t是为了用最小堆存相反数构造最大堆
        courses.sort(key=lambda x:x[1])
        #print courses
        for i in range(N):
            c = courses[i]
            if curTime + c[0] <= c[1]:
                curTime += c[0]
                heapq.heappush(selectedC, (-c[0],c[1])) 
            elif len(selectedC) > 0:
                maxD = heapq.heappop(selectedC)
                if c[0] <= -maxD[0]: # change maxD to c
                    curTime += -(-maxD[0]) + c[0]
                    heapq.heappush(selectedC, (-c[0], c[1]))
                else:
                    heapq.heappush(selectedC, maxD)
            #print selectedC, curTime
        return len(selectedC)
