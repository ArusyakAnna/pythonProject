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

def dig_convert(num):
    digit_string = str(num)
    digit_map = map(int, digit_string)
    digit_list = list(digit_map)
    return digit_list


List = dig_convert(num=)
# Result from count matches with result from len()
result = List.count(List[0]) == len(List)
if (result):
   print("Boring")
else:
   print("Interesting")