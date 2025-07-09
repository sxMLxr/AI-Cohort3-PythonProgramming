unsorted_list = [35, 73, 90, 65, 23, 86, 43, 81, 34, 58, 23]

def insertion_sort(unsorted_list):
    
    for i, v in enumerate(unsorted_list):
        
        while i > 0:
            if unsorted_list[i - 1] > unsorted_list[i]:
                unsorted_list[i - 1], unsorted_list[i] = unsorted_list[i], unsorted_list[i - 1]
            
            else:
                # if previous number is smaller than current number, break out of the while loop.
                break
            i -= 1
            
insertion_sort(unsorted_list)
print(unsorted_list)
