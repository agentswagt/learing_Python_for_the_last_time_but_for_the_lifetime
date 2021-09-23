#python assert statement | error handling

def MySalary(salary):
    #assert <condition>, "message"
    assert salary > 0, "Invalid Insert"
    print("My salary is {}".format(salary))

MySalary(1000)