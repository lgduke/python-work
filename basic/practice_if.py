#weather = "미세먼지"
weather = input("How is weather? ")
if weather == "비" or weather == "눈":
    print("Take Umbrella")
elif weather == "미세먼지":
    print("Take Mask")
else:
    print("Nothing need")

temp = int(input("Temperature ? "))
if 30 <= temp :
    print("It is Hot, Don t go out")
elif 10 <= temp and temp < 30:
    print("it is fine")
elif 0 <= temp < 10:
    print("Take outter")
else:
    print("It is too cold, don't go out")