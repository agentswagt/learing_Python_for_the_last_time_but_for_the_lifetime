import sys
hello = ("shagato", "hello", "bon")

list =  ["shagato", "hello", "bon"]
#unchangable data
print("hello ", sys.getsizeof(hello))
print(list, sys.getsizeof(list))
del hello
print(hello)