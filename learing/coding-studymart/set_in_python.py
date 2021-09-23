hello = [1,2,3,4,5]

hello = set(hello)
print(hello)
hello.add(6)
hello.update([7, 8, 9])
print(hello)


hello2 = {10,11,12}
hello.update(hello2)
hello.remove(1)
hello.discard(15)
print(hello)