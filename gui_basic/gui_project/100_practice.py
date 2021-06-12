# lst = [1,2,3,4,5]
# print(lst)
# lst.reverse()
# print(lst)

# lst2 = [5,6,7,8,9]
# print("before lst2 reverse : ", lst2)
# lst3 = reversed(lst2)
# print("after lst2 reverse : ", lst2)
# print("after lst3 reverse : ", list(lst3))

eng = ["apple","banana","orange"]
kor = ["사과","바나나","오렌지"]

mixed = list(zip(kor, eng))
print(mixed)

kor2, eng2 = zip(*mixed) 
print(kor2)
print(eng2)
