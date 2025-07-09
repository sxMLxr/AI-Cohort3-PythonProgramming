#How I fixed sort

def insertionSort(unsorted_list):
    for j in range(len(unsorted_list)):
        while j > 0:
            if unsorted_list[j-1] > unsorted_list[j]:
                unsorted_list[j-1], unsorted_list[j] = unsorted_list[j], unsorted_list[j-1]
            else:
                break
            j -= 1

def main():    
    begin_time = datetime.datetime.now()
    recursion_sort(unsorted_list, counter-1)
    print(unsorted_list)
    print(datetime.datetime.now() - begin_time)

main()
