from typing import MutableSequence

def selection_sort(data: MutableSequence) -> None:
    '''Sorts a mutable sequence using selection sort algorithm'''
    
    for last_unsorted_index in range(len(data)-1,0,-1):
        largest = 0
        for i in range(1,last_unsorted_index+1):
            if data[i] > data[largest]:
                largest = i
        data[largest],data[last_unsorted_index] = data[last_unsorted_index],data[largest]
        # print(f"Sorted {last_unsorted_index}: {data}")

if __name__ == '__main__':
    from array import array
    # numbers = array('i',[5,3,8,6,2,7,4,1])
    numbers = [2,4,3,1,5,6,7,8]

    print("Before sorting:", numbers)
    selection_sort(numbers)
    print("After sorting:", numbers)

    # O(n^2) time complexity