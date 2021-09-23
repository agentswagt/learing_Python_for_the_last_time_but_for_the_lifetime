#find max number out of three max number

x = [1, 2, 3]
if x[0] > x[1] and x[0] > x[2]:
    print("{} is the max number".format(x[0]))
if x[1] > x[0] and x[1] > x[2]:
    print("{} is the max number".format(x[1]))
else:
    print("3 is the max number")