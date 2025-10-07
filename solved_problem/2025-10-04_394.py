class Solution:
    def decodeString(self, s: str) -> str:
        # create a stack
        stack = []

        for char in s:
            # adding into stack until we see close bracket ']'
            if char != ']':
                stack.append(char)
            
            # when we find the close bracket, we need to decode that substring
            else:
                sub_str = ""
                # we pop the character until we see the open bracket '['
                while stack[-1] != '[':
                    sub_str = stack.pop() + sub_str
                stack.pop() # this pop remove the open bracket

                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
            

                # update stack with number
                sub_str = int(num) * sub_str
                stack.append(sub_str)
                print(sub_str)
        return "".join(stack)



# Time Complexity: O(n)
# Space complexity: O(n)