"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.
"""
#C:\Users\kaiba\OneDrive\Asztali gép\LeetCode 75\LeetCode-75\exercise_one.py


def mergeAlternately():
    word_one = "abc"
    word_two = "pqr"
    first_word_one = word_one[0]
    first_word_two = word_two[0]
    # TODO: Make this part working 
    first_word = int(word_one) - int(first_word_one)
    # TODO: Make this part working as well 
    second_word = word_two - first_word_two
    #This is just the output
    print(first_word + second_word)
    



if __name__ == "__main__":
    mergeAlternately()