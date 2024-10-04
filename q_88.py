"""Merge Sorted Array"""

def merge_array(list_one: List[int], m: int, list_two: List[int], n: int) -> None:
    """Function for merging arrays."""
    list_one = list_one[:m] + list_two[:n]


if __name__ == "__main__":
    m = 3
    n = 3
    list_one = [1,2,3,0,0,0]
    list_two = [2,5,6]
