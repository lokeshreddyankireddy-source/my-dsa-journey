class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        stack = []
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                area = height * width
                max_area = max(area , max_area)
            stack.append(i)
        while stack:
            height = heights[stack.pop()]
            if stack:
                width = n - stack[-1] - 1
            else:
                width = n
            area = height * width
            max_area = max(area , max_area)
        return max_area