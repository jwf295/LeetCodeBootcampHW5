class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        heap = []
        for key in hashmap.keys():
            if len(heap) == k:
                heappushpop(heap, (hashmap[key], key))
            else:
                heappush(heap, (hashmap[key], key))
        result = []
        while k > 0:
            result.append(heappop(heap)[1])
            k -=1
        return result
