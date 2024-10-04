"""Merge Sorted Array"""
from typing import List

def merge_array(list_one: List[int], m: int, list_two: List[int], n: int) -> None:
    """Function for merging arrays."""
    list_one = list_one[:m] + list_two[:n]
    return sorted(list_one)
    

if __name__ == "__main__":
    m = 0
    n = 1
    list_one = [0]
    list_two = [1]
    print(merge_array(list_one, m, list_two, n))
