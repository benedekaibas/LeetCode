"""27. Remove Element"""

from typing import List

def remove_element(nums: List[int], val: int) -> int:
    """Function for implementing remove element method."""
    if val in nums:
        nums.remove(val)
        new_list = nums
        return new_list
        
if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    store_rmv_elmnt = remove_element(nums, val)
    print(store_rmv_elmnt)
