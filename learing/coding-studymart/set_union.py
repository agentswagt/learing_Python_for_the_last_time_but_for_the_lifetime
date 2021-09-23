a = {1,2,3,4,5}
b = {2,4,6,5}
c = {5,6,7,8,9}

result = a.union(b)
result = a | b 
print(result)d1 = {"name": "shagato chy", "age": 17, "college": "cuet"}
print(d1["name"])
d3 = d1.copy()

print(d3, len(d1))

#for adding:
d1["varsity"] = "Buet"
print(d1)

#for remove

d1.pop("varsity")

d1.clear()
print(d1)