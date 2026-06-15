class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        res = []
        for i in range(len(points)):
            temp = math.sqrt((points[i][0])**2 + (points[i][1])**2)
            heapq.heappush(pq,(temp, points[i]))
        for _ in range(k):
            dist, point = heapq.heappop(pq)
            res.append(point)
        return res