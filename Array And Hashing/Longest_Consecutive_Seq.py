"""
Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

should also be O(n) complexity

"""
nums = [0,3,7,2,5,8,4,6,0,1]
longest = 0
num_set = set(nums)
print(num_set)

for n in num_set:
    print(n-1)
    if (n-1) not in num_set:
        print("Case True")
        length = 1
        while (n+length) in num_set:
            print(n,n+length)
            length += 1
        longest = max(longest, length)
print(longest)