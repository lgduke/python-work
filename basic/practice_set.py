# 집합(Set)
# 중복암됨. 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"Kim","Yoo","Yang"}
python = set(["Kim","Park"])

#교집합
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

#차집합
print(java - python)
print(java.difference(python))

#add
python.add("Tae")
print(python)

java.remove("Kim")
print(java)