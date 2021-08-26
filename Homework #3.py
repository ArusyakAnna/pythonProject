# Homework 3
# Salaries

# def max_min(lst):
#     lst.sort(reverse=True)
#     diff = lst[0] - lst[-1]
#     return diff
#
# lst = []
# n = int(input())
# for i in range(0, n):
#     el = int(input())
#     lst.append(el)
#
# print(max_min(lst))

# Boring Numbers

# x = int(input())

# switch = False

# y = str(x)
# lst = list(y)
# for i in range(0, len(lst)):
#     for j in range(0, len(lst) - i - 1):
#         if lst[j] == lst[j + 1]:
#             print('Boring')
#         else:
#             print('Interesting')

# boring

# x = int(input())
#
# y = str(x)
# lst = list(y)
#
# result = all(el == lst[0] for el in lst)
# if result:
#     print('Bor')
# else:
#     print('int')


# List 1

# def conv_to_str(lst):
#     str1 = ""

#     for i in lst:
#         str1 += i

#     return str1


# lst = ['a', 'b', 'c', 'd']
# print(conv_to_str(lst))

# List 2

# def sec_small_el(list_n):
#     list_n.sort()
#     sec_sm_el = list_n[1]
#     return sec_sm_el


# s = [1, 2, -8, -2, 0, -2]
# print(sec_small_el(s))


# Largest number

# x = int(input())
# y = str(x)
# lst = list(y)

# result = False
# for i in range(len(lst)):
#     for j in range(len(lst)):
#         if lst[0] < lst[j]:
#             result = True
# # result = (lst[0] > lst[i] for i in lst)
# if result:
#     print('yes')
# else:
#     print('No')


# Number Of Divisors

# x = int(input())
# count_of_div = 2
# for i in range(2, x//2+1):
#     if x % i == 0:
#         count_of_div +=1

# print(count_of_div)

