from typing import MutableSequence

def bubble_sort(data: MutableSequence) -> None:
 '''Sorts a mutable sequence'''

 for sorted_partition in range(len(data)-1,0,-1):
    for i in range(sorted_partition):
      if data[i] > data[i+1]:
            data[i],data[i+1] = data[i+1],data[i]
    print(f"Sorted {sorted_partition}: {data}")




if __name__ == '__main__':
    from array import array
    numbers = array('i',[5,3,8,6,2,7,4,1])

    print("Before sorting:", numbers)
    bubble_sort(numbers)
    print("After sorting:", numbers)

    # O(n^2) time complexity

