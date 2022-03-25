from typing import List
import heapq 

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[0])
        q = []
        for room in intervals:
            if q and q[0] <= room[0]:
                heapq.heappop(q)
            heapq.heappush(q,  room[1])
        return len(q)
            
if __name__=='__main__':
    Solution().minMeetingRooms([[7,10],[2,4]])