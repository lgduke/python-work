cabinet = {3:"Yoo", 100:"Kim"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

# print(cabinet[5])
# print("Hi")

print(cabinet.get(5))
print(cabinet.get(5,"Available"))

print("Hi")

print(3 in cabinet) #True
print(5 in cabinet) #False

cabinet_2 = {"A-3":"Yoo2","B-100":"Kim2"}
print(cabinet_2["A-3"])
print(cabinet_2["B-100"])

cabinet_2["A-3"] = "Jong2" #Update
cabinet_2["C-20"] = "Jo2"
print(cabinet_2["C-20"])

# 
del  cabinet_2["A-3"]
print(cabinet_2)

print(cabinet_2.keys())
print(cabinet_2.values())
print(cabinet_2.items())

#Go out
cabinet_2.clear()
print(cabinet_2)