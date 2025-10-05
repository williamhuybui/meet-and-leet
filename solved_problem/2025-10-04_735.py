class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Create stack to keep track
        stack = []

        # Loop through each num in asteriod
        for num in asteroids:
            # Colision acan only happen when:
            # - the stack is not empty
            # - num in stack is moving left (num<0)
            # - last num in stack is moving right (stack[-1]>0)
            while stack and num < 0 and stack[-1] > 0:
                # example stack[-1] = 5, num = -3, track = 2

                # if sum is negative, which mean the right move(in stack) is smaller -> remove it
                if stack[-1] + num < 0:
                    stack.pop()
                # if sum is positive, which mean the the current asteroid (num) is smaller, so num = 0 (just ignore it)
                elif stack[-1] + num > 0:
                    num = 0
                # if sum == 0, both are equal. Remove right one (pop), set num = 0
                else:
                    stack.pop()
                    num = 0
            
            # if num is still non zero -> push to stack
            if num:
                stack.append(num)
        return stack        


# Time complexity: O(n)
# Space complexity: O(n)
# stack []
# 5 -> add[5]
# 10 -> add [5,10]
# -5 -> truck = 10 + (-5) = 5 -> num = 0 -> current asteroid destroyed
