class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        self.eval_stack = []
        operators = ["+","-","*","/"]
        self.output = 0
        for i in tokens:
            print("Current Elm {}".format(i))
            if i not in operators: 
                self.eval_stack.append(int(i))
                print(self.eval_stack)
                continue
        
            if i == "+" and len(self.eval_stack) >= 2:
                print("Adding stack elms {}".format(self.eval_stack))
                val1 = self.eval_stack.pop()
                val2 = self.eval_stack.pop()
                sums = val1+val2
                self.eval_stack.append(sums)
                print("After Operation stack is {}".format(self.eval_stack),sums)
            if i == "-" and len(self.eval_stack) >= 2:
                val1 = self.eval_stack.pop()
                val2 = self.eval_stack.pop()
                sub = val2-val1
                self.eval_stack.append(sub)
            if i == "*":
                val1 = self.eval_stack.pop()
                val2 = self.eval_stack.pop()
                self.eval_stack.append(val1*val2)
                print("stack after * is {}".format(self.eval_stack))
            if i == "/":
                val1 = self.eval_stack.pop()
                val2 = self.eval_stack.pop()
                div = int(val2/val1)
                self.eval_stack.append(div)
                print("After {}/{} the stack is {}".format(val2,val1,self.eval_stack))
        return self.eval_stack.pop()


obj1 = Solution()
tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]


print(obj1.evalRPN(tokens))