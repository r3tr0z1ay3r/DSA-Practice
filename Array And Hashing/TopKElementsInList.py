class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            count[i] = nums.count(i)
        print(count)
        for val,count in count.items():
            print(val,count)
            freq[count].append(val)
        print(freq)
        result_arr = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                result_arr.append(n)
                if len(result_arr) == k:
                    return result_arr