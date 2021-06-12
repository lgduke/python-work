#list 순서를 가진 객체

subway1 = 10
subway2 = 20
subway3 = 30

subway = [10,20,30]
print(subway)

subway = ["Lee","Kim","Park"]
print(subway)

# where is kim
print(subway.index("Kim"))
# Haha get in to the list
subway.append("Haha")
print(subway)

#Jeong into after Lee
subway.insert(1,"Jeong")
print(subway)

#Delete last one
print(subway.pop())
print(subway)

#Number of same name
subway.append("Lee")
print(subway)
print(subway.count("Lee"))

#sort list
num_list=[5,2,4,3,1]
print(num_list)
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)
#num_list.clear()
#print(num_list)

#Vartious type
mix_list =["Jo", 20, False]
print(mix_list)

num_list.extend(mix_list)
print(num_list)

