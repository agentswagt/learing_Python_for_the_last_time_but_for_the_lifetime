student = {1: {"name": "Shagato Chy", "age": 24, "sex": "male"}, 2: {"name": " Chy", "age": 4, "sex": "male"}, 3: {"name": "Chy", "age": 24, "sex": "male"}}
print(student)
print(student[1]["sex"])
print(student[1]["name"])
print(student[1]["age"])

student[4] = {}
student[4]["name"] = "hello"
student[4]["age"] = "19"
print(student)

del student[4]["age"]
print(student)