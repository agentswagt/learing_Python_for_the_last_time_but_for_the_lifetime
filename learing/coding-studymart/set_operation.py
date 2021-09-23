hello1 = {1,2,3}
hello2 = {4,5,6}
hello3 = {7,8,9,4}
#hello_f = hello3.intersection(hello2)
hello_f = hello3.difference(hello2)
print(hello_f)
hello_f = hello2.difference(hello3)
print(hello_f)
#hello_f = hello2.symmetric_difference(hello3)
#print(hello_f)

s1 = [1, 2, 3, 3]
#print(set(s1))