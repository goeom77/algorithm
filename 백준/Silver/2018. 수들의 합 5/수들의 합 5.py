all_sum = 1
s_idx = 1
e_idx = 1
cnt = 0
get_answer = int(input())
if get_answer == 1:
    print(1)
elif get_answer == 2:
    print(1)
elif get_answer == 3:
    print(2)
else:
    while e_idx != (get_answer//2)+2:
        if all_sum == get_answer:
            cnt += 1
            all_sum -= s_idx
            s_idx += 1
        elif all_sum < get_answer:
            e_idx += 1
            all_sum += e_idx
        else:
            all_sum -= s_idx
            s_idx += 1
    print(cnt+1)
