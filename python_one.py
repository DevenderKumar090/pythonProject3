#
# #Write a Python program to perform a deep flattening of a list
# # Original list elements:
# # [1, [2], [[3], [4], 5], 6]
# # Deep flatten the said list:
# # [1, 2, 3, 4, 5, 6]
# import itertools
#

#
# from collections.abc import Iterable
# def deep_flatten(lst):




#   return ([a for i in lst for a in
#           deep_flatten(i)] if isinstance(lst, Iterable) else [lst])
# nums = [1, [2], [[3], [4], 5], 6]
# print("Original list elements:")
# print(nums)
# print()
# print("Deep flatten the said list:")
# print(deep_flatten(nums))
# nums = [[[1, 2, 3], [4, 5]], 6]
# print("\nOriginal list elements:")
# print(nums)
# print()
# print("Deep flatten the said list:")
# print(deep_flatten(nums))
#
#
# # def flattenlist(_2dlist):
# #     # defining an empty list
# #     flatlist = []
# #     # Iterating through the outer list
# #     for item in _2dlist:
# #         if type(item) is list:
# #             # If the item is of the list type, iterating through the sub-list
# #             for element in item:
# #                 flatlist.append(element)
# #         else:
# #             flatlist.append(item)
# #     return flatlist
# #
# #
# # # defining the nested list
# # nestedlist = [1, [2], [[3], [4], 5], 6]
# # print('Genuine List:', nestedlist)
# # print('Converted Flat List:', flattenlist(nestedlist))
#
# # defining the nested list
# nestedlist = [1, [2], [[3], [4], 5], 6]
# # list comprehension
# flatlist = [element for sub_list in nestedlist for element in sub_list]
# print('Genuine list:', nestedlist)
# print('Converted list:', flatlist)



fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)