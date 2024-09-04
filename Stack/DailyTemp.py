class Solution:
    def dailyTemperaturesOWN(self, temperatures: list[int]) -> list[int]:
        res_days = []
        for i in range(len(temperatures)):
            temp_stack = []
            validated = False
            curr_val = temperatures[i]
            for val in temperatures[i+1:len(temperatures)-1]:
                temp_stack.append(val)
                if val > curr_val:
                    validated = True
                    break
            if validated:
                res_days.append(len(temp_stack))
            if not validated:
                res_days.append(0)
        print(res_days)
    def dailyTemperatures(self,temperatures:list[int]) -> list[int]:
        res_arr = [0] * len(temperatures)
        stack = []
        for ind , temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:  #Stack[-1][0] -> Temperatur of the top value from the stack
                stackTemp , stackInd = stack.pop()
                res_arr[stackInd] = ind - stackInd
            stack.append((temp,ind))
        return res_arr


temperatures1 = [30,38,30,36,35,40,28]
temp2 = [22,21,20]
temp3 = [30,40,50,60]
obj1 = Solution()
obj1.dailyTemperatures(temp3)