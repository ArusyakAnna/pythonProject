# Homework 3
# Salaries

def max_min(lst):
    lst.sort(reverse=True)
    return lst[0] - lst[-1]

lst = []
n = int(input())
for i in range(0, n):
    el = int(input())
    lst.append(el)

print(max_min(lst))
