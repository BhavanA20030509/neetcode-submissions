class Solution:
    def evalRPN(self, tokens):
        stack=[]
        for ch in tokens:
            if ch =='+':
                num2=stack.pop()
                num1=stack.pop()
                stack.append(num1+num2)
            elif ch =='-':
                num2=stack.pop()
                num1=stack.pop()
                stack.append(num1-num2)
            elif ch=='*':
                num2=stack.pop()
                num1=stack.pop()
                stack.append(num1*num2)
            elif ch=='/':
                num2=stack.pop()
                num1=stack.pop()
                stack.append(int(num1/num2))
            else:
                stack.append(int(ch))
        return stack[-1]
