class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1

        cur_left_i = i
        cur_right_j = j
        cur_left = height[cur_left_i]
        cur_right = height[cur_right_j]
        cur_area = min(cur_left, cur_right) * (cur_right_j-cur_left_i)

        while (i<cur_right_j) or (j>cur_left_i):
            print("cur_left_i:", cur_left_i)
            print("cur_right_j:", cur_right_j)
            print("cur_left:", cur_left)
            print("cur_right:", cur_right)
            print("cur_area:", cur_area)
            print("i:", i)
            print("j:", j)
            print("\n")

            new_left = height[i]
            new_right = height[j]

            if new_left<=cur_left:
                pass
            else:
                new_area = min(new_left, cur_right) * (cur_right_j-i)
                print("new_area:", new_area)
                if cur_area<new_area:
                    cur_left_i = i
                    cur_left = new_left
                    cur_area = new_area
                else:
                    pass


            if new_right<=cur_right:
                pass
            else:
                new_area = min(cur_left, new_right) * (j-cur_left_i)
                print("new_area:", new_area)
                if cur_area<new_area:
                    cur_right_j = j
                    cur_right = new_right
                    cur_area = new_area
                else:
                    pass

            if i<cur_right_j:
                i+=1
            if j>cur_left_i:
                j-=1

        


        return cur_area


