import heapq
def get_key(arr:dict,val):
    for key,value in arr.items():
        if val == value:
            return_list = key
    return return_list


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hash_count = {}
        for i in nums:
            hash_count[i] = nums.count(i)
        print(hash_count)
        counts = [-x for x in hash_count.values()]
        heapq.heapify(counts)
        indxs_of_max = []
        for i in range(k):
            indxs_of_max.append(abs(heapq.heappop(counts)))
        print(indxs_of_max)
        keys = []
        for i in indxs_of_max:
            keys.append(get_key(hash_count,i))
        print(keys)
nums=[1,2]
k=2

obj = Solution()
obj.topKFrequent(nums,k)