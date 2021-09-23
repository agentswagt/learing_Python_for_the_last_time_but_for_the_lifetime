a = 5
b = 10
"""
#step 1
c = ""
c = a
a = b
b = c
print("Step 1 a: {} b: {}".format(a, b)) 
"""
#step2

a = a+b
b = a-b
a = a-b 

print("Step 2 a: {} b: {}".format(a, b))

#step3
a,b = b, a
print("Step 3 a: {} b: {}".format(a,b))