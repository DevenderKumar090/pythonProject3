# # Check if main_set is a strict superset or not
# main_set = [1, 2, 3, 4, 5, 6, 17, 8, 9, 10, 11, 12, 23, 45, 84, 78]
# set1 = [1, 2, 3, 4, 5]
# set2 = [100, 78, 12]
# set3 = [6, 23, 1, 45]
#
#
# def superset_main(self):
# find length of each string in list in optimised way
# input_list = ['Tina', 'Raj', 'Tom']
# # output : [4, 3, 3]
# len(input_list)
# print(input_list)
import re

# Question
# 3:
# Text
# manipulation
# 1.
# Remove
# all
# the
# symbols in the
# text.Keep
# only
# alphanumeric
# values and spaces.
# 2.
# Split
# the
# text
# to
# list
# of
# sentence.
# 3.
# Split
# each
# sentence
# into
# list
# of
# words.
# 4.
# Replace
# acronyms(case
# insensitive) with their full forms.
# 5.
# Find
# the
# list
# of
# unique
# words in the
# text.

text = """
The quick brown cat jumps over the lazy DOG.
the qu!ck Brown cAT, jump$ over 100 l@zy dog.
The quick brown DoG; jumps 0vEr the crazy CAT. 

"""

text = re.sub('[^A-Za-z0-9]+','' , text)
print(text)
# print("The given string is")
# print(text)
# print("Removing special characters and white spaces")
# print(re.sub('[^A-Za-z0-9]+', '',  text))