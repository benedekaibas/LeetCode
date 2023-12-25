"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.
"""
#C:\Users\kaiba\OneDrive\Asztali gép\LeetCode 75\LeetCode-75\exercise_one.py


def mergeAlternately():
    word_one = "abc"
    word_two = "pqr"
    count_one = -1
    for index in word_one:
        count_one += 1
        print(f"{index}: {count_one}")

        # TODO: Finish this part since it will work 
        if count_one % 2 != 0:
            print(index)
        


    print("\n")
    count_two = -1
    for index in word_two:
        count_two += 1
        print(f"{index}: {count_two}")
        




if __name__ == "__main__":
    mergeAlternately()