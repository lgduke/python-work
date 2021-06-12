# print("Python","Java")
# print("Python"+"Java")
# print("Python","Java",sep=",")
# print("Python","Java","Javascript",sep=" vs ")
# print("Python","Java","Javascript",sep=" vs ", end="? ")
# print("What is more funny?")

# import sys
# print("Python","Java","Javascript",file=sys.stdout)
# print("Python","Java","Javascript",file=sys.stderr)

# Test score dictionary
scores = {"Math":0, "Eng":50, "Coding":100}
for subject, score in scores.items():
#    print(subject,score)
    print(subject.ljust(8),str(score).rjust(4), sep=":")


#bank waiting lines 001,002,003~~~

for num in range(1, 21):
    print("Waiting No : " +str(num).zfill(3))

answer = input("Type whatever : ")
print(type(answer))
print("The value you put  is  " + answer)