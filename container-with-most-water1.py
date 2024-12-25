class Solution:
    def maxArea(self, height: List[int]) -> int:
        pos_list = [(k,i) for i,k in enumerate(height)]
        pos_list = sorted(pos_list, key=lambda x:-x[0]*len(height)+x[1])

        # print("pos_list:", pos_list)

        i=0
        j=1
        cnt = 1
        if pos_list[i][1]<pos_list[j][1]:
            cur_left_index = pos_list[i][1]
            cur_right_index = pos_list[j][1]
        else:
            cur_left_index = pos_list[j][1]
            cur_right_index = pos_list[i][1]
        cur_left = pos_list[i][0]
        cur_right = pos_list[j][0]

        gap = cur_right_index - cur_left_index
        cur_min = min(cur_left, cur_right)
        cur_area = cur_min * gap
        
        left_comparation_stack = []
        right_comparation_stack = []

        while cnt<len(pos_list)-1:
            cnt+=1
            next_val, next_index = pos_list[cnt]

            # print("cnt:", cnt)
            # print("cur_left:", cur_left)
            # print("cur_right:", cur_right)
            # print("cur_left_index:", cur_left_index)
            # print("cur_right_index:", cur_right_index)
            # print("gap:", gap)
            # print("cur_min:", cur_min)
            # print("cur_area:", cur_area)
            # print("next_val:", next_val)
            # print("next_index:", next_index)
            # print("left_comparation_stack:", left_comparation_stack)
            # print("right_comparation_stack:", right_comparation_stack)

        
            if next_val<=cur_min and ((next_index > cur_left_index) and (next_index < cur_right_index)):
                pass
            elif next_val<=cur_min and next_index < cur_left_index:
                new_left_index = next_index
                new_right_index = cur_right_index
                new_left = next_val
                new_right = cur_right
                new_gap = new_right_index-new_left_index
                new_min = min(new_left, new_right)
                new_area = new_gap * new_min

                if new_area>=cur_area:
                    cur_left = new_left
                    cur_right = new_right
                    cur_left_index = new_left_index
                    cur_right_index = new_right_index
                    gap = new_gap
                    cur_min = new_min
                    cur_area = new_area

                
                tmp_val,tmp_index = next_val,next_index
                succeed = False
                max_i = 0
                for i,(stack_val,stack_index) in enumerate(right_comparation_stack):
                    new_right_index = stack_index
                    new_left = next_val
                    new_right = stack_val
                    new_gap = new_right_index-new_left_index
                    new_min = min(new_left, new_right)
                    new_area = new_gap * new_min
                    if new_area>=cur_area:
                        succeed=True
                        cur_left = new_left
                        cur_right = new_right
                        cur_left_index = new_left_index
                        cur_right_index = new_right_index
                        gap = new_gap
                        cur_min = new_min
                        cur_area = new_area
                        max_i = i

                right_comparation_stack = right_comparation_stack[max_i:]

                if not succeed:
                    left_comparation_stack.append((tmp_val,tmp_index))
                                    


                # print("new_area:", new_area)

            elif next_val<=cur_min and next_index > cur_right_index:
                new_left_index = cur_left_index
                new_right_index = next_index
                new_left = cur_left
                new_right = next_val
                new_gap = new_right_index-new_left_index
                new_min = min(new_left, new_right)
                new_area = new_gap * new_min

                if new_area>=cur_area:
                    cur_left = new_left
                    cur_right = new_right
                    cur_left_index = new_left_index
                    cur_right_index = new_right_index
                    gap = new_gap
                    cur_min = new_min
                    cur_area = new_area
                
          
                tmp_val,tmp_index = next_val,next_index
                succeed = False
                max_i = 0
                for i,(stack_val,stack_index) in enumerate(left_comparation_stack):
                    new_left_index = stack_index
                    new_left = stack_val
                    new_right = next_val
                    new_gap = new_right_index-new_left_index
                    new_min = min(new_left, new_right)
                    new_area = new_gap * new_min
                    if new_area>=cur_area:
                        succeed=True
                        cur_left = new_left
                        cur_right = new_right
                        cur_left_index = new_left_index
                        cur_right_index = new_right_index
                        gap = new_gap
                        cur_min = new_min
                        cur_area = new_area
                        max_i = i
                
                left_comparation_stack = left_comparation_stack[max_i:]


                if not succeed:
                    right_comparation_stack.append((tmp_val,tmp_index))
                              

                # print("new_area:", new_area)
                                    
            # elif next_val>cur_min: # Not possible
            else:
                raise(Exception("Error"))

            
            # print("\n")

        return cur_area


