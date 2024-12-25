class Solution:
    def maxArea(self, height: List[int]) -> int:

        ## Two pointer
        i = 0
        j = len(height)-1
        max_area = 0
        # max_i = i
        # max_j = j
        while(i<j):
            # print("i:", i)
            # print("j:", j)
            # print("max_i:", max_i)
            # print("max_j:", max_j)
            # print("max_area:", max_area)


            cur_left = height[i]
            cur_right = height[j]
            cur_area = (j-i)*min(cur_left, cur_right)
            if cur_area>max_area:
                max_area = cur_area
                # max_i = i
                # max_j = j

            # print("cur_left:", cur_left)
            # print("cur_right:", cur_right)
            # print("cur_area:", cur_area)

            if height[i]<height[j]:
                i+=1
            else:
                j-=1

            # print("next_i:",i)
            # print("next_j:",j)
            # print("\n")


        return max_area


