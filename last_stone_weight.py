import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        [heapq.heappush(heap, -s) for s in stones]

        while len(heap) > 1:
            stone_y = -heapq.heappop(heap)
            stone_x = -heapq.heappop(heap)

            stone_remain = stone_y - stone_x
            if stone_remain:
                heapq.heappush(heap, -stone_remain)
    
        return -heap[0] if heap else 0
