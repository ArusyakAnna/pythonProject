# Homework 2

#P1
#Given a list, find value 20 in the list, replace it with 200. Only update the first occurrence of a value.

# list1 = [5, 10, 15, 20, 25, 50, 20]
# list1[3] = 200
# print(list1)

# P2
#Given a list, remove the first occurrence of 20 from the list.

# list1 = [5, 20, 15, 20, 25, 50, 20]
# list1.remove(20)
# print(list1)

# P3
#Given a list, print the second largest element.

# list1 = [10, 20, 4]
# list2 = [70, 11, 20, 4, 100]
# list1.sort()
# list2.sort()
# print(list1[-2])
# print(list2[-2])

# P4
# Given 3 dictionaries, create a new dictionary, which contains all of them.

# dic1 = {1:10, 2:20}
# dic2 = {3:30, 4:40}
# dic3 = {5:50, 6:60}
# dic4 = {}
# dic4.update(dic1)
# dic4.update(dic2)
# dic4.update(dic3)
# print(dic4)

# P5
#Given a dictionary, remove the given key.

# dict1 = {'a':1,'b':2,'c':3,'d':4}
# dict2 = {'a':1,'b':2,'c':3,'d':4, 'e':5}
# dict1.pop('a')
# dict2.pop('e')
# print(dict1)
# print(dict2)

# P6
#Given a set, check if the given number exists.

# s1 = {1, 10, 90, 9}
# n1 = 90 in s1
# print(n1)
#
# s2 = {6, 4, 10, 20, 21, 3}
# n2 = 90 in s2
# print(n2)

# P7
# For a given n, create a list (using loops, or list comprehension), which
# contains all natural numbers less or equal n divisible by 7.

# lst = []
# n = int(input())
# for i in range(1, n):
#   if i % 7 == 0:
#     lst.append(i)
#
# print(lst)
