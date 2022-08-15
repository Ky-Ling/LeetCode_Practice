import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Min heap of size k
        # Turn the input to a heap with O(n) time
        # Pop out one element: O((n - k)logn) ~ O(nlogn)
        # Add one element: O(logn)
        self.minHeap, self.k = nums, k

        # Transform list nums into a heap, in-place, in linear time O(n).
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > k:

            # Pop and return the smallest item
            heapq.heappop(self.minHeap)

    
    def add(self, val: int) -> int:

        # Push the value item onto the heap
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]