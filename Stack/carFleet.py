class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = [(p,s) for p,s in zip(position,speed)] #Pairing up the position and speed
        cars.sort(reverse=True) #Sorting and reversing to finding the closest to identify first collision
        stack = [] 
        for p,s in cars:
            stack.append((target-p)/s) #(10-7)/1 = 3 Denoting the time required to reach target
            while len(stack) >= 2 and stack[-1] <= stack [-2]: # Comparing two vals from stack, if lower than top means that collision occurs,
                stack.pop() #Since collision , pop the one with the least time , as the faster car would merge with the slower and speed matches
        return len(stack)
    
target = 10
position = [4,1,0,7]
speed = [2,2,1,1]
obj1 = Solution()
print(obj1.carFleet(target,position,speed))