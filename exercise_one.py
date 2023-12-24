"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.
"""
#C:\Users\kaiba\OneDrive\Asztali gép\LeetCode 75\LeetCode-75\exercise_one.py


def mergeAlternately():
    word1 = "abc"
    word2 = "pqr"
    first = word1[0]
    sol = word1 + word2 
    print(f"{sol}\n{first}")
    



if __name__ == "__main__":
    mergeAlternately()