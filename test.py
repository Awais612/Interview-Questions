def sort_colors (arr):
    #TODO: WRITE - CODE - HERE
    start = 0
    cur = 0
    end = len(arr) - 1

    while start < end and cur <= end:
        if arr[cur] == 0:
            arr[start], arr[cur] = arr[cur], arr[start]
            start += 1
            cur += 1
        elif arr[cur] == 1:
            cur += 1
        elif arr[cur] == 2:
            arr[cur], arr[end] = arr[end], arr[cur]
            end -= 1

input_list = [2,0,2,1,1,0]
sort_colors(input_list)
print(input_list)