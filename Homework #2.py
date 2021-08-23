# Homework 2

# P1
# Given a list, find value 20 in the list, replace it with 200. Only update the first occurrence of a value.

# list1 = [5, 10, 15, 20, 25, 50, 20]
# list1[3] = 200
# print(list1)

# P2
# Given a list, remove the first occurrence of 20 from the list.

# list1 = [5, 20, 15, 20, 25, 50, 20]
# list1.remove(20)
# print(list1)

# P3
# Given a list, print the second largest element.

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
# Given a dictionary, remove the given key.

# dict1 = {'a':1,'b':2,'c':3,'d':4}
# dict2 = {'a':1,'b':2,'c':3,'d':4, 'e':5}
# dict1.pop('a')
# dict2.pop('e')
# print(dict1)
# print(dict2)

# P6
# Given a set, check if the given number exists.

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
# #

#
# sum1 = 0
# n = int(input("Please enter number "))
# for i in range(1, n + 1, 1):
#     sum1 += i
# print("\n")
# print("Sum is: ", sum1)
#
# n = int(input())
# m = int(input())
# l = []
# for i in range(n):
#     l.append(int(input()))
# x = 0
# for i in range(len(l)):
#     if l[i] == m:
#         x +=1
# print(x)
#
#
# n = int(input())
# l = []
# sum = 1
# while n//10 != 0:
#     l.append(n % 10)
#     n = n // 10
# l.append(n)
# l.reverse()
# for i in range(len(l)):
#     if l[i] != 0:
#         sum = sum * l[i]
# #
# dict_1 = {'key1': 'value1', 'key2': 'value2', 'key3': 3}
# dict_2 = {''}
# # phonebook = {'Name': ['John', 'Mary', 'Kate'], 'Phone': [123123, 412412, 512214]}
#
# phonebook = {'John': 123123, 'Mary': 412412, 'Kate': 129837123}
# # print(phonebook[input()])
# print(dict_1.values())

# def my_sum_1(a, b):
#     print(a + b)
# my_sum_1(7, 9)
#
# def multi(a, b):
#     print(a*b)
# multi(156, 69)
#
# def my_sum_2 (a,b):
#     print('Sum of {} {} equls {}'.format(a,b, a+b))
#     return a + b
#
# x_2 = my_sum_2(15, 69)

# lst = [15, 6, 9, 34, 1]
# h = lst.sort()
# print(lst)

# def equals_ten (x):
#     if x == 10:
#         print('x is {}'.format(x))
#         return x**2
#     else:
#         print('x is not ten, but it is {}'.format(x))
#         return x**3
# y = int(input())
# z = equals_ten(y)
# print(z)

# lst1 = [15, 6, 9, 34, 1]
#
#
# def sort(lst1):
#     for i in range(len(lst1)):
#         for j in range(len(lst1)):
#             print(lst1)
#
#             if lst1[i] < lst1[j]:
#                 lst1[i], lst1[j] = lst1[j], lst1[i]
#                 print(lst1)
# input_string = input('Enter elements of a list separated by space ')
# print("\n")
# user_list = input_string.split()
# # print list
# print('list: ', user_list)
#
# # convert each item to int type
# for i in range(len(user_list)):
#     # convert each item to int type
#     user_list[i] = int(user_list[i])
#
# # Calculating the sum of list elements
# print("Sum = ", sum(user_list))


