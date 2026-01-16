from typing import MutableSequence

def bubble_sort(data: MutableSequence) -> None:
 '''Sorts a mutable sequence'''

 for sorted_partition in range(len(data)-1,0,-1):
    swapped = False
    for i in range(sorted_partition):
      if data[i] > data[i+1]:
            data[i],data[i+1] = data[i+1],data[i]
            swapped = True
    # print(f"Sorted {sorted_partition}: {data}")
    if not swapped:
        break



if __name__ == '__main__':
    from array import array
    # numbers = array('i',[5,3,8,6,2,7,4,1])
    numbers = [2,4,3,1,5,6,7,8]

    print("Before sorting:", numbers)
    bubble_sort(numbers)
    print("After sorting:", numbers)

    # O(n^2) time complexity

'''Initiallt the test cases took roughly 13.6 seconds to run 18 test cases but with the addition 
of swapped flag for early stopping the time was significantly reduced to 8.5 seconds for 18 test cases.'''
