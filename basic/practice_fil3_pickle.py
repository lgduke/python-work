import pickle
# profile_file = open("profile.pickle", "wb") # pickle 사용을 위해 항상 b(binary) 사용
# profile = {"name":"Paek", "Age":"30", "Hobby":["Soccer","Golf","Coding"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를  file에 저장
# profile_file.close()

profile_file = open("profile.pickle", "rb") 
# pickle 사용을 위해 항상 b(binary) 사용

profile = pickle.load(profile_file) 
# file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

