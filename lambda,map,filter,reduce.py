# lambda, map, filter, reduce
def summer(a, b):
    print(a + b)
    return a + b

print(summer(1, 3)  * 9)

new_sum = lambda a, b: a + b
print(new_sum(4, 5))

#map

salaries = [1000, 2000, 3000, 4000, 5000]
def new_salary(x):
    return x * 20 / 100 + x
new_salary(5000)

for salary in salaries:
    print(new_salary(salary))

print(list(map(new_salary, salaries)))

#list(map(lambda x: x * 20 / 100 + x, salaries))
#del new_sum

print(list(map(lambda x: x * 20 / 100 + x, salaries)))
print(list(map(lambda x: x ** 2, salaries)))

#FILTER
list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x % 2 == 0, list_store)))

#REDUCE
from functools import reduce
list_store1 = [1, 2, 3, 4]
print(reduce(lambda a, b: a + b, list_store1))