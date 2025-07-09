unsorted_list = [35, 73, 90, 65, 23, 86, 43, 81, 34, 58]

def main():
    insertion_sort(unsorted_list)
    print (unsorted_list)

def insertion_sort(unsorted_list):
    for i in range(2, len(unsorted_list)):
        insert(unsorted_list, i)

def insert(unsorted_list, j):
    if j == 0 or unsorted_list[j-1] <= unsorted_list[j]:
        return
    
    unsorted_list[j-1], unsorted_list[j] = unsorted_list[j], unsorted_list[j-1]
    insert(unsorted_list, j - 1)

if __name__ == '__main__':
    main()
