class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1

        max_volume = 0
        while i<j:
            cur_volume = (j-i) * min(height[i], height[j])

            if cur_volume>max_volume:
                max_volume = cur_volume
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
                
        return max_volume