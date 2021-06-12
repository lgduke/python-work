#local, global variable

gun = 10

def checkpoint(soldiers):
    # gun = 20 #local var
    global gun #use global gun variable 
    gun = gun - soldiers
    print("In function, No of gun left is {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("In function, No of gun left is {0}".format(gun))    
    return gun

print("Total no of gun is {0}".format(gun))
# checkpoint(2)
gun = checkpoint_ret(gun,2)

print("Total no of gun left after check is {0}".format(gun))