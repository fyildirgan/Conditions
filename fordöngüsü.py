# Döngüler (LOOPS)
# for loop
students = ["John", "Mark", "Venessa", "Mariam"]
print(students[0])
print(students[1])
print(students[2])

for student in students:
    print(student)

for student in students:
    print(student.upper())

salaries = [1000, 2000, 3000, 4000, 5000]
for salary in salaries:
    print(salary)

for salary in salaries:
    print(int(salary*20/100 + salary))

for salary in salaries:
    print(int(salary*30/100 + salary))

def new_salary(salary, rate):
    print(int(salary * rate / 100 + salary))
    return (salary*rate/100 + salary)


new_salary(1500, 10)
new_salary(2000, 20)

for salary in salaries:
    print(int(new_salary(salary, 20)))

salaries2 = [10700, 25000, 30400, 40300, 50200]
for salary in salaries2:
    print((new_salary(salary, 15)))

for salary in salaries:
    if salary >= 3000:
            print((new_salary(salary, 10)))
    else:
            print((new_salary(salary, 20)))




