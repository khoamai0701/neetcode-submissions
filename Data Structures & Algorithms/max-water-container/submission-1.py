class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0
        #[1,8,6,2,5,4,8,3,7]
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            if area > maxArea:
                maxArea = area
                
            
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return maxArea