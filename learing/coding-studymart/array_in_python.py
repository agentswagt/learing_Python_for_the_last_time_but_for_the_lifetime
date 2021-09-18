from array import *

salary = array("i", [30000, 40000, 50000])
print(salary)
for i in range(3):
    print(salary[i])
print(salary.append(2299))

salary.reverse()
salary.remove(30000)
print(salary.buffer_info())
print(salary)