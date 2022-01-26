from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        q = []
        heapq.heappush(q, intervals[0][1])
        
        for interval in intervals[1:]:
            if q[0]<=interval[1]:
                heapq.heappop(q)
            heapq.heappush(q, interval[1])
        
        return len(q)
        
if __name__=='__main__':
    Solution().minMeetingRooms([[0,30],[5,10],[15,20]])