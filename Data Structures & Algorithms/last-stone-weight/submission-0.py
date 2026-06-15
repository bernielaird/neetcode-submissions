class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -(stones[i])
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            print(stone1)
            print(stone2)
            if stone1 != stone2:
                temp = stone1 - stone2
                print(temp)
                heapq.heappush(stones, temp)
        if stones:
            return -(stones[0])
        return 0